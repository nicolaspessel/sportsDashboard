from pydantic import BaseModel, ConfigDict

class TeamBase(BaseModel):
    name: str
    region: str

class TeamCreate(TeamBase):
    titles: int = 0

class TeamResponse(TeamBase):
    titles: int
    id: int

    model_config = ConfigDict(from_attributes=True)  # allows Pydantic to read ORM attributes

class TeamUpdate(BaseModel):
    name: str | None = None  # creates an optional attribute, sets null by default and can be omitted
    region: str | None = None
    titles: int | None = None