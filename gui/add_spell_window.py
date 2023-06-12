import tkinter as tk
from tkinter import messagebox

import database
from data.schema_definition import SpellSchema


class AddSpellWindow(tk.Toplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
        self.title("Add New Spell")

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

        self.button_add = tk.Button(self, text="Add", command=self.add_spell)
        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)

        self.db = db

    def add_spell(self):
        spell = SpellSchema(Name=self.entry_name.get(), Description=self.entry_desc.get("1.0", "end-1c"))
        self.db.add_spell(spell, self.parent.character_id)
        messagebox.showinfo("Success", "Spell added successfully!")
        self.parent.refresh()
        self.destroy()

if __name__ == "__main__":
    app = tk.Tk()
    db = database.Database()
    add_character_window = AddSpellWindow(app, db)
    app.mainloop()
