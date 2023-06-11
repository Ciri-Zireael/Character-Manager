from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Database.model_definition import get_base, Campaign, Character, CharacterCampaign, CharacterData, Spell, \
    CharacterSpells, CharacterItems, Item

engine = create_engine('sqlite:///DnD_database.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = get_base()
# Create the tables based on the defined models
Base.metadata.create_all(engine)

# Check if Campaign table has data
if session.query(Campaign).count() == 0:
    # Insert sample data into the Campaign table
    campaigns = [
        Campaign(Id=1, Name='The Lost City of Eldoria',
                 Description='Embark on an epic quest to discover the hidden ruins of Eldoria, a mythical city rumored to '
                             'hold ancient treasures and powerful artifacts. Encounter dangerous creatures, '
                             'solve intricate puzzles, and unravel the secrets of this long-forgotten civilization.',
                 Start_date=date(2023, 1, 1), End_date=None),
        Campaign(Id=2, Name='Shadows of the Darkwood',
                 Description='Venture into the mysterious Darkwood, a dense forest shrouded in darkness and home to '
                             'malevolent forces. As brave adventurers, you must confront the ancient evil lurking within, '
                             'battling monstrous creatures, facing ethereal nightmares, and ultimately restoring light to '
                             'the land.',
                 Start_date=date(2023, 2, 1), End_date=date(2023, 3, 1)),
        Campaign(Id=3, Name='Rise of the Dragonlords',
                 Description='A great prophecy foretells the return of mighty dragonlords who will shape the destiny of '
                             'the realm. Join a faction of dragon riders, master the arcane arts, and navigate political '
                             'intrigue as you compete for power, facing fierce dragon battles and making pivotal choices '
                             'that determine the fate of kingdoms.',
                 Start_date=date(2023, 3, 1), End_date=None),
        Campaign(Id=4, Name='The Cursed Seas',
                 Description='Set sail on a perilous voyage across treacherous waters infested with ghost ships, '
                             'sea monsters, and vengeful spirits. Seek the source of a powerful curse that plagues the '
                             'seas, battling fierce storms, uncovering ancient maritime lore, and ultimately freeing the '
                             'ocean from its haunted grip.',
                 Start_date=date(2023, 4, 1), End_date=None),
        Campaign(Id=5, Name='City of Thieves',
                 Description='In the lawless metropolis of Storvale, crime syndicates reign supreme, and corruption runs '
                             'deep. Join a band of renegade outlaws and navigate the criminal underworld, '
                             'planning heists, engaging in intense urban combat, and outsmarting powerful crime lords to '
                             'become the rulers of the city.',
                 Start_date=date(2023, 5, 1), End_date=None)
    ]
    session.add_all(campaigns)

# Check if Character table has data
if session.query(Character).count() == 0:
    # Insert sample data into the Character table
    characters = [
        Character(Id=1, Name='Aveline', Surname='Stormrider', Level=5, Race='Human', Class='Rogue'),
        Character(Id=2, Name='Thaddeus', Surname='Blackthorn', Level=8, Race='Dwarf', Class='Fighter'),
        Character(Id=3, Name='Seraphina', Surname='Nightshade', Level=3, Race='Elf', Class='Wizard'),
        Character(Id=4, Name='Ragnar', Surname='Thunderaxe', Level=6, Race='Half-Orc', Class='Barbarian'),
        Character(Id=5, Name='Isabella', Surname='Winterwind', Level=4, Race='Tiefling', Class='Sorcerer'),
        Character(Id=6, Name='Orion', Surname='Silverleaf', Level=7, Race='Half-Elf', Class='Ranger'),
        Character(Id=7, Name='Elara', Surname='Brightblade', Level=2, Race='Dragonborn', Class='Paladin'),
        Character(Id=8, Name='Kaelin', Surname='Swiftwind', Level=9, Race='Wood Elf', Class='Druid'),
        Character(Id=9, Name='Lucas', Surname='Stormwind', Level=5, Race='Halfling', Class='Bard'),
        Character(Id=10, Name='Valeria', Surname='Frostwind', Level=6, Race='High Elf', Class='Cleric')
    ]
    session.add_all(characters)

# Check if Character_Campaign table has data
if session.query(CharacterCampaign).count() == 0:
    # Insert sample data into the Character_Campaign table
    character_campaigns = [
        CharacterCampaign(Character_Id=1, Campaign_Id=1),
        CharacterCampaign(Character_Id=2, Campaign_Id=1),
        CharacterCampaign(Character_Id=2, Campaign_Id=2),
        CharacterCampaign(Character_Id=3, Campaign_Id=3),
        CharacterCampaign(Character_Id=4, Campaign_Id=2),
        CharacterCampaign(Character_Id=4, Campaign_Id=3),
        CharacterCampaign(Character_Id=5, Campaign_Id=4),
        CharacterCampaign(Character_Id=6, Campaign_Id=5),
        CharacterCampaign(Character_Id=7, Campaign_Id=4),
        CharacterCampaign(Character_Id=7, Campaign_Id=3),
        CharacterCampaign(Character_Id=8, Campaign_Id=2),
        CharacterCampaign(Character_Id=9, Campaign_Id=2),
        CharacterCampaign(Character_Id=10, Campaign_Id=1),
        CharacterCampaign(Character_Id=10, Campaign_Id=5)
    ]
    session.add_all(character_campaigns)

# Check if Character_Data table has data
if session.query(CharacterData).count() == 0:
    # Insert sample data into the Character_Data table
    character_data = [
        CharacterData(Character_Id=1, Proficiency_bonus=2, Strength=10, Dexterity=12, Constitution=14, Intelligence=8, Wisdom=16, Charisma=18),
        CharacterData(Character_Id=2, Proficiency_bonus=4, Strength=16, Dexterity=14, Constitution=12, Intelligence=10, Wisdom=8, Charisma=6),
        CharacterData(Character_Id=3, Proficiency_bonus=3, Strength=8, Dexterity=10, Constitution=12, Intelligence=14, Wisdom=16, Charisma=18),
        CharacterData(Character_Id=4, Proficiency_bonus=5, Strength=18, Dexterity=16, Constitution=14, Intelligence=12, Wisdom=10, Charisma=8),
        CharacterData(Character_Id=5, Proficiency_bonus=2, Strength=12, Dexterity=14, Constitution=16, Intelligence=18, Wisdom=8, Charisma=10),
        CharacterData(Character_Id=6, Proficiency_bonus=4, Strength=14, Dexterity=16, Constitution=18, Intelligence=10, Wisdom=8, Charisma=12),
        CharacterData(Character_Id=7, Proficiency_bonus=3, Strength=8, Dexterity=10, Constitution=12, Intelligence=14, Wisdom=16, Charisma=18),
        CharacterData(Character_Id=8, Proficiency_bonus=5, Strength=16, Dexterity=18, Constitution=14, Intelligence=12, Wisdom=10, Charisma=8),
        CharacterData(Character_Id=9, Proficiency_bonus=2, Strength=10, Dexterity=12, Constitution=14, Intelligence=16, Wisdom=18, Charisma=8),
        CharacterData(Character_Id=10, Proficiency_bonus=4, Strength=12, Dexterity=14, Constitution=16, Intelligence=18, Wisdom=8, Charisma=10)
    ]
    session.add_all(character_data)

# Check if Item table has data
if session.query(Item).count() == 0:
    # Insert sample data into the Item table
    items = [
        Item(Id=1, Name='Sword of Truth', Description='A legendary sword that glows with divine light.'),
        Item(Id=2, Name='Cloak of Invisibility', Description='A magical cloak that grants invisibility to the wearer.')
    ]
    session.add_all(items)

# Check if Spell table has data
if session.query(Spell).count() == 0:
    # Insert sample data into the Spell table
    spells = [
        Spell(Id=1, Name='Fireball', Description='Unleashes a powerful ball of fire.', Level=3),
        Spell(Id=2, Name='Healing Touch', Description='Restores health to the target.', Level=2)
    ]
    session.add_all(spells)

# Check if Character_Spells table has data
if session.query(CharacterSpells).count() == 0:
    character_spells = [
        CharacterSpells(Character_Id=3, Spell_Id=1),
        CharacterSpells(Character_Id=3, Spell_Id=2)
    ]
    session.add_all(character_spells)

# Check if Character_Items table has data
if session.query(CharacterItems).count() == 0:
    character_items = [
        CharacterItems(Character_Id=1, Item_Id=1),
        CharacterItems(Character_Id=1, Item_Id=2)
    ]
    session.add_all(character_items)

# Commit the changes
session.commit()

# Close the session
session.close()
