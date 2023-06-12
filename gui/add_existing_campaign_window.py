import tkinter as tk
from tkinter import messagebox, ttk

from data.schema_definition import CampaignSchema
from gui.add_campaign_window import AddCampaignWindow

import database


class AddExistingCampaignWindow(tk.Toplevel):
    """
    A window for adding an existing campaign to a character.

    Args:
        parent (tk.Widget): The parent widget.
        db (database.Database): The database object.

    Attributes:
        parent (tk.Widget): The parent widget.
        db (database.Database): The database object.
        combobox_campaign (ttk.Combobox): The combobox widget for selecting an existing campaign.
    """
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
        self.db = db
        self.title("Add or Select Campaign")

        label = tk.Label(self, text="Select one of the existing campaigns or create a new one")
        label.grid(row=0, columnspan=2)

        self.combobox_campaign = ttk.Combobox(self, state="readonly")
        self.combobox_campaign.grid(row=1, columnspan=2)

        campaigns = db.get_campaigns()
        campaign_names = []
        for c in campaigns:
            campaign_names.append(c.Name)

        self.combobox_campaign["values"] = campaign_names

        button = tk.Button(self, text="Add Selected", command=self.add_campaign_to_user)
        button.grid(row=2, column=0, sticky="e")

        button = tk.Button(self, text="Add New", command=self.open_new_campaign_window)
        button.grid(row=2, column=1, sticky="w")

    def add_campaign_to_user(self):
        """
        Add the selected campaign to the character.

        Retrieves the campaign ID based on the selected campaign name, adds the campaign to the character
        in the database, displays a success message, refreshes the parent window, and closes the current window.
        """
        camp_id = self.db.get_campaign_id(self.combobox_campaign.get())
        self.db.add_campaign_to_character(self.parent.character_id, camp_id)
        messagebox.showinfo("Success", "Campaign assigned successfully!")
        self.parent.refresh()
        self.destroy()

    def open_new_campaign_window(self):
        """
        Open the window for adding a new campaign.

        Opens the AddCampaignWindow and closes the current window.
        """
        new_campaign_window = AddCampaignWindow(self.parent, self.db)
        self.destroy()

if __name__ == "__main__":
    app = tk.Tk()
    db = database.Database()
    add_character_window = AddExistingCampaignWindow(app, db)
    app.mainloop()
