from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.company.models.product import Product
from src.config import config


async def init_mongodb():
    mongodb = config.database['mongodb']

    client = AsyncIOMotorClient(
        f'mongodb://{mongodb['user']}:{mongodb['password']}@{mongodb['host']}:{mongodb['port']}'
    )

    await init_beanie(
        database=client[mongodb['db']],
        document_models=[Product]
    )
