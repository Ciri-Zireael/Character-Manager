from pydantic import BaseModel, Field

from database.model_definition import Campaign, Item, Spell


class OrmBase(BaseModel):
    class Config:
        orm_mode: True


class CharacterSchema(OrmBase):
    Name: str = Field(max_length=30)
    Surname: str
    Level: int
    Race: str
    Class: str


class CharacterDataSchema(OrmBase):
    Proficiency_bonus: int
    Strength: int
    Dexterity: int
    Constitution: int
    Intelligence: int
    Wisdom: int
    Charisma: int = Field(le=20)


class CharacterDetailsSchema:
    Name: str
    Surname: str
    Level: int
    Class: str
    Race: str
    Campaigns: list[Campaign]
    Stats: dict
    Items: list[Item]
    Spells: list[Spell]


class CampaignSchema:
    Name: str
    Description: str
