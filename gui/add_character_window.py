import tkinter as tk
from tkinter import messagebox

from data.schema_definition import CharacterSchema, CharacterDataSchema


class AddCharacterWindow(tk.Toplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
        self.title("Add Character")

        # Create a grid for labels and entries
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Add label-entry pairs for each field
        fields = [
            ("Name", "entry_name"),
            ("Surname", "entry_surname"),
            ("Level", "entry_level"),
            ("Class", "entry_class"),
            ("Race", "entry_race"),
            ("Proficiency bonus", "entry_prof"),
            ("Strength", "entry_str"),
            ("Dexterity", "entry_dex"),
            ("Constitution", "entry_con"),
            ("Intelligence", "entry_int"),
            ("Wisdom", "entry_wis"),
            ("Charisma", "entry_char")
        ]

        for row, (label_text, entry_name) in enumerate(fields):
            label = tk.Label(self, text=label_text + ":")
            label.grid(row=row, column=0, sticky="e")
            entry = tk.Entry(self)
            entry.grid(row=row, column=1, pady=5, sticky="w")
            setattr(self, entry_name, entry)

        # Add the "Add" button
        self.button_add = tk.Button(self, text="Add", command=self.add_character)
        self.button_add.grid(row=len(fields), column=0, columnspan=2, pady=10)

        self.db = db

    def add_character(self):
        char = CharacterSchema(
            Name=self.entry_name.get(),
            Surname=self.entry_surname.get(),
            Level=self.entry_level.get(),
            Race=self.entry_race.get(),
            Class=self.entry_class.get()
        )

        char_data = CharacterDataSchema(
            Proficiency_bonus=self.entry_prof.get(),
            Strength=self.entry_str.get(),
            Dexterity=self.entry_dex.get(),
            Constitution=self.entry_con.get(),
            Intelligence=self.entry_int.get(),
            Wisdom=self.entry_wis.get(),
            Charisma=self.entry_char.get()
        )

        self.db.add_character(char, char_data)
        messagebox.showinfo("Success", "Character added successfully!")
        self.parent.refresh()
        self.destroy()


if __name__ == "__main__":
    app = tk.Tk()
    add_character_window = AddCharacterWindow(app)
    app.mainloop()
