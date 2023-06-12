import tkinter as tk
from tkinter import messagebox, ttk

import database
from gui.add_item_window import AddItemWindow


class AddExistingItemWindow(tk.Toplevel):
    """
    A window for adding an existing item to a character.

    Args:
        parent (tk.Widget): The parent widget.
        db (database.Database): The database object.

    Attributes:
        parent (tk.Widget): The parent widget.
        db (database.Database): The database object.
        combobox_items (ttk.Combobox): The combobox widget for selecting an existing item.
    """
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
        self.db = db
        self.title("Add or Select Item")

        label = tk.Label(self, text="Select one of the existing items or create a new one")
        label.grid(row=0, columnspan=2)

        self.combobox_items = ttk.Combobox(self, state="readonly")
        self.combobox_items.grid(row=1, columnspan=2)

        items = db.get_items()
        item_names = []
        for i in items:
            item_names.append(i.Name)

        self.combobox_items["values"] = item_names

        button = tk.Button(self, text="Add Selected", command=self.add_item_to_character)
        button.grid(row=2, column=0, sticky="e")

        button = tk.Button(self, text="Add New", command=self.open_new_item_window)
        button.grid(row=2, column=1, sticky="w")

    def add_item_to_character(self):
        """
        Add the selected item to the character.

        Retrieves the item ID based on the selected item name, adds the item to the character
        in the database, displays a success message, refreshes the parent window, and closes the current window.
        """
        item_id = self.db.get_item_id(self.combobox_items.get())
        self.db.add_item_to_character(self.parent.character_id, item_id)
        messagebox.showinfo("Success", "Item assigned successfully!")
        self.parent.refresh()
        self.destroy()

    def open_new_item_window(self):
        """
        Open the window for adding a new item.

        Opens the AddItemWindow and closes the current window.
        """
        new_campaign_window = AddItemWindow(self.parent, self.db)
        self.destroy()

if __name__ == "__main__":
    app = tk.Tk()
    db = database.Database()
    add_character_window = AddExistingItemWindow(app, db)
    app.mainloop()
