from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from docx import Document

from tools.convert_csv108_markdown_to_docx import (
    MarkdownTableError,
    apply_known_markdown_repairs,
    convert_one,
    parse_front_matter,
    parse_markdown_blocks,
)


ROOT = Path(__file__).resolve().parents[1]
CSV108 = ROOT / "CSV108"


def zip_text(path: Path, member: str) -> str:
    with zipfile.ZipFile(path) as archive:
        return archive.read(member).decode("utf-8")


class Csv108MarkdownParserTests(unittest.TestCase):
    def test_parse_front_matter_extracts_metadata_and_body(self) -> None:
        text = '---\ndocument_number: DOC-001\ntitle: "My Title"\n---\n\n# My Title\n\nBody'

        meta, body = parse_front_matter(text)

        self.assertEqual(meta["document_number"], "DOC-001")
        self.assertEqual(meta["title"], "My Title")
        self.assertIn("# My Title", body)

    def test_table_parser_rejects_inconsistent_pipe_counts(self) -> None:
        body = "# T\n\n| A | B |\n|---|---|\n| one | two | three |\n"

        with self.assertRaises(MarkdownTableError) as ctx:
            parse_markdown_blocks(body, source_name="bad.md")

        self.assertIn("bad.md", str(ctx.exception))
        self.assertIn("line 3", str(ctx.exception))

    def test_known_repairs_fix_current_csv108_table_issues(self) -> None:
        source = CSV108 / "076_System_Handover_and_Support_Model.md"
        repaired = apply_known_markdown_repairs(source, source.read_text(encoding="utf-8-sig"))
        _, body = parse_front_matter(repaired)

        blocks = parse_markdown_blocks(body, source_name=source.name)

        table_blocks = [block for block in blocks if block.kind == "table"]
        self.assertTrue(any(len(row) == 5 for block in table_blocks for row in block.rows))


class Csv108DocxConversionTests(unittest.TestCase):
    def test_convert_one_creates_controlled_docx_with_expected_structure(self) -> None:
        source = CSV108 / "001_CSV_Lifecycle_Management_Procedure.md"
        with tempfile.TemporaryDirectory() as tmp:
            output = convert_one(source, Path(tmp), fix_known_issues=False)

            self.assertTrue(output.exists())
            doc = Document(output)
            full_text = "\n".join([p.text for p in doc.paragraphs])
            self.assertIn("Site Computerised System Lifecycle Management Procedure", full_text)

            document_xml = zip_text(output, "word/document.xml")
            self.assertIn("<w:tblHeader", document_xml)

            core_xml = zip_text(output, "docProps/core.xml")
            self.assertIn("CSV108 Markdown DOCX Converter", core_xml)

            header_members = [
                name
                for name in zipfile.ZipFile(output).namelist()
                if name.startswith("word/header") and name.endswith(".xml")
            ]
            footer_members = [
                name
                for name in zipfile.ZipFile(output).namelist()
                if name.startswith("word/footer") and name.endswith(".xml")
            ]
            header_xml = "\n".join(zip_text(output, member) for member in header_members)
            footer_xml = "\n".join(zip_text(output, member) for member in footer_members)
            self.assertIn("QCLabOne 2.0", header_xml)
            self.assertIn("SOP-CSV-001", footer_xml)
            self.assertIn("PAGE", footer_xml)


if __name__ == "__main__":
    unittest.main(verbosity=2)
