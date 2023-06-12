import tkinter as tk
from tkinter import messagebox

from data.schema_definition import CharacterSchema, CharacterDataSchema


class AddCharacterWindow(tk.Toplevel):
    """
    A window for adding a character.

    Args:
        parent (tk.Widget): The parent widget.
        db (database.Database): The database object.

    Attributes:
        parent (tk.Widget): The parent widget.
        entry_name (tk.Entry): The entry widget for character name.
        entry_surname (tk.Entry): The entry widget for character surname.
        entry_level (tk.Entry): The entry widget for character level.
        entry_class (tk.Entry): The entry widget for character class.
        entry_race (tk.Entry): The entry widget for character race.
        entry_prof (tk.Entry): The entry widget for character proficiency bonus.
        entry_str (tk.Entry): The entry widget for character strength.
        entry_dex (tk.Entry): The entry widget for character dexterity.
        entry_con (tk.Entry): The entry widget for character constitution.
        entry_int (tk.Entry): The entry widget for character intelligence.
        entry_wis (tk.Entry): The entry widget for character wisdom.
        entry_char (tk.Entry): The entry widget for character charisma.
        button_add (tk.Button): The button widget for adding the character.
        db (database.Database): The database object.
    """
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
        """
        Add a character to the database.

        Creates a CharacterSchema object and a CharacterDataSchema object based on the entered
        character details, adds them to the database, displays a success message, refreshes the
        parent window, and closes the current window.
        """
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
