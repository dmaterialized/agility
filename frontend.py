# AgilePlanner Front End (tkinter)


from tkinter import *
from AgilePlanner import Database
database=Database("agile.db")

print("Frontend initialized.")
database.view()
