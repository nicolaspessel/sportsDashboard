from pydantic import BaseModel, ConfigDict

class TeamBase(BaseModel):
    name: str
    abbreviation: str
    is_active: bool
    region: str


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


class TeamCreate(TeamBase):
    titles: int = 0


class TeamResponse(TeamBase):
    titles: int
    id: int
    stadium: StadiumResponse | None = None  # nested Pydantic models
    
    model_config = ConfigDict(from_attributes=True)  


class TeamUpdate(BaseModel):
    name: str | None = None  # creates an optional attribute, sets null by default and can be omitted
    abbreviation: str | None = None
    is_active: bool | None = None    
    region: str | None = None
    titles: int | None = None