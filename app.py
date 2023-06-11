import Database
from gui import start_main_window

# Create the database
db = Database.Database()

# Pass the database to the main window and start the main window
start_main_window(db)
