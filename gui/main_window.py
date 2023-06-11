import tkinter as tk
from tkinter import ttk

import Database
from add_character_window import AddCharacterWindow
from character_details_window import CharacterDetailsWindow


class MainWindow(tk.Tk):
    def __init__(self, database):
        super().__init__()
        self.title("Character Management")
        self.database = database

        # Create a treeview widget to display the list of characters
        self.treeview = ttk.Treeview(self)
        self.treeview.heading("#0", text="Character List")
        self.treeview.bind("<<TreeviewSelect>>", self.view_character_details)
        self.treeview.pack()

        characters = database.get_characters()

        # Populate the treeview with character names
        for character in characters:
            self.treeview.insert("", "end", text=f'{character.Name} {character.Surname}   lv.{character.Level}', values=character.Id)

        # Add button for adding a new character
        add_button = ttk.Button(self, text="Add Character", command=self.open_add_character_window)
        add_button.pack()

    def view_character_details(self, event):
        selected_item = self.treeview.focus()
        character_id = self.treeview.item(selected_item)["values"][0]
        character_details_window = CharacterDetailsWindow(self, character_id, self.database)

    def open_add_character_window(self):
        add_character_window = AddCharacterWindow(self, self.database)


def start_main_window(database):

    # Create the main window and start the Tkinter event loop
    main_window = MainWindow(database)
    main_window.mainloop()


if __name__ == "__main__":
    start_main_window(Database.Database())

