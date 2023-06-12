from pydantic import BaseModel, Field

from database.model_definition import Campaign, Item, Spell


class OrmBase(BaseModel):
    class Config:
        orm_mode: True


class CharacterSchema(OrmBase):
    Name: str = Field(max_length=50)
    Surname: str = Field(max_length=100)
    Level: int = Field(le=20)
    Race: str = Field(max_length=50)
    Class: str = Field(max_length=50)


class CharacterDataSchema(OrmBase):
    Proficiency_bonus: int = Field(le=12)
    Strength: int = Field(le=30)
    Dexterity: int = Field(le=30)
    Constitution: int = Field(le=30)
    Intelligence: int = Field(le=30)
    Wisdom: int = Field(le=30)
    Charisma: int = Field(le=30)


class CharacterUpdateSchema(OrmBase):
    Level: int = Field(le=20)
    Proficiency_bonus: int = Field(le=30)
    Strength: int = Field(le=30)
    Dexterity: int = Field(le=30)
    Constitution: int = Field(le=30)
    Intelligence: int = Field(le=30)
    Wisdom: int = Field(le=30)
    Charisma: int = Field(le=30)


class CharacterDetailsSchema:
    Name: str = Field(max_length=50)
    Surname: str = Field(max_length=100)
    Level: int = Field(le=20)
    Class: str = Field(max_length=50)
    Race: str = Field(max_length=50)
    Campaigns: list[Campaign]
    Stats: dict
    Items: list[Item]
    Spells: list[Spell]


class CampaignSchema(OrmBase):
    Name: str = Field(max_length=50)
    Description: str = Field(max_length=200)


class ItemSchema(OrmBase):
    Name: str = Field(max_length=50)
    Description: str = Field(max_length=200)


class SpellSchema(OrmBase):
    Name: str = Field(max_length=50)
    Description: str = Field(max_length=200)
    Level: int = Field(le=9)
