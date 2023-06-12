import tkinter as tk
from tkinter import messagebox, ttk

import database
from gui.add_spell_window import AddSpellWindow


class AddExistingSpellWindow(tk.Toplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
        self.db = db
        self.title("Add or Select Spell")

        label = tk.Label(self, text="Select one of the existing spells or create a new one")
        label.grid(row=0, columnspan=2)

        self.combobox_spells = ttk.Combobox(self, state="readonly")
        self.combobox_spells.grid(row=1, columnspan=2)

        spells = db.get_spells()
        spell_names = []
        for i in spells:
            spell_names.append(i.Name)

        self.combobox_spells["values"] = spell_names

        button = tk.Button(self, text="Add Selected", command=self.add_spell_to_character)
        button.grid(row=2, column=0, sticky="e")

        button = tk.Button(self, text="Add New", command=self.open_new_spell_window)
        button.grid(row=2, column=1, sticky="w")

    def add_spell_to_character(self):
        spell_id = self.db.get_spell_id(self.combobox_spells.get())
        self.db.add_spell_to_character(self.parent.character_id, spell_id)
        messagebox.showinfo("Success", "Spell assigned successfully!")
        self.parent.refresh()
        self.destroy()

    def open_new_spell_window(self):
        new_campaign_window = AddSpellWindow(self.parent, self.db)
        self.destroy()

if __name__ == "__main__":
    app = tk.Tk()
    db = database.Database()
    add_character_window = AddExistingSpellWindow(app, db)
    app.mainloop()
