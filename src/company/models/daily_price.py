from sqlalchemy import String, VARCHAR, Column, Date, BigInteger

from src.database.mysql import Base


class DailyPrice(Base):
    __tablename__ = 'daily_price'

    code = Column(String(6), primary_key=True)
    date = Column(Date, primary_key=True)
    open = Column(BigInteger)
    high = Column(BigInteger)
    low = Column(BigInteger)
    close = Column(BigInteger)
    diff = Column(BigInteger)
    volume = Column(BigInteger)
