from fastapi import APIRouter
from sqlalchemy.orm import Session

def get_session():
	session = Session()
	try:
		yield session  # pause and returns the session value
	finally:
		session.close()  # once the session is finished, the session is closed

router = APIRouter()

@router.get("/teams/{team_id}")
def get_team_by_id(team_id: int):
    pass