from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class Reference(BaseModel):
    source: str
    pages: List[int]

class SubQuestionResult(BaseModel):
    question_id: UUID
    question_text: str
    display_text: str
    answer: str
    title_relevance_score: int
    title_relevance_color: str
    references: List[Reference]

class SectionResult(BaseModel):
    section_id: UUID
    sub_domain_code: int
    sub_domain: str
    section_code: float
    section_title: str
    sub_questions_results: List[SubQuestionResult]
    section_status: str
    section_justification: str
    section_summary: str
    evidence_required: bool

class ReportResponse(BaseModel):
    status: str
    id: UUID
    pdf_url: str
    results: List[SectionResult]