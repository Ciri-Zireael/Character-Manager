import tkinter as tk
from tkinter import messagebox

import database


class AddCampaignWindow(tk.Toplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
        self.title("Add Campaign")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        label = tk.Label(self, text="Name:")
        label.grid(row=0, column=0, sticky="w")
        entry = tk.Entry(self, width=35)
        entry.grid(row=0, column=1, pady=5, sticky="e")
        label = tk.Label(self, text="Description:")
        label.grid(row=1, column=0, sticky="w")
        entry = tk.Text(self, width=40, height=10)
        entry.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")

        self.button_add = tk.Button(self, text="Add", command=self.add_campaign)
        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)

        self.db = db

    def add_campaign(self):
        pass

        # self.db.add_character(char, char_data)
        messagebox.showinfo("Success", "Character added successfully!")
        self.parent.refresh()
        self.destroy()

if __name__ == "__main__":
    app = tk.Tk()
    db = database.Database()
    add_character_window = AddCampaignWindow(app, db)
    app.mainloop()
