from __future__ import annotations

from typing import TYPE_CHECKING

from sec_parser.processing_steps.individual_semantic_element_extractor.single_element_checks.abstract_single_element_check import (
    AbstractSingleElementCheck,
)
from sec_parser.processing_steps.top_section_manager_for_10q import (
    TopSectionManagerFor10Q,
)


from sec_parser.processing_steps.top_section_manager_for_10k import (
    TopSectionManagerFor10K,
    TopSectionManagerFor10KForKR,
)

if TYPE_CHECKING:  # pragma: no cover
    from sec_parser.semantic_elements.abstract_semantic_element import (
        AbstractSemanticElement,
    )


def _is_match_part_or_item_in_10q(text: str) -> bool:
    return TopSectionManagerFor10Q.is_match_part_or_item(text)


class TopSectionTitleCheckIn10Q(AbstractSingleElementCheck):
    def contains_single_element(self, element: AbstractSemanticElement) -> bool | None:
        match_count = element.html_tag.count_text_matches_in_descendants(
            _is_match_part_or_item_in_10q,
            exclude_links=True,
        )

        if match_count >= 1:
            return False

        return None


def _is_match_part_or_item_in_10k(text: str) -> bool:
    return TopSectionManagerFor10K.is_match_part_or_item(text)


class TopSectionTitleCheckIn10K(AbstractSingleElementCheck):
    def contains_single_element(self, element: AbstractSemanticElement) -> bool | None:
        match_count = element.html_tag.count_text_matches_in_descendants(
            _is_match_part_or_item_in_10k,
            exclude_links=True,
        )

        if match_count >= 1:
            return False

        return None


def _is_match_part_or_item_in_10k_for_kr(text: str) -> bool:
    return TopSectionManagerFor10KForKR.is_match_part_or_item(text)


class TopSectionTitleCheckIn10KForKR(AbstractSingleElementCheck):
    def contains_single_element(self, element: AbstractSemanticElement) -> bool | None:
        match_count = element.html_tag.count_text_matches_in_descendants(
            _is_match_part_or_item_in_10k_for_kr,
            exclude_links=True,
        )

        if match_count >= 1:
            return False

        return None
