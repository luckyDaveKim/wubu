import pandas as pd
from sqlalchemy import Column, String, VARCHAR, Date

from src.database.mysql import Base


class CompanyInfo(Base):
    __tablename__ = 'company_info'

    code = Column(String(6), primary_key=True)
    company = Column(String(40))
    market_type = Column(String(20))
    last_update = Column(Date)

    @staticmethod
    def convert_to_dataframe(company_info_list):
        data = [(company_info.code, company_info.company, company_info.market_type, company_info.last_update) for
                company_info in company_info_list]

        return pd.DataFrame(data, columns=["code", "company", "market_type", "last_update"])
