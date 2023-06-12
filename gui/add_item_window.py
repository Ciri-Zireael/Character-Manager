import tkinter as tk
from tkinter import messagebox

import database
from data.schema_definition import ItemSchema


class AddItemWindow(tk.Toplevel):
    """
    A window for adding a new item.

    Args:
        parent (tk.Widget): The parent widget.
        db (database.Database): The database object.

    Attributes:
        parent (tk.Widget): The parent widget.
        db (database.Database): The database object.
        entry_name (tk.Entry): The entry widget for entering the item name.
        entry_desc (tk.Text): The text widget for entering the item description.
    """
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
        self.title("Add New Item")

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

        self.button_add = tk.Button(self, text="Add", command=self.add_item)
        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)

        self.db = db

    def add_item(self):
        """
        Add the new item.

        Retrieves the item name and description from the entry widgets, creates an ItemSchema object,
        adds the item to the character in the database, displays a success message, refreshes the parent window,
        and closes the current window.
        """
        item = ItemSchema(Name=self.entry_name.get(), Description=self.entry_desc.get("1.0", "end-1c"))
        self.db.add_item(item, self.parent.character_id)
        self.parent.refresh()
        self.destroy()

if __name__ == "__main__":
    app = tk.Tk()
    db = database.Database()
    add_character_window = AddItemWindow(app, db)
    app.mainloop()
