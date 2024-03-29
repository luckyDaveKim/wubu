from datetime import datetime

from sqlalchemy import and_

from src.common.models.builder import Builder
from src.common.models.filter_condition import FilterCondition
from src.company.models.daily_price import DailyPrice

DATE_FORMAT = '%Y-%m-%d'


class DailyPriceFilterCondition(FilterCondition):
    def __init__(self):
        self.code = None
        self.start_date = None
        self.end_date = None

    def get_filter(self):
        condition = []

        if self.code:
            condition.append(DailyPrice.code == self.code)
        print(self.start_date)
        if self.start_date or self.end_date:
            try:
                if self.start_date and self.end_date:
                    condition.append(
                        and_(
                            DailyPrice.date >= datetime.strptime(self.start_date, DATE_FORMAT),
                            DailyPrice.date <= datetime.strptime(self.end_date, DATE_FORMAT)
                        )
                    )
                elif self.start_date:
                    condition.append(
                        DailyPrice.date >= datetime.strptime(self.start_date, DATE_FORMAT),
                    )
                elif self.end_date:
                    condition.append(
                        DailyPrice.date <= datetime.strptime(self.end_date, DATE_FORMAT)
                    )
            except Exception as e:
                print('start_date, end_date 파싱 오류!!!', e)

        return and_(*condition)

    @staticmethod
    def builder():
        return DailyPriceFilterConditionBuilder()


class DailyPriceFilterConditionBuilder(Builder):
    def __init__(self):
        self.object = DailyPriceFilterCondition()

    def set_code(self, value):
        self.object.code = value
        return self

    def set_start_date(self, value):
        self.object.start_date = value
        return self

    def set_end_date(self, value):
        self.object.end_date = value
        return self

    def build(self):
        return self.object
