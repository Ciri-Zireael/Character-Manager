import tkinter as tk
from tkinter import messagebox

import database
from data.schema_definition import CampaignSchema


class AddCampaignWindow(tk.Toplevel):
    """
    A window for adding a campaign.

    Args:
        parent (tk.Widget): The parent widget.
        db (database.Database): The database object.

    Attributes:
        parent (tk.Widget): The parent widget.
        entry_name (tk.Entry): The entry widget for campaign name.
        entry_desc (tk.Text): The text widget for campaign description.
        button_add (tk.Button): The button widget for adding the campaign.
        db (database.Database): The database object.
    """
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
        self.title("Add Campaign")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        label = tk.Label(self, text="Name:")
        label.grid(row=0, column=0, sticky="w")
        self.entry_name = tk.Entry(self, width=35)
        self.entry_name.grid(row=0, column=1, pady=5, sticky="e")
        label = tk.Label(self, text="Description:")
        label.grid(row=1, column=0, sticky="w")
        self.entry_desc = tk.Text(self, width=40, height=10)
        self.entry_desc.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")

        self.button_add = tk.Button(self, text="Add", command=self.add_campaign)
        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)

        self.db = db

    def add_campaign(self):
        """
        Add a campaign to the database.

        Creates a CampaignSchema object based on the entered name and description,
        adds it to the database, displays a success message, refreshes the parent window,
        and closes the current window.
        """
        campaign = CampaignSchema(Name=self.entry_name.get(), Description=self.entry_desc.get("1.0", "end-1c"))
        self.db.add_campaign(campaign, self.parent.character_id)
        messagebox.showinfo("Success", "Campaign added successfully!")
        self.parent.refresh()
        self.destroy()


if __name__ == "__main__":
    app = tk.Tk()
    db = database.Database()
    add_character_window = AddCampaignWindow(app, db)
    app.mainloop()
