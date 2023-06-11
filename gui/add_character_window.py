import tkinter as tk
from tkinter import messagebox

from data.schema_definition import CharacterSchema, CharacterDataSchema


class AddCharacterWindow(tk.Toplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.title("Add Character")
        # self.geometry("400x300")

        # Create widgets and add them to the window
        self.label_name = tk.Label(self, text="Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self)
        self.entry_name.pack(pady=5)

        self.label_surname = tk.Label(self, text="Surname:")
        self.label_surname.pack()
        self.entry_surname = tk.Entry(self)
        self.entry_surname.pack(pady=5)

        self.label_level = tk.Label(self, text="Level:")
        self.label_level.pack()
        self.entry_level = tk.Entry(self)
        self.entry_level.pack(pady=5)

        self.label_class = tk.Label(self, text="Class:")
        self.label_class.pack()
        self.entry_class = tk.Entry(self)
        self.entry_class.pack(pady=5)

        self.label_race = tk.Label(self, text="Race:")
        self.label_race.pack()
        self.entry_race = tk.Entry(self)
        self.entry_race.pack(pady=5)

        self.label_prof = tk.Label(self, text="Proficiency bonus:")
        self.label_prof.pack()
        self.entry_prof = tk.Entry(self)
        self.entry_prof.pack(pady=5)

        self.label_str = tk.Label(self, text="Strength:")
        self.label_str.pack()
        self.entry_str = tk.Entry(self)
        self.entry_str.pack(pady=5)

        self.label_dex = tk.Label(self, text="Dexterity:")
        self.label_dex.pack()
        self.entry_dex = tk.Entry(self)
        self.entry_dex.pack(pady=5)

        self.label_con = tk.Label(self, text="Constitution:")
        self.label_con.pack()
        self.entry_con = tk.Entry(self)
        self.entry_con.pack(pady=5)

        self.label_int = tk.Label(self, text="Intelligence:")
        self.label_int.pack()
        self.entry_int = tk.Entry(self)
        self.entry_int.pack(pady=5)

        self.label_wis = tk.Label(self, text="Wisdom:")
        self.label_wis.pack()
        self.entry_wis = tk.Entry(self)
        self.entry_wis.pack(pady=5)

        self.label_char = tk.Label(self, text="Charisma:")
        self.label_char.pack()
        self.entry_char = tk.Entry(self)
        self.entry_char.pack(pady=5)

        self.button_add = tk.Button(self, text="Add", command=self.add_character)
        self.button_add.pack(pady=10)

        self.db = db

    def add_character(self):
        char = CharacterSchema()
        char.Name = self.entry_name.get()
        char.Surname = self.entry_surname.get()
        char.Level = self.entry_level.get()
        char.Race = self.entry_race.get()
        char.Class = self.entry_class.get()

        char_data = CharacterDataSchema()
        char_data.Proficiency_bonus = self.entry_prof.get()
        char_data.Strength = self.entry_str.get()
        char_data.Dexterity = self.entry_dex.get()
        char_data.Constitution = self.entry_con.get()
        char_data.Intelligence = self.entry_int.get()
        char_data.Wisdom = self.entry_wis.get()
        char_data.Charisma = self.entry_char.get()

        self.db.add_character(char, char_data)
        messagebox.showinfo("Success", "Character added successfully!")
        self.destroy()


if __name__ == "__main__":
    app = tk.Tk()
    add_character_window = AddCharacterWindow(app)
    app.mainloop()
