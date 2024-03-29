from datetime import datetime
from typing import Optional

from beanie import Document


class BaseDocument(Document):
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    modified_at: Optional[datetime] = None
    modified_by: Optional[str] = None

    async def insert(self):
        now = datetime.now()
        self.created_at = now
        self.modified_at = now
        return await super().insert()

    async def update(self):
        now = datetime.now()
        self.modified_at = now
        return await super().update()
