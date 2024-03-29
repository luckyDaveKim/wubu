import pandas as pd
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

    @staticmethod
    def convert_to_dataframe(daily_price_list):
        data = [(daily_price.code, daily_price.date, daily_price.open, daily_price.high, daily_price.low,
                 daily_price.close, daily_price.diff, daily_price.volume) for daily_price in daily_price_list]

        return pd.DataFrame(data, columns=["code", "date", "open", "high", "low", "close", "diff", "volume"])
