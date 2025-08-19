from uuid import UUID
from src.models.schemas import ReportResponse

def get_sample_report() -> ReportResponse:
    """Returns the hardcoded compliance report data"""
    
    return ReportResponse(
        status="success",
        id=UUID("7ed5921f-641b-4956-9162-7809aa2eef48"),
        pdf_url="https://example.com/dummy-report.pdf",
        results=[
            {
                "section_id": UUID("e38c08c4-62a1-441d-9fd4-326f7f385c1d"),
                "sub_domain_code": 1,
                "sub_domain": "Industry Standards",
                "section_code": 1.1,
                "section_title": "Third party adheres to industry best practices and quality standards.",
                "sub_questions_results": [
                    {
                        "question_id": UUID("0dd8fd6e-dd2d-481c-9c49-45645ed7e053"),
                        "question_text": "Does the third party follow standard operating procedures for project management?",
                        "display_text": "Does the third party follow standard operating procedures for project management?",
                        "answer": "Yes, the organization follows defined project management procedures including regular status reviews and milestone tracking.",
                        "title_relevance_score": 8,
                        "title_relevance_color": "green",
                        "references": [
                            { "source": "Project Management Handbook.pdf", "pages": [2, 5] }
                        ]
                    },
                    {
                        "question_id": UUID("2a4ae291-08d4-45db-a238-ff5a4301b5ee"),
                        "question_text": "List any certifications held by the third party relevant to industry standards.",
                        "display_text": "List any certifications held by the third party relevant to industry standards.",
                        "answer": "- **ISO 9001:2015**\n  - Expiry Date: 2026-03-31\n- **ISO 14001:2015**\n  - Expiry Date: 2025-12-15",
                        "title_relevance_score": 7,
                        "title_relevance_color": "green",
                        "references": [
                            { "source": "ISO Certification Summary.pdf", "pages": [1, 2] }
                        ]
                    },
                    {
                        "question_id": UUID("f5b46b7e-5f05-4c39-8bb7-4fac088cddce"),
                        "question_text": "Are the third party's certifications currently valid?",
                        "display_text": "Are the third party's certifications currently valid?",
                        "answer": "- **ISO 9001:2015**: In Date\n- **ISO 14001:2015**: In Date",
                        "title_relevance_score": 9,
                        "title_relevance_color": "green",
                        "references": [
                            { "source": "ISO Certification Summary.pdf", "pages": [1, 2] }
                        ]
                    }
                ],
                "section_status": "Mature",
                "section_justification": "- Certifications are valid and align with industry standards.",
                "section_summary": "The organization maintains valid ISO certifications and follows standard practices.",
                "evidence_required": True
            },
            {
                "section_id": UUID("6a0100fe-b414-4144-8836-b0e5a23a908c"),
                "sub_domain_code": 2,
                "sub_domain": "Governance and Process",
                "section_code": 2.1,
                "section_title": "Third party has a governance framework in place with clearly defined roles.",
                "sub_questions_results": [
                    {
                        "question_id": UUID("d21eabb6-f6b8-4ad2-a205-2325421f7087"),
                        "question_text": "Is there a defined hierarchy for decision-making within the organization?",
                        "display_text": "Is there a defined hierarchy for decision-making within the organization?",
                        "answer": "Yes, the organization has a structured decision-making hierarchy including managers, directors, and executives.",
                        "title_relevance_score": 8,
                        "title_relevance_color": "green",
                        "references": [
                            { "source": "Governance Manual.pdf", "pages": [3] }
                        ]
                    },
                    {
                        "question_id": UUID("ae366a56-d88a-4679-a3d5-bf7a096abe7e"),
                        "question_text": "List the key governance committees and their responsibilities.",
                        "display_text": "List the key governance committees and their responsibilities.",
                        "answer": "- **Risk Committee**: Oversees risk management policies.\n- **Audit Committee**: Monitors financial reporting and internal controls.\n- **Compliance Committee**: Ensures compliance with regulatory standards.",
                        "title_relevance_score": 9,
                        "title_relevance_color": "green",
                        "references": [
                            { "source": "Governance Manual.pdf", "pages": [4, 5] }
                        ]
                    },
                    {
                        "question_id": UUID("54c7fdfa-9625-4e69-9a94-5bcced2d2a27"),
                        "question_text": "Does the organization maintain a formal policy documentation for governance?",
                        "display_text": "Does the organization maintain a formal policy documentation for governance?",
                        "answer": "Yes, formal governance and policy documentation is maintained and updated annually.",
                        "title_relevance_score": 7,
                        "title_relevance_color": "green",
                        "references": [
                            { "source": "Governance Policy.pdf", "pages": [1, 2] }
                        ]
                    }
                ],
                "section_status": "Mature",
                "section_justification": "- Governance framework is formally documented with committees and defined responsibilities.",
                "section_summary": "The organization has an established governance framework with defined committees and policies.",
                "evidence_required": True
            }
        ]
    )