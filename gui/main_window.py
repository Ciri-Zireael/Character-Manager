import tkinter as tk
from tkinter import ttk

import database
from gui.character_details_window import CharacterDetailsWindow
from gui.add_character_window import AddCharacterWindow


class MainWindow(tk.Tk):
    def __init__(self, database):
        super().__init__()
        self.title("Character Management")
        self.database = database
        self.geometry("300x700")

        # Create a treeview widget to display the list of characters
        self.treeview = ttk.Treeview(self, height=30)
        self.treeview.heading("#0", text="Character List")
        self.treeview.bind("<<TreeviewSelect>>", self.view_character_details)
        self.treeview.pack(fill="both", expand=True)  # Set pack options to fill and expand

        self.characters = database.get_characters()

        # Populate the treeview with character names
        for character in self.characters:
            self.treeview.insert("", "end", text=f'{character.Name} {character.Surname}   lv.{character.Level}',
                                 values=character.Id)

        # Add button for adding a new character
        add_button = ttk.Button(self, text="Add Character", command=self.open_add_character_window)
        add_button.pack()

    def view_character_details(self, event):
        selected_item = self.treeview.focus()
        character_id = self.treeview.item(selected_item)["values"][0]
        character_details_window = CharacterDetailsWindow(self, character_id, self.database)

    def open_add_character_window(self):
        add_character_window = AddCharacterWindow(self, self.database)

    def refresh(self):
        # Retrieve the updated list of characters from the database
        characters = self.database.get_characters()

        self.treeview.delete(*self.treeview.get_children())
        # Create labels for each character and add them to the character frame
        for character in characters:
            self.treeview.insert("", "end", text=f'{character.Name} {character.Surname}   lv.{character.Level}',
                                 values=character.Id)


def start_main_window(database):

    # Create the main window and start the Tkinter event loop
    main_window = MainWindow(database)
    main_window.mainloop()


if __name__ == "__main__":
    start_main_window(database.Database())
