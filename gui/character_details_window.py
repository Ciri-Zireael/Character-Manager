import tkinter as tk
from tkinter import ttk, messagebox

from data.schema_definition import CharacterUpdateSchema
from gui.add_existing_campaign_window import AddExistingCampaignWindow


class CharacterDetailsWindow(tk.Toplevel):
    def __init__(self, parent, character_id, database):
        super().__init__(parent)

        self.character_details = database.get_character_details_by_id(character_id)
        self.character_id = character_id
        self.database = database

        self.title(f"{self.character_details.Name} {self.character_details.Surname} - Details")

        self.view_labels = []
        self.edit_labels = []
        self.view_values = []
        self.edit_values = []

        self.edit_mode = True

        self.fill_fields()

    def change_mode(self):
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

    def remove_spell(self, spell_id, character_id):
        pass

    def add_spell(self):
        pass

    def remove_item(self, item_id, character_id):
        pass

    def add_item(self):
        pass

    def remove_campaign(self, campaign_id, character_id):
        # self.database
        pass

    def open_add_campaign_window(self):
        new_campaign_widow = AddExistingCampaignWindow(self, self.database)

    def refresh(self):
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

        name_label = ttk.Label(self, text="Name:")
        self.view_labels.append(name_label)

        name_value = ttk.Label(self, text=self.character_details.Name)
        self.view_values.append(name_value)

        surname_label = ttk.Label(self, text="Surname:")
        self.view_labels.append(surname_label)

        surname_value = ttk.Label(self, text=self.character_details.Surname)
        self.view_values.append(surname_value)

        full_name_label = ttk.Label(self, text=self.character_details.Name + ' ' + self.character_details.Surname)
        self.edit_labels.append(full_name_label)
        empty_label = ttk.Label(self, text='')
        self.edit_values.append(empty_label)

        level_label = ttk.Label(self, text="Level:")
        self.view_labels.append(level_label)
        level_label_e = ttk.Label(self, text="Level:")
        self.edit_labels.append(level_label_e)

        level_value = ttk.Label(self, text=self.character_details.Level)
        self.view_values.append(level_value)

        level_entry = ttk.Entry(self, textvariable=self.character_details.Level)
        level_entry.insert(0, self.character_details.Level)
        self.edit_values.append(level_entry)

        class_label = ttk.Label(self, text="Class:")
        self.view_labels.append(class_label)
        class_value = ttk.Label(self, text=self.character_details.Class)
        self.view_values.append(class_value)

        race_label = ttk.Label(self, text="Race:")
        self.view_labels.append(race_label)

        race_value = ttk.Label(self, text=self.character_details.Race)
        self.view_values.append(race_value)

        stats_label = ttk.Label(self, text="Stats:")
        self.view_labels.append(stats_label)
        stats_label_e = ttk.Label(self, text="Stats:")
        self.edit_labels.append(stats_label_e)

        stats_label = ttk.Label(self, text="")
        self.view_values.append(stats_label)
        stats_label_e = ttk.Label(self, text="")
        self.edit_values.append(stats_label_e)

        for stat in self.character_details.Stats:
            label = ttk.Label(self, text='    ' + stat + ':')
            self.view_labels.append(label)
            label_e = ttk.Label(self, text='    ' + stat + ':')
            self.edit_labels.append(label_e)

            value = ttk.Label(self, text=self.character_details.Stats.get(stat))
            self.view_values.append(value)

            entry = ttk.Entry(self, )
            entry.insert(0, self.character_details.Stats.get(stat))
            self.edit_values.append(entry)

        items_label = ttk.Label(self, text="Items:")
        self.view_labels.append(items_label)
        items_label_e = ttk.Label(self, text="Items:")
        self.edit_labels.append(items_label_e)

        items_label = ttk.Label(self, text="")
        self.view_values.append(items_label)
        items_label_e = ttk.Label(self, text="")
        self.edit_values.append(items_label_e)

        for item in self.character_details.Items:
            label = ttk.Label(self, text='    ' + item.Name)
            self.view_labels.append(label)
            label_e = ttk.Label(self, text='    ' + item.Name)
            self.edit_labels.append(label_e)

            value = ttk.Label(self, text=item.Description)
            self.view_values.append(value)

            remove_button = ttk.Button(self, text="Remove", command=self.remove_item(item.Id, self.character_id))
            self.edit_values.append(remove_button)

        add_button = ttk.Button(self, text="Add item", command=self.add_item())
        self.edit_labels.append(add_button)
        empty_label = ttk.Label(self, text='')
        self.edit_values.append(empty_label)

        spells_label = ttk.Label(self, text="Spells:")
        self.view_labels.append(spells_label)
        spells_label_e = ttk.Label(self, text="Spells:")
        self.edit_labels.append(spells_label_e)

        spells_label = ttk.Label(self, text="")
        self.view_values.append(spells_label)
        spells_label_e = ttk.Label(self, text="")
        self.edit_values.append(spells_label_e)

        for spell in self.character_details.Spells:
            label = ttk.Label(self, text='    ' + spell.Name)
            self.view_labels.append(label)
            label_e = ttk.Label(self, text='    ' + spell.Name)
            self.edit_labels.append(label_e)

            value = ttk.Label(self, text=spell.Description)
            self.view_values.append(value)

            remove_button = ttk.Button(self, text="Remove", command=self.remove_spell(spell.Id, self.character_id))
            self.edit_values.append(remove_button)

        add_button = ttk.Button(self, text="Add spell", command=self.add_spell())
        self.edit_labels.append(add_button)
        empty_label = ttk.Label(self, text='')
        self.edit_values.append(empty_label)

        campaigns_label = ttk.Label(self, text="Campaigns:")
        self.view_labels.append(campaigns_label)
        campaigns_label_e = ttk.Label(self, text="Campaigns:")
        self.edit_labels.append(campaigns_label_e)

        campaigns_label = ttk.Label(self, text="")
        self.view_values.append(campaigns_label)
        campaigns_label_e = ttk.Label(self, text="")
        self.edit_values.append(campaigns_label_e)

        for campaign in self.character_details.Campaigns:
            label = ttk.Label(self, text='    ' + campaign.Name)
            self.view_labels.append(label)
            label_e = ttk.Label(self, text='    ' + campaign.Name)
            self.edit_labels.append(label_e)

            details_button = ttk.Button(self, text="See Details", command=lambda c=campaign: show_campaign_details(c))
            self.view_values.append(details_button)

            remove_button = ttk.Button(self, text="Remove",
                                       command=self.remove_campaign(campaign.Id, self.character_id))
            self.edit_values.append(remove_button)

        add_button = ttk.Button(self, text="Add campaign", command=self.open_add_campaign_window)
        self.edit_labels.append(add_button)
        empty_label = ttk.Label(self, text='')
        self.edit_values.append(empty_label)

        edit_button = ttk.Button(self, text="Edit", command=self.change_mode)
        save_button = ttk.Button(self, text="Save changes", command=self.edit)
        edit_button.grid(column=0, columnspan=1, pady=5)
        self.view_labels.append(edit_button)
        self.edit_labels.append(save_button)

        close_button = ttk.Button(self, text="Close", command=self.destroy)
        close_button_e = ttk.Button(self, text="Close", command=self.destroy)
        close_button.grid(column=1, columnspan=1, pady=5)
        self.view_values.append(close_button)
        self.edit_values.append(close_button_e)

        # for label, value in zip(self.edit_labels, self.edit_values):
        #     print(label.cget("text"), value.cget("text"))

        for i in range(len(self.view_labels)):
            self.view_labels[i].grid(row=i, column=0, sticky=tk.W)
            self.view_values[i].grid(row=i, column=1, sticky=tk.W)

        for i in range(len(self.edit_labels)):
            self.edit_labels[i].grid(row=i, column=0, sticky=tk.W)
            self.edit_values[i].grid(row=i, column=1, sticky=tk.W)

        self.change_mode()


def show_campaign_details(campaign):
    message = f"Campaign Name: {campaign.Name}\n\nDescription: {campaign.Description}"
    messagebox.showinfo("Campaign Details", message)
