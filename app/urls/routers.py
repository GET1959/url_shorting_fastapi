from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.urls.service import create_short_url, get_db, get_short_url_by_id

router = APIRouter(prefix="/urls")


@router.post(
    path="/shorten",
    tags=["Urls shorting"],
    status_code=status.HTTP_201_CREATED,
    summary="Create shortened url"
)
async def create_short(
        original_url: str,
        db: AsyncSession = Depends(get_db)
):
    result = await create_short_url(original_url, db)
    return result


@router.get(
    path="/{shorten-url-id}",
    status_code=307,
    tags=["Urls shorting"],
    summary="Redirect to original url by id"
)
async def redirect_to_original_by_id(
    short_id: str,
    db: AsyncSession = Depends(get_db)
):
    url = await get_short_url_by_id(db, short_id)
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")

    origin_url = str(url.original_url)
    if not origin_url:
        raise HTTPException(status_code=404, detail="Shortened URL not found")

    response = RedirectResponse(
        url=origin_url,
        status_code=307
    )
    response.headers["Location"] = origin_url
    return response.headers["Location"]
