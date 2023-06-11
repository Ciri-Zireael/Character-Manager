import tkinter as tk
from copy import copy
from tkinter import ttk, messagebox


class CharacterDetailsWindow(tk.Toplevel):
    def __init__(self, parent, character_id, database):
        super().__init__(parent)

        # Retrieve the character details based on the character ID
        self.character_details = database.get_character_details_by_id(character_id)

        self.title(f"{self.character_details.Name} {self.character_details.Surname} - Details")

        self.view_labels = []
        self.edit_labels = []
        self.view_values = []
        self.edit_values = []

        self.index = 0

        self.edit_mode = False

        name_label = ttk.Label(self, text="Name:")
        self.view_labels.append(name_label)

        name_value = ttk.Label(self, text=self.character_details.Name)
        self.view_values.append(name_value)
        name_value_e = ttk.Label(self, text=self.character_details.Name)
        # self.edit_values.append(name_value_e)

        surname_label = ttk.Label(self, text="Surname:")
        self.view_labels.append(surname_label)

        surname_value = ttk.Label(self, text=self.character_details.Surname)
        self.view_values.append(surname_value)
        # surname_value_e = ttk.Label(self, text=self.character_details.Surname)

        full_name_label = ttk.Label(self, text=self.character_details.Name+' '+self.character_details.Surname)
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

            entry = ttk.Entry(self)
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
            value.grid(row=self.index, column=1, sticky=tk.W)
            self.view_values.append(value)

            entry = ttk.Entry(self, textvariable=item.Description)
            entry.insert(0, item.Description)
            self.edit_values.append(entry)

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

            entry = ttk.Entry(self, textvariable=spell.Description)
            entry.insert(0, spell.Description)
            self.edit_values.append(entry)

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
            label_e = ttk.Label(self, text='    ' + campaign.Name)
            self.view_labels.append(label)
            self.edit_labels.append(label_e)

            details_button = ttk.Button(self, text="See Details", command=lambda c=campaign: show_campaign_details(c))
            details_button_e = ttk.Button(self, text="See Details", command=lambda c=campaign: show_campaign_details(c))
            self.view_values.append(details_button)
            self.edit_values.append(details_button_e)

        # Add a button to close the window
        self.edit_button = ttk.Button(self, text="Edit", command=self.change_mode)
        self.save_button = ttk.Button(self, text="Save changes", command=self.edit)
        self.edit_button.grid(column=0, columnspan=1, pady=5)
        self.view_labels.append(self.edit_button)
        self.edit_labels.append(self.save_button)

        close_button = ttk.Button(self, text="Close", command=self.destroy)
        close_button_e = ttk.Button(self, text="Close", command=self.destroy)
        close_button.grid(column=1, columnspan=1, pady=5)
        self.view_values.append(close_button)
        self.edit_values.append(close_button_e)

        for i in range(len(self.view_labels)):
            self.view_labels[i].grid(row=i, column=0, sticky=tk.W)
            self.view_values[i].grid(row=i, column=1, sticky=tk.W)

        for i in range(len(self.edit_labels)):
            self.edit_labels[i].grid(row=i, column=0, sticky=tk.W)
            self.edit_labels[i].grid_remove()
            self.edit_values[i].grid(row=i, column=1, sticky=tk.W)
            self.edit_values[i].grid_remove()

        # for label, value in zip(self.edit_labels, self.edit_values):
        #     print(label.cget("text"), value.cget("text"))
        #
        # print()
        # for label, value in zip(self.view_labels, self.view_values):
        #     print(label.cget("text"), value.cget("text"))

    def change_mode(self):
        print("entered edit mode")
        self.edit_mode = not self.edit_mode

        if self.edit_mode:
            for label, value in zip(self.view_labels, self.view_values):
                label.grid_remove()
                value.grid_remove()
            for label, value in zip(self.edit_labels, self.edit_values):
                label.grid()
                value.grid()
                print(label.cget("text"), value.cget("text"))

        else:
            for label, value in zip(self.edit_labels, self.edit_values):
                label.grid_remove()
                value.grid_remove()
            for label, value in zip(self.view_labels, self.view_values):
                label.grid()
                value.grid()
                print(label.cget("text"), value.cget("text"))

    def edit(self):
        self.change_mode()


def show_campaign_details(campaign):
    # Display a message box with the campaign details
    message = f"Campaign Name: {campaign.Name}\n\nDescription: {campaign.Description}"
    messagebox.showinfo("Campaign Details", message)
