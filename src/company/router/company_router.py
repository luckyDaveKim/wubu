import json
from typing import List, Optional

import pandas as pd
from fastapi import APIRouter
from fastapi.params import Query
from sqlalchemy import exists, and_

from src.common.utils import dataframe2json
from src.company.model.company_info import CompanyInfo
from src.company.model.company_info_filter_condition import CompanyInfoFilterCondition
from src.company.model.dailyPriceStrategy import StrategyExecutorFactory
from src.company.model.daily_price import DailyPrice
from src.company.model.daily_price_filter_condition import DailyPriceFilterCondition
from src.database.mysql import Session, engine
from src.company.service import company_service

router = APIRouter()


@router.get("/api/companies/")
async def get_companies():
    condition = CompanyInfoFilterCondition.builder().set_market_type('KOSPI').build()
    companies = await company_service.get_companies(condition)
    dataframe = CompanyInfo.convert_to_dataframe(companies)

    return dataframe2json(dataframe)


@router.get("/api/companies/{code}/daily/price")
# TODO : parameter model 로 받기
async def get_companies_daily_price(code: str,
                                    start_date: Optional[str] = Query(None), end_date: Optional[str] = Query(None),
                                    strategy_names: Optional[List[str]] = Query(None)):
    if strategy_names is None:
        strategy_names = []

    condition = (DailyPriceFilterCondition
                 .builder()
                 .set_code(code)
                 .set_start_date(start_date)
                 .set_end_date(end_date)
                 .build())

    daily_price_list = await company_service.get_company_daily_prices(condition)
    dataframe = DailyPrice.convert_to_dataframe(daily_price_list)
    calculated_dataframe = StrategyExecutorFactory(dataframe).execute_all(strategy_names)
    return dataframe2json(calculated_dataframe)
