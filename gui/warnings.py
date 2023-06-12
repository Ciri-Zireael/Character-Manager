from tkinter import messagebox


def campaign_already_exists_warning():
    message = "Campaign with such name already exists."
    messagebox.showwarning("Name already defined", message)


def item_already_exists_warning():
    message = "Item with such name already exists."
    messagebox.showwarning("Name already defined", message)


def spell_already_exists_warning():
    message = "Spell with such name already exists."
    messagebox.showwarning("Name already defined", message)
