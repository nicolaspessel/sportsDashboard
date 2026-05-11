from pydantic import BaseModel, ConfigDict

class StadiumBase(BaseModel):
    name: str
    location: str


class StadiumCreate(StadiumBase):
    team_id: int


class StadiumResponse(StadiumBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  # allows Pydantic to read ORM attributes


class StadiumUpdate(BaseModel):
    name: str | None = None
    location: str | None = None