import tkinter as tk
from tkinter import messagebox, ttk
from gui.add_campaign_window import AddCampaignWindow

import database


class AddExistingCampaignWindow(tk.Toplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
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

        button = tk.Button(self, text="Add Selected", command=self.add_campaign)
        button.grid(row=2, column=0, sticky="e")

        button = tk.Button(self, text="Add New", command=self.open_new_campaign_window)
        button.grid(row=2, column=1, sticky="w")

        self.db = db

    def add_campaign(self):

        # self.db.add_character(char, char_data)
        messagebox.showinfo("Success", "Character added successfully!")
        self.parent.refresh()
        self.destroy()

    def open_new_campaign_window(self):
        pass
        new_campaign_window = AddCampaignWindow(self.parent, db)

if __name__ == "__main__":
    app = tk.Tk()
    db = database.Database()
    add_character_window = AddExistingCampaignWindow(app, db)
    app.mainloop()
