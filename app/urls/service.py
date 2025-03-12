import uuid

from fastapi import HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session_maker
from app.urls.models import ShortURL


async def get_db():
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()


async def get_short_url_by_id(
        session: AsyncSession,
        short_url_id: str,
) -> ShortURL:

    query = select(ShortURL).where(ShortURL.id == short_url_id)

    result = (await session.execute(query)).scalars().first()

    if not result:
        raise HTTPException(status_code=404, detail="Объект не найден")

    return result


async def create_short_url(
        original_url: str,
        db: AsyncSession = Depends(get_db)
):
    short_code = str(uuid.uuid4())[:6]
    short_url_instance = ShortURL(
        original_url=original_url,
        short_url=f"http://127.0.0.1:8080/{short_code}"
    )
    db.add(short_url_instance)
    await db.commit()
    await db.refresh(short_url_instance)
    return {
        "original_url": original_url,
        "shortened_url": short_url_instance
    }
