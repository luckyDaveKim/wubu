from typing import Union, Optional

from beanie import init_beanie, Document, Indexed
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from src.company.model.company_info import CompanyInfo
from src.company.model.daily_price import DailyPrice
from src.company.model.product import Category, Product
from src.analysis.router import analysis_router
from src.company.router import company_router
from src.database.mongodb import init_mongodb
from src.database.mysql import Session

app = FastAPI()
app.include_router(analysis_router.router)
app.include_router(company_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.on_event('startup')
async def start_db():
    await init_mongodb()


@app.get("/")
async def read_root():
    # chocolate = Category(name="Chocolate", description="A preparation of roasted and ground cacao seeds.")
    # # Beanie documents work just like pydantic models
    # tonybar = Product(name="Tony's", price=5.95, category=chocolate)
    # # And can be inserted into the database
    # await tonybar.insert()
    #
    # # You can find documents with pythonic syntax
    # products = Product.find_many(Product.price < 10)
    # async for result in products:
    #     print(result)

    # And update them
    # await product.set({Product.name: "Gold bar"})

    # session = Session()
    # companies = session.query(CompanyInfo).all()
    # for company in companies:
    #     print(company.company)

    # session = Session()
    # companies = session.query(DailyPrice).filter(DailyPrice.code == '035420').all()
    # for company in companies:
    #     print(company)
    return {'a': 'product'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
