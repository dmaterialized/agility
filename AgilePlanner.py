
# this is the correct file for AgilePlanner.


# AGILE Toolkit
# by DM Cook
# begun 2016.07.24
# version 0.3
# m: 2017.08.17

#  TODO
# - addTo doesn't get values added to it from the timeframe evaluator
# - need to store list items in an array
# - make sure that we handle "Go Back" being issued as first command
# - make sure we have method for printing any specific list at any time in the process.
# - make sure lowercase works as well as uppercase for specifying list names.
# - error correction when typing name of a list (otherwise it doesn't work right)
# - create an error printer and request errors from the error printer
# - create a db to store this info in (use bookstore as an example)
# - add the modified date and created date automatically



import string, datetime, sqlite3

# set some vars
addTo = "xxx"
theItem = ""
global theItem

# build arrays
weeklyTasks = ['no items']
monthlyTasks = ['no items']
quarterlyTasks = ['no items']
# may need to remove these upon switch to sqlite3.








# SQL CONNECTION =======================================================
# ======================================================================


# create a database first (using OOP)
class Database:
    # create blueprint of the object
    # then create object instances

    def __init__(self,db):# this syntax is a constructor

    # __init__ is how python creates an initial call when class is instanced.
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor() # TODO: HOW: how exactly does self.cur work?
        self.cur.execute("CREATE TABLE IF NOT EXISTS agile (id INTEGER PRIMARY KEY, item text, notes text, createdtime text, modifiedtime text)")
        self.conn.commit()

    def insert(id, item, notes, createdtime, modifiedtime):
        self.cur.execute("INSERT INTO agile VALUES (NULL,?,?,?,?)",(item,notes,createdtime,modifiedtime))
        self.conn.commit()
        #TODO: how to add the modified date and created date automatically?
    #
    # TODO: This code is from bookstore. Commenting out until the following items
    # are using correct values for the  agileplanner (not bookstore!)

    # def view(self):
    #     self.cur.execute("SELECT * from booktable")
    #     rows=self.cur.fetchall()
    #     self.conn.commit()
    #     return rows
    #
    # def search(self,title="",author="",year="",isbn=""):
    #     self.cur.execute("SELECT * from booktable WHERE title=? OR author=? or year=? OR isbn=?",(title,author,year,isbn))
    #     rows=self.cur.fetchall()
    #     self.conn.commit()
    #     return rows
    #
    # def delete(self,id):
    #     self.cur.execute("DELETE FROM booktable WHERE id=?",(id,))
    #     # rows=cur.fetchall()
    #     self.conn.commit()
    #
    # def update(self,id, title, author, year, isbn):
    #     self.cur.execute("UPDATE booktable SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn, id))
    #     self.conn.commit()
    #
    #     # need a close method now.
    # def __del__(self):
    #     self.conn.close()

print("Backend initialized.") # check in when loaded

# ============================================================================


# commenting out during switch to sqlite3 (from what was once a text file)
# open the working file
# file=open('agile.txt','a')








# ============================================
# ======= F U N C T I O N S ##################
# ============================================

def initializer():
    print("hello!")
    print("do you want to view the current list, or add a new item?")


def reviewMode():
    print("welcome to Review Mode.")
    # more to come

def getTimeframe(text): #follows up with a request for timeframe
    if "add" in text: #where does it look for text var? - unanswered question
        timeframe = input("Where does this entry go? \n Weekly, Monthly or Quarterly?: ")
        evaluateInput(timeframe) # sends the timeframe to evaluateInput


# takes an item and checks its timeframe
def evaluateInput(timeframe):
    global addTo
    global theItem
    if timeframe == "Weekly":
        addTo = "weeklyTasks"
        printDestination()
        weeklyTasks.insert(0,theItem)

    if timeframe == "Monthly":
         addTo = "monthlyTasks"
         monthlyTasks.insert(0,theItem)
         printDestination()
    if timeframe == "Quarterly":
         addTo = "quarterlyTasks"
         quarterlyTasks.insert(0,theItem)
         printDestination()
    if (timeframe != "Monthly") or (timeframe !="Weekly") or (timeframe !="Quarterly"):
        print ("Sorry, I didn't get that. Please try again.")




    # next, ask for the item
    theItem = input('what is the item?')

    # how to call a list by a variable name?
    # so far, tried
    # addTo.insert(0, theItem)
    # weeklytasks.append(theItem)
    # print(addTo)
    # def askForItem(theItem):
    #     addTo.push(theItem)
    #     print(addTo)
    #


def printDirections():
    print("Type 'go back' to go back to main menu. \n Type 'review' to enter Review mode. \n Type 'add' to add a new item.")


def printDestination():
    print("The item (" + theItem+") will be added to " + addTo)
    # prints where something is going
    print("the "+addTo+" list now contains:") # good, this worked
    print(weeklyTasks) #good, this worked (but the method to push doesn't work)
    # end print destination


# Review phase needs to be set up


# ===============
#    showtime
#     . . .
# ===============

initializer()
printDirections()
initInput = input("What next? ")
getTimeframe(initInput) # passes everything over for eval
printDestination()
