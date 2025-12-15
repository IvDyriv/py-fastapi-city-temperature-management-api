from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud

router = APIRouter(prefix="/temperatures", tags=["Temperatures"])


@router.get("", response_model=list[schemas.TemperatureRead])
def get_temperatures(
    city_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    return crud.list_temperatures(db, city_id=city_id)
