from dataclasses import dataclass


@dataclass(frozen=True)
class TopSection:
    identifier: str
    title: str
    order: int
    level: int = 0


TopSectionType = TopSection

InvalidTopSection = TopSection(
    identifier="invalid",
    title="Invalid",
    order=-1,
    level=1,
)


ALL_10Q_SECTIONS = (
    TopSection(
        identifier="part1",
        title="Financial Information",
        order=0,
        level=0,
    ),
    TopSection(
        identifier="part1item1",
        title="Financial Statements",
        order=1,
        level=1,
    ),
    TopSection(
        identifier="part1item2",
        title="Management's Discussion and Analysis of Financial Condition and Results of Operations",
        order=2,
        level=1,
    ),
    TopSection(
        identifier="part1item3",
        title="Quantitative and Qualitative Disclosures About Market Risk",
        order=3,
        level=1,
    ),
    TopSection(
        identifier="part1item4",
        title="Controls and Procedures",
        order=4,
        level=1,
    ),
    TopSection(
        identifier="part2",
        title="Other Information",
        order=5,
        level=0,
    ),
    TopSection(
        identifier="part2item1",
        title="Legal Proceedings",
        order=6,
        level=1,
    ),
    TopSection(
        identifier="part2item1a",
        title="Risk Factors",
        order=7,
        level=1,
    ),
    TopSection(
        identifier="part2item2",
        title="Unregistered Sales of Equity Securities and Use of Proceeds",
        order=8,
        level=1,
    ),
    TopSection(
        identifier="part2item3",
        title="Defaults Upon Senior Securities",
        order=9,
        level=1,
    ),
    TopSection(
        identifier="part2item4",
        title="Mine Safety Disclosures",
        order=10,
        level=1,
    ),
    TopSection(
        identifier="part2item5",
        title="Other Information",
        order=11,
        level=1,
    ),
    TopSection(
        identifier="part2item6",
        title="Exhibits",
        order=12,
        level=1,
    ),
)


IDENTIFIER_TO_10Q_SECTION = {section.identifier: section for section in ALL_10Q_SECTIONS}


ALL_10K_SECTIONS = (
    TopSection(identifier="part1", title="PART I", order=0, level=0),
    TopSection(identifier="part1item1", title="Business", order=1, level=1),
    TopSection(identifier="part1item1a", title="Risk Factors", order=2, level=1),
    TopSection(identifier="part1item1b", title="Unresolved Staff Comments", order=3, level=1),
    TopSection(identifier="part1item1c", title="Cybersecurity", order=4, level=1),
    TopSection(identifier="part1item2", title="Properties", order=5, level=1),
    TopSection(identifier="part1item3", title="Legal Proceedings", order=6, level=1),
    TopSection(identifier="part1item4", title="Mine Safety Disclosures", order=7, level=1),
    TopSection(identifier="part2", title="PART II", order=8, level=0),
    TopSection(
        identifier="part2item5",
        title="Market for Registrant's Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities",
        order=9,
        level=1,
    ),
    TopSection(identifier="part2item6", title="[Reserved]", order=10, level=1),
    TopSection(
        identifier="part2item7",
        title="Management's Discussion and Analysis of Financial Condition and Results of Operations",
        order=11,
        level=1,
    ),
    TopSection(
        identifier="part2item7a", title="Quantitative and Qualitative Disclosures About Market Risk", order=12, level=1
    ),
    TopSection(identifier="part2item8", title="Financial Statements and Supplementary Data", order=13, level=1),
    TopSection(
        identifier="part2item9",
        title="Changes in and Disagreements with Accountants on Accounting and Financial Disclosure",
        order=14,
        level=1,
    ),
    TopSection(identifier="part2item9a", title="Controls and Procedures", order=15, level=1),
    TopSection(identifier="part2item9b", title="Other Information", order=16, level=1),
    TopSection(
        identifier="part2item9c",
        title="Disclosure Regarding Foreign Jurisdictions that Prevent Inspections",
        order=17,
        level=1,
    ),
    TopSection(identifier="part3", title="PART III", order=18, level=0),
    TopSection(
        identifier="part3item10", title="Directors, Executive Officers and Corporate Governance", order=19, level=1
    ),
    TopSection(identifier="part3item11", title="Executive Compensation", order=20, level=1),
    TopSection(
        identifier="part3item12",
        title="Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters",
        order=21,
        level=1,
    ),
    TopSection(
        identifier="part3item13",
        title="Certain Relationships and Related Transactions, and Director Independence",
        order=22,
        level=1,
    ),
    TopSection(identifier="part3item14", title="Principal Accountant Fees and Services", order=23, level=1),
    TopSection(identifier="part4", title="PART IV", order=24, level=0),
    TopSection(identifier="part4item15", title="Exhibit and Financial Statement Schedules", order=25, level=1),
    TopSection(identifier="part4item16", title="Form 10-K Summary", order=26, level=1),
)

IDENTIFIER_TO_10K_SECTION = {section.identifier: section for section in ALL_10K_SECTIONS}


ALL_10K_SECTIONS_KR = (
    TopSection(identifier="파트1", title="파트 I", order=0, level=0),
    TopSection(identifier="파트1항목1", title="비지니스", order=1, level=1),
    TopSection(identifier="파트1항목1a", title="위험 요인", order=2, level=1),
    TopSection(identifier="파트1항목1b", title="해결되지 않은 직원 의견", order=3, level=1),
    TopSection(identifier="파트1항목1c", title="사이버 보안", order=4, level=1),
    TopSection(identifier="파트1항목2", title="속성", order=5, level=1),
    TopSection(identifier="파트1항목3", title="법적 절차", order=6, level=1),
    TopSection(identifier="파트1항목4", title="광산 안전 공시", order=7, level=1),
    TopSection(identifier="파트2", title="파트 II", order=8, level=0),
    TopSection(
        identifier="파트2항목5",
        title="등록자의 보통주, 관련 주주 문제 및 발행자의 지분 증권 매입 시장",
        order=9,
        level=1,
    ),
    TopSection(identifier="파트2항목6", title="[보유]", order=10, level=1),
    TopSection(
        identifier="파트2항목7",
        title="재무 상태 및 운영 결과에 대한 경영진의 논의 및 분석",
        order=11,
        level=1,
    ),
    TopSection(identifier="파트2항목7a", title="시장 위험에 대한 정량적 및 정성적 공개", order=12, level=1),
    TopSection(identifier="파트2항목8", title="재무 제표 및 보충 데이터", order=13, level=1),
    TopSection(
        identifier="파트2항목9",
        title="회계 및 재무 공시에 대한 회계사의 변경 사항 및 회계사와의 의견 불일치",
        order=14,
        level=1,
    ),
    TopSection(identifier="파트2항목9a", title="제어 및 절차", order=15, level=1),
    TopSection(identifier="파트2항목9b", title="기타 정보", order=16, level=1),
    TopSection(
        identifier="파트2항목9c",
        title="검사를 방해하는 외국 관할권 관련 공시",
        order=17,
        level=1,
    ),
    TopSection(identifier="파트3", title="파트 III", order=18, level=0),
    TopSection(identifier="파트3항목10", title="이사, 임원 및 기업 지배구조", order=19, level=1),
    TopSection(identifier="파트3항목11", title="임원 보상", order=20, level=1),
    TopSection(
        identifier="파트3항목12",
        title="특정 수익 소유자의 증권 소유권 및 경영진 및 관련 주주 문제",
        order=21,
        level=1,
    ),
    TopSection(
        identifier="파트3항목13",
        title="특정 관계 및 관련 거래 및 이사 독립성",
        order=22,
        level=1,
    ),
    TopSection(identifier="파트3항목14", title="수석 회계사 수수료 및 서비스", order=23, level=1),
    TopSection(identifier="파트4", title="파트 IV", order=24, level=0),
    TopSection(identifier="파트4항목15", title="첨부 자료 및 재무 제표 일정", order=25, level=1),
    TopSection(identifier="파트4항목16", title="양식 10-K 요약", order=26, level=1),
)

IDENTIFIER_TO_10K_SECTION_KR = {section.identifier: section for section in ALL_10K_SECTIONS_KR}
