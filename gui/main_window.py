import tkinter as tk
from tkinter import ttk

import database
from gui.character_details_window import CharacterDetailsWindow
from gui.add_character_window import AddCharacterWindow


class MainWindow(tk.Tk):
    """
    Main window for the character management application.
    """
    def __init__(self, database):
        """
        Initialize the main window.

        Args:
            database (database.Database): The database object.
        """
        super().__init__()
        self.title("Character Management")
        self.database = database
        self.geometry("300x700")

        self.treeview = ttk.Treeview(self, height=30)
        self.treeview.heading("#0", text="Character List")
        self.treeview.bind("<<TreeviewSelect>>", self.view_character_details)
        self.treeview.pack(fill="both", expand=True)  # Set pack options to fill and expand

        self.characters = database.get_characters()

        for character in self.characters:
            self.treeview.insert("", "end", text=f'{character.Name} {character.Surname}   lv.{character.Level}',
                                 values=character.Id)

        add_button = ttk.Button(self, text="Add Character", command=self.open_add_character_window)
        add_button.pack()

    def view_character_details(self, event):
        """
        Event handler for selecting a character in the treeview.

        Args:
            event (tk.Event): The event object.
        """
        selected_item = self.treeview.focus()
        item_text = self.treeview.item(selected_item)["text"]
        if "lv." in item_text:
            character_id = self.treeview.item(selected_item)["values"][0]
            character_details_window = CharacterDetailsWindow(self, character_id, self.database)

    def open_add_character_window(self):
        """
        Open the window for adding a new character.
        """
        add_character_window = AddCharacterWindow(self, self.database)

    def refresh(self):
        """
        Refresh the character list in the treeview.
        """
        characters = self.database.get_characters()

        self.treeview.delete(*self.treeview.get_children())

        for character in characters:
            self.treeview.insert("", "end", text=f'{character.Name} {character.Surname}   lv.{character.Level}',
                                 values=character.Id)


def start_main_window(database):
    """
    Start the main window of the application.

    Args:
        database (database.Database): The database object.
    """
    main_window = MainWindow(database)
    main_window.mainloop()


if __name__ == "__main__":
    start_main_window(database.Database())
