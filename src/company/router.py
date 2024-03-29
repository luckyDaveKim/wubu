import json
from typing import List

import pandas as pd
from fastapi import APIRouter
from sqlalchemy import exists, and_

from src.common.utils import dataframe2json
from src.company.models.company_info import CompanyInfo
from src.company.models.company_info_filter_condition import CompanyInfoFilterCondition
from src.company.models.dailyPriceStrategy import StrategyExecutorFactory
from src.company.models.daily_price import DailyPrice
from src.company.models.daily_price_filter_condition import DailyPriceFilterCondition
from src.database.mysql import Session, engine

router = APIRouter(prefix="/api/companies")


@router.get("/")
async def get_companies():
    condition = CompanyInfoFilterCondition.builder().set_market_type('KOSPI').build()

    session = Session()
    return session.query(CompanyInfo).filter(condition.get_filter()).order_by("company").all()


@router.get("/{code}/price/daily")
# TODO : parameter model 로 받기
async def get_companies(code: str, start_date: str | None = None, end_date: str | None = None,
                        strategy_names: List[str] | None = None):
    if strategy_names is None:
        strategy_names = []

    condition = (DailyPriceFilterCondition
                 .builder()
                 .set_code(code)
                 .set_start_date(start_date)
                 .set_end_date(end_date)
                 .build())

    session = Session()
    dataframe = pd.read_sql_query(
        sql=session.query(DailyPrice).filter(condition.get_filter()).order_by("date").statement,
        con=engine
    )

    df = StrategyExecutorFactory(dataframe).execute_all(strategy_names)
    return dataframe2json(df)
