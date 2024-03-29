from typing import Optional, List

from sqlalchemy import and_

from src.common.models.builder import Builder
from src.common.models.filter_condition import FilterCondition
from src.company.model.company_info import CompanyInfo


class CompanyInfoFilterCondition(FilterCondition):
    def __init__(self):
        self.market_type: Optional[str] = None
        self.code: Optional[str] = None
        self.codes: Optional[List[str]] = None

    def get_filter(self):
        condition = []

        if self.market_type:
            condition.append(CompanyInfo.market_type == self.market_type)

        if self.code:
            condition.append(CompanyInfo.code == self.code)

        if self.codes:
            condition.append(CompanyInfo.code.in_(self.codes))

        return and_(*condition)

    @staticmethod
    def builder():
        return CompanyInfoFilterConditionBuilder()


class CompanyInfoFilterConditionBuilder(Builder):
    def __init__(self):
        self.object = CompanyInfoFilterCondition()

    def set_market_type(self, value):
        self.object.market_type = value
        return self

    def set_code(self, value):
        self.object.code = value
        return self

    def set_codes(self, value):
        self.object.codes = value
        return self

    def build(self):
        return self.object
