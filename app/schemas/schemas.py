from pydantic import BaseModel, ConfigDict

class TeamBase(BaseModel):
    name: str
    region: str

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  # allows Pydantic to read ORM attributes