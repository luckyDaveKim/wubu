from typing import List

import pandas as pd

from src.common.models.filter_condition import FilterCondition
from src.common.utils import dataframe2json
from src.company.model.company_info import CompanyInfo
from src.company.model.dailyPriceStrategy import StrategyExecutorFactory
from src.company.model.daily_price import DailyPrice
from src.database.mysql import Session, engine


async def get_companies(condition: FilterCondition):
    session = Session()

    return session.query(CompanyInfo).filter(condition.get_filter()).order_by("company").all()


async def get_company_daily_prices(condition: FilterCondition):
    session = Session()

    return session.query(DailyPrice).filter(condition.get_filter()).order_by("date").all()
