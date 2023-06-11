from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from Database.model_definition import Character, CharacterData, CharacterCampaign, Campaign, CharacterItems, \
    CharacterSpells, Spell, Item
from data.schema_definition import CharacterSchema, CharacterDataSchema, CharacterDetailsSchema


DB_PATH = "sqlite:///C:\\Users\ewaja\OneDrive\\University\IV semester\PPY\Character-Manager\Database\DnD_database.db"


class Database:
    engine: Engine
    session: Session

    def __init__(self):
        self.engine = create_engine(
            DB_PATH,
            connect_args={"check_same_thread": False})
        connection = self.engine.connect()

        session_local = sessionmaker(bind=self.engine)
        self.session = session_local()

    def get_characters(self):
        characters = self.session.query(Character).all()
        return characters

    def get_character_details_by_id(self, character_id):
        character = self.session.query(Character).filter_by(Id=character_id).first()
        details = CharacterDetailsSchema()

        details.Name = character.Name
        details.Surname = character.Surname
        details.Level = character.Level
        details.Class = character.Class
        details.Race = character.Race

        details.Campaigns = []
        char_camp = self.session.query(CharacterCampaign).filter_by(Character_Id=character_id).all()
        for cc in char_camp:
            details.Campaigns.append(self.session.query(Campaign).filter_by(Id=cc.Campaign_Id).first())
        char_it = self.session.query(CharacterItems).filter_by(Character_Id=character_id).all()

        stats = self.session.query(CharacterData).filter_by(Character_Id=character_id).first()
        details.Stats = {"Proficiency bonus": stats.Proficiency_bonus, "Strength": stats.Strength,
                         "Dexterity": stats.Dexterity, "Constitution": stats.Constitution,
                         "Intelligence": stats.Intelligence, "Wisdom": stats.Wisdom, "Charisma": stats.Charisma}

        details.Items = []
        for ci in char_it:
            details.Items.append(self.session.query(Item).filter_by(Id=ci.Item_Id).first())
        char_sp = self.session.query(CharacterSpells).filter_by(Character_Id=character_id).all()

        details.Spells = []
        for cs in char_sp:
            details.Spells.append(self.session.query(Spell).filter_by(Id=cs.Spell_Id).first())
        return details

    def add_character(self, character: CharacterSchema, character_data: CharacterDataSchema):
        char = Character(**character.dict())
        # Character(Name=character.Name, Surname=character.Surname, Level=character.Level, Race=character.Race, Class=character.Class)
        self.session.add(char)
        self.session.commit()

        char_data = CharacterData(**character_data.dict())
        char_data.Character_Id = char.Id

        self.session.add(char_data)
        self.session.commit()

    def update_character_by_id(self, character_data_update: CharacterDataSchema, character_id):
        char_data = self.session.query(CharacterData).filter_by(id=character_id).first()
        char_data.Proficiency_bonus = character_data_update.Proficiency_bonus
        char_data.Strength = character_data_update.Strength
        char_data.Dexterity = character_data_update.Dexterity
        char_data.Constitution = character_data_update.Constitution
        char_data.Intelligence = character_data_update.Intelligence
        char_data.Wisdom = character_data_update.Wisdom
        char_data.Charisma = character_data_update.Charisma
        self.session.commit()

    def delete_character(self, character_id: int):
        character = self.session.query(Character).filter_by(id=character_id).first()

        self.session.delete(character)
        self.session.commit()

    def close(self):
        self.engine.dispose()
        self.session.close()
