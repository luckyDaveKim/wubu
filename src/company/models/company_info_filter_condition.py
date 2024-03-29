from sqlalchemy import and_

from src.common.models.builder import Builder
from src.common.models.filter_condition import FilterCondition
from src.company.models.company_info import CompanyInfo


class CompanyInfoFilterCondition(FilterCondition):
    def __init__(self):
        self.market_type = None

    def get_filter(self):
        condition = []

        if self.market_type:
            condition.append(CompanyInfo.market_type == self.market_type)

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

    def build(self):
        return self.object
