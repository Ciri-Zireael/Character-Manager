import functools
import tkinter as tk
from tkinter import ttk, messagebox

from data.schema_definition import CharacterUpdateSchema
from gui.add_existing_campaign_window import AddExistingCampaignWindow
from gui.add_existing_item_window import AddExistingItemWindow
from gui.add_existing_spell_window import AddExistingSpellWindow


def show_campaign_details(campaign):
    """
    Displays the details of a campaign in a messagebox.

    Args:
        campaign: The campaign object containing the details to display.
    """
    message = f"Campaign Name: {campaign.Name}\n\nDescription: {campaign.Description}"
    messagebox.showinfo("Campaign Details", message)


def show_item_details(item):
    """
    Displays the details of an item in a messagebox.

    Args:
        item (Item): The item object containing the details to display.
    """
    message = f"Item Name: {item.Name}\n\nDescription: {item.Description}"
    messagebox.showinfo("Item Details", message)


def show_spell_details(spell):
    """
    Displays the details of a spell in a messagebox.

    Args:
        spell (Spell): The spell object containing the details to display.
    """
    message = f"Spell Name: {spell.Name}    lv.{spell.Level}\n\nDescription: {spell.Description}"
    messagebox.showinfo("Spell Details", message)


class CharacterDetailsWindow(tk.Toplevel):
    """
    A window for displaying and editing character details.
    """
    def __init__(self, parent, character_id, database):
        """
        Initialize the main window.

        Args:
            parent: The parent window.
            character_id: The ID of the character to display details for.
            database: The database object for accessing character data.
        """
        super().__init__(parent)

        self.character_details = database.get_character_details_by_id(character_id)
        self.character_id = character_id
        self.database = database
        self.parent = parent

        self.title(f"{self.character_details.Name} {self.character_details.Surname} - Details")

        self.view_labels = []
        self.edit_labels = []
        self.view_values = []
        self.edit_values = []

        self.edit_mode = True

        self.fill_fields()

    def change_mode(self):
        """
        Toggles between view mode and edit mode for the character details.
        """
        self.edit_mode = not self.edit_mode

        if self.edit_mode:
            for label, value in zip(self.view_labels, self.view_values):
                label.grid_remove()
                value.grid_remove()
            for label, value in zip(self.edit_labels, self.edit_values):
                label.grid()
                value.grid()

        else:
            for label, value in zip(self.edit_labels, self.edit_values):
                label.grid_remove()
                value.grid_remove()
            for label, value in zip(self.view_labels, self.view_values):
                label.grid()
                value.grid()

    def edit(self):
        """
        Updates the character details with the edited values.
        """
        character_update = CharacterUpdateSchema(
            Level=self.edit_values[1].get(),
            Proficiency_bonus=self.edit_values[3].get(),
            Strength=self.edit_values[4].get(),
            Dexterity=self.edit_values[5].get(),
            Constitution=self.edit_values[6].get(),
            Intelligence=self.edit_values[7].get(),
            Wisdom=self.edit_values[8].get(),
            Charisma=self.edit_values[9].get()
        )
        self.database.update_character_by_id(character_update, self.character_id)
        self.refresh()

    def delete_character(self):
        """
        Deletes the character from the database.
        """
        self.database.delete_character(self.character_id)
        messagebox.showinfo("Success", "Character removed successfully!")
        self.parent.refresh()
        self.destroy()

    def remove_spell(self, spell_id, character_id):
        """
        Removes a spell from the character's spell list.

        Args:
            spell_id: The ID of the spell to remove.
            character_id: The ID of the character.
        """
        self.database.remove_spell(character_id, spell_id)
        messagebox.showinfo("Success", "Campaign removed successfully!")
        self.refresh()

    def open_add_spell_window(self):
        """
        Opens the window to add an existing spell to the character's spell list.
        """
        new_spell_window = AddExistingSpellWindow(self, self.database)

    def remove_item(self, item_id, character_id):
        """
        Removes an item from the character's item list.

        Args:
            item_id: The ID of the item to remove.
            character_id: The ID of the character.
        """
        self.database.remove_item(character_id, item_id)
        messagebox.showinfo("Success", "Item removed successfully!")
        self.refresh()

    def open_add_item_window(self):
        """
        Opens the window to add an existing item to the character's item list.
        """
        new_item_window = AddExistingItemWindow(self, self.database)

    def remove_campaign(self, campaign_id, character_id):
        """
        Removes a campaign from the character's campaign list.

        Args:
            campaign_id: The ID of the campaign to remove.
            character_id: The ID of the character.
        """
        self.database.remove_campaign(character_id, campaign_id)
        messagebox.showinfo("Success", "Campaign removed successfully!")
        self.refresh()

    def open_add_campaign_window(self):
        """
        Opens the window to add an existing campaign to the character's campaign list.
        """
        new_campaign_widow = AddExistingCampaignWindow(self, self.database)

    def refresh(self):
        """
        Refreshes the character details window with the latest data.
        """
        self.character_details = self.database.get_character_details_by_id(self.character_id)

        for label, value in zip(self.edit_labels, self.edit_values):
            label.grid_remove()
            value.grid_remove()
        for label, value in zip(self.view_labels, self.view_values):
            label.grid_remove()
            value.grid_remove()

        self.view_labels.clear()
        self.edit_labels.clear()
        self.view_values.clear()
        self.edit_values.clear()

        self.fill_fields()

    def fill_fields(self):
        """
        Populates the character details fields in the window.
        """
        # ----------------- VIEW MODE ----------------------------------------------------------------------------------
        # Name
        name_label = ttk.Label(self, text="Name:")
        self.view_labels.append(name_label)
        name_value = ttk.Label(self, text=self.character_details.Name)
        self.view_values.append(name_value)

        # Surname
        surname_label = ttk.Label(self, text="Surname:")
        self.view_labels.append(surname_label)
        surname_value = ttk.Label(self, text=self.character_details.Surname)
        self.view_values.append(surname_value)

        # Level
        level_label = ttk.Label(self, text="Level:")
        self.view_labels.append(level_label)
        level_value = ttk.Label(self, text=self.character_details.Level)
        self.view_values.append(level_value)

        # Class
        class_label = ttk.Label(self, text="Class:")
        self.view_labels.append(class_label)
        class_value = ttk.Label(self, text=self.character_details.Class)
        self.view_values.append(class_value)

        # Race
        race_label = ttk.Label(self, text="Race:")
        self.view_labels.append(race_label)
        race_value = ttk.Label(self, text=self.character_details.Race)
        self.view_values.append(race_value)

        # Stats
        stats_label = ttk.Label(self, text="Stats:")
        self.view_labels.append(stats_label)
        stats_label = ttk.Label(self, text="")
        self.view_values.append(stats_label)

        for stat in self.character_details.Stats:
            label = ttk.Label(self, text='    ' + stat + ':')
            self.view_labels.append(label)
            value = ttk.Label(self, text=self.character_details.Stats.get(stat))
            self.view_values.append(value)

        # Items
        items_label = ttk.Label(self, text="Items:")
        self.view_labels.append(items_label)
        items_label = ttk.Label(self, text="")
        self.view_values.append(items_label)

        for item in self.character_details.Items:
            label = ttk.Label(self, text='    ' + item.Name)
            self.view_labels.append(label)
            details_button = ttk.Button(self, text="See Details", command=lambda it=item: show_item_details(it))
            self.view_values.append(details_button)

        # Spells
        spells_label = ttk.Label(self, text="Spells:")
        self.view_labels.append(spells_label)
        spells_label = ttk.Label(self, text="")
        self.view_values.append(spells_label)

        for spell in self.character_details.Spells:
            label = ttk.Label(self, text='    ' + spell.Name)
            self.view_labels.append(label)
            details_button = ttk.Button(self, text="See Details", command=lambda s=spell: show_spell_details(s))
            self.view_values.append(details_button)

        # Campaigns
        campaigns_label = ttk.Label(self, text="Campaigns:")
        self.view_labels.append(campaigns_label)
        campaigns_label = ttk.Label(self, text="")
        self.view_values.append(campaigns_label)

        for campaign in self.character_details.Campaigns:
            label = ttk.Label(self, text='    ' + campaign.Name)
            self.view_labels.append(label)
            details_button = ttk.Button(self, text="See Details", command=lambda c=campaign: show_campaign_details(c))
            self.view_values.append(details_button)

        # ----------------- EDIT MODE ----------------------------------------------------------------------------------
        # Full name
        full_name_label = ttk.Label(self, text=self.character_details.Name + ' ' + self.character_details.Surname)
        self.edit_labels.append(full_name_label)
        empty_label = ttk.Label(self, text='')
        self.edit_values.append(empty_label)

        # Level
        level_label_e = ttk.Label(self, text="Level:")
        self.edit_labels.append(level_label_e)
        level_entry = ttk.Entry(self)
        level_entry.insert(0, self.character_details.Level)
        self.edit_values.append(level_entry)

        # Stats
        stats_label_e = ttk.Label(self, text="Stats:")
        self.edit_labels.append(stats_label_e)
        stats_label_e = ttk.Label(self, text="")
        self.edit_values.append(stats_label_e)

        for stat in self.character_details.Stats:
            label_e = ttk.Label(self, text='    ' + stat + ':')
            self.edit_labels.append(label_e)
            entry = ttk.Entry(self, )
            entry.insert(0, self.character_details.Stats.get(stat))
            self.edit_values.append(entry)

        # Items
        items_label_e = ttk.Label(self, text="Items:")
        self.edit_labels.append(items_label_e)
        items_label_e = ttk.Label(self, text="")
        self.edit_values.append(items_label_e)

        for item in self.character_details.Items:
            label_e = ttk.Label(self, text='    ' + item.Name)
            self.edit_labels.append(label_e)
            remove_button = ttk.Button(self, text="Remove",
                                       command=functools.partial(self.remove_item, item.Id, self.character_id))
            self.edit_values.append(remove_button)

        add_button = ttk.Button(self, text="Add item", command=self.open_add_item_window)
        self.edit_labels.append(add_button)
        empty_label = ttk.Label(self, text='')
        self.edit_values.append(empty_label)

        # Spells
        spells_label_e = ttk.Label(self, text="Spells:")
        self.edit_labels.append(spells_label_e)
        spells_label_e = ttk.Label(self, text="")
        self.edit_values.append(spells_label_e)

        for spell in self.character_details.Spells:
            label_e = ttk.Label(self, text='    ' + spell.Name)
            self.edit_labels.append(label_e)
            remove_button = ttk.Button(self, text="Remove",
                                       command=functools.partial(self.remove_spell, spell.Id, self.character_id))
            self.edit_values.append(remove_button)

        add_button = ttk.Button(self, text="Add spell", command=self.open_add_spell_window)
        self.edit_labels.append(add_button)
        empty_label = ttk.Label(self, text='')
        self.edit_values.append(empty_label)

        # Campaigns
        campaigns_label_e = ttk.Label(self, text="Campaigns:")
        self.edit_labels.append(campaigns_label_e)
        campaigns_label_e = ttk.Label(self, text="")
        self.edit_values.append(campaigns_label_e)

        for campaign in self.character_details.Campaigns:
            label_e = ttk.Label(self, text='    ' + campaign.Name)
            self.edit_labels.append(label_e)
            remove_button = ttk.Button(self, text="Remove",
                                       command=functools.partial(self.remove_campaign, campaign.Id, self.character_id))
            self.edit_values.append(remove_button)

        add_button = ttk.Button(self, text="Add campaign", command=self.open_add_campaign_window)
        self.edit_labels.append(add_button)
        empty_label = ttk.Label(self, text='')
        self.edit_values.append(empty_label)

        # ----- BUTTONS AT THE BOTTOM (for both modes) -----------------------------------------------------------------
        edit_button = ttk.Button(self, text="Edit", command=self.change_mode)
        save_button = ttk.Button(self, text="Save changes", command=self.edit)
        edit_button.grid(column=0, columnspan=1, pady=5)
        self.view_labels.append(edit_button)
        self.edit_labels.append(save_button)

        delete_button = ttk.Button(self, text="Delete", command=self.delete_character)
        delete_button_e = ttk.Button(self, text="Delete", command=self.delete_character)
        delete_button.grid(column=1, columnspan=1, pady=5)
        delete_button_e.grid(column=1, columnspan=1, pady=5)
        self.view_values.append(delete_button)
        self.edit_values.append(delete_button_e)

        # ---- Positioning elements ------------------------------------------------------------------------------------
        for i in range(len(self.view_labels)):
            self.view_labels[i].grid(row=i, column=0, sticky=tk.W)
            self.view_values[i].grid(row=i, column=1, sticky=tk.W)

        for i in range(len(self.edit_labels)):
            self.edit_labels[i].grid(row=i, column=0, sticky=tk.W)
            self.edit_values[i].grid(row=i, column=1, sticky=tk.W)

        # ---- Setting the mode ----------------------------------------------------------------------------------------
        self.change_mode()
