from pydantic import BaseModel, ConfigDict

class AthleteBase(BaseModel):
    full_name: str
    position: str
    age: int
    weight: int
    height: int
    jersey_num: int | None = None
    debut: int | None = None


class AthleteCreate(AthleteBase):
    pass


class AthleteResponse(AthleteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)