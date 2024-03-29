import pymongo
from pydantic import BaseModel
from pymongo import IndexModel

from src.common.models.BaseDocument import BaseDocument


class RuleInfo(BaseModel):
    rule_id: int
    version: int


class Analysis(BaseDocument):
    # TODO : 해외/국내 구분 값 추가
    code: str
    rule_info: RuleInfo
    # TODO : 분석 과정 추가 (어떤 룰이 통과했고, 실패했는지)
    is_matched_rule: bool

    class Settings:
        indexes = [
            IndexModel(
                [
                    ("code", pymongo.ASCENDING),
                    ("rule_info", pymongo.ASCENDING),
                ],
                unique=True
            ),
        ]
