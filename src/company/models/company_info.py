from sqlalchemy import Column, String, VARCHAR, Date

from src.database.mysql import Base


class CompanyInfo(Base):
    __tablename__ = 'company_info'

    code = Column(String(6), primary_key=True)
    company = Column(String(40))
    market_type = Column(String(20))
    last_update = Column(Date)
