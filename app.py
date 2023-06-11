import database
from gui import start_main_window

# Create the database
db = database.Database()

# Pass the database to the main window and start the main window
start_main_window(db)
