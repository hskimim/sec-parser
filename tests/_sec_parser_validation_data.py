from __future__ import annotations

from collections.abc import Generator
from dataclasses import dataclass
from pathlib import Path

DEFAULT_VALIDATION_DATA_DIR = (
    Path(__file__).resolve().parent.parent.parent / "sec-parser-validation-data"
)


@dataclass(frozen=True)
class Report:
    document_type: str
    company_name: str
    report_name: str
    report_full_path: Path

    @property
    def expected_elements_json_path(self) -> Path:
        return self.report_full_path / "expected-semantic-elements-list.json"

    @property
    def actual_elements_json_path(self) -> Path:
        return self.report_full_path / "actual-semantic-elements-list.json"

    @property
    def primary_doc_html_path(self) -> Path:
        return self.report_full_path / "primary-document.html"

    @property
    def identifier(self) -> str:
        return f"{self.document_type}_{self.company_name}_{self.report_name}"


def filter_valid_directories(starting_directory: Path) -> Generator[Path, None, None]:
    for current_directory in starting_directory.iterdir():
        if current_directory.name.startswith("."):
            continue
        if not current_directory.is_dir():
            continue
        yield current_directory


def traverse_repository_for_reports(
    root_directory: Path | None = None,
) -> Generator[Report, None, None]:
    root_directory = Path(root_directory or DEFAULT_VALIDATION_DATA_DIR)
    for document_type_directory in filter_valid_directories(root_directory):
        for company_directory in filter_valid_directories(document_type_directory):
            for individual_report_directory in filter_valid_directories(
                company_directory,
            ):
                yield Report(
                    document_type=document_type_directory.name,
                    company_name=company_directory.name,
                    report_name=individual_report_directory.name,
                    report_full_path=individual_report_directory,
                )
