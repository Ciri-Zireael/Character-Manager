from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base

# Define the models
Base = declarative_base()
engine = create_engine("sqlite:///C:\\Users\ewaja\OneDrive\\University\IV semester\PPY\DnD_character_manager\Database\DnD_database.db")
connection = engine.connect()

class Campaign(Base):
    __tablename__ = 'Campaign'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Description = Column(String(200), nullable=False)
    Start_date = Column(Date, nullable=False)
    End_date = Column(Date)


class Character(Base):
    __tablename__ = 'Character'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Surname = Column(String(100))
    Level = Column(Integer, nullable=False)
    Race = Column(String(50), nullable=False)
    Class = Column(String(50), nullable=False)


class CharacterCampaign(Base):
    __tablename__ = 'Character_Campaign'

    Character_Id = Column(Integer, ForeignKey('Character.Id'), primary_key=True)
    Campaign_Id = Column(Integer, ForeignKey('Campaign.Id'), primary_key=True)


class CharacterData(Base):
    __tablename__ = 'Character_Data'

    Character_Id = Column(Integer, ForeignKey('Character.Id'), primary_key=True)
    Proficiency_bonus = Column(Integer, nullable=False)
    Strength = Column(Integer, nullable=False)
    Dexterity = Column(Integer, nullable=False)
    Constitution = Column(Integer, nullable=False)
    Intelligence = Column(Integer, nullable=False)
    Wisdom = Column(Integer, nullable=False)
    Charisma = Column(Integer, nullable=False)


class Item(Base):
    __tablename__ = 'Item'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Description = Column(String(200), nullable=False)


class Spell(Base):
    __tablename__ = 'Spell'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Description = Column(String(200), nullable=False)
    Level = Column(Integer, nullable=False)


class CharacterItems(Base):
    __tablename__ = 'Character_Items'

    Character_Id = Column(Integer, ForeignKey('Character.Id'), primary_key=True)
    Item_Id = Column(Integer, ForeignKey('Item.Id'), primary_key=True)


class CharacterSpells(Base):
    __tablename__ = 'Character_Spells'

    Character_Id = Column(Integer, ForeignKey('Character.Id'), primary_key=True)
    Spell_Id = Column(Integer, ForeignKey('Spell.Id'), primary_key=True)

Base.metadata.create_all(engine)
def get_base():
    return Base