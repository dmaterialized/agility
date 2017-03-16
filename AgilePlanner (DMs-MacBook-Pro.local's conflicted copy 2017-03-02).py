# AGILE Toolkit
# by DM Cook
# begun 2016.07.24
# version 0.4 - 12.30.2016

#  TODO
# - make sure that we handle "Go Back" being issued as first command
# - make sure we have method for printing any specific list at any time in
#       the process.
# - error handler for Review Mode.
# - ensure that "no items" entry is removed.
# - error correction when typing name of a list  (one method is below but needs
#       to cover both lowercase & upper; also injects at wrong time)
# - create an error printer and request errors from the error printer
# - save array/load arrays to a json file
# - ensure array content isn't lost when overwriting

# NICE TO HAVE features
# - web app component would be ideal.
# - a visualization would be killer

def initializer():
    print("hello!")
    print("do you want to view the current list, or add a new item?")


# set some vars

weeklyTasks = []
monthlyTasks = []
quarterlyTasks = []

addTo = "xxx"
theItem = ""
global theItem

# ----- imports -------
import string
import json
import random
# ---------------------


# print('addTo in globals, ' 'addTo' in globals())


#  ---- functions -------
def askInput():
    initInput = input("What next? ")
    getTimeframe(initInput)  # passes everything over for eval

def getTimeframe(text: object) -> object:  # follows up with a request for timeframe

  #  :rtype: object #what does this do?

    if "add" in text:  # where does it look for text var? - unanswered question
        timeframe = input("Where does this entry go? \n Weekly, Monthly or Quarterly?: ")
        evaluateInput(timeframe)  # sends the timeframe to evaluateInput
    if "review" in text:
        reviewMode()

# ==== modes ====

def reviewMode():
    print("welcome to Review Mode.")
    print("pick a list: weekly, monthly, or quarterly?")

    def getReviewMode(request: object) -> object:
        if "weekly" in request or "Weekly" in request:
            print("weekly list contains:")
            print(weeklyTasks)
        if "monthly" in request or "Monthly" in request:
            print("monthly list contains:")
            print(monthlyTasks)
        if "quarterly" in request or "Quarterly" in request:
            print("quarterly list contains:")
            print(quarterlyTasks)
            # need error handler for typos

        print("Here are your Lists:")
        print ("weekly list contains:")
        print(weeklyTasks)
        print ("monthly list contains:")
        print(monthlyTasks)
        print ("quarterly list contains:")
        print(quarterlyTasks)
        getReviewMode(input("pick a List: weekly, monthly, or quarterly."))


def evaluateInput(timeframe):
    # takes an item and checks its timeframe
    global addTo
    global theItem
    if timeframe == "Weekly" or timeframe == "weekly":
        addTo = "weeklyTasks"
        # next, ask for the item
        theItem = input('what is the item?')
        weeklyTasks.insert(0, theItem)
        printDestination()
        print(weeklyTasks)
        printDirections()
        askInput()

    if timeframe == "Monthly" or timeframe == "monthly":
        addTo = "monthlyTasks"
        theItem = input('what is the item?')
        monthlyTasks.insert(0, theItem)
        printDestination()
        print(monthlyTasks)
        printDirections()
        askInput()

    if timeframe == "Quarterly" or timeframe == "quarterly":
        addTo = "quarterlyTasks"
        theItem = input('what is the item?')
        quarterlyTasks.insert(0, theItem)
        printDestination()
        print(quarterlyTasks)
        printDirections()
        askInput()



    # check for mistakes to list name - need to adjust this
    # this was originally under evaluateInput - might need to stay there for flow control
    # if (timeframe != "Monthly") or (timeframe != "Weekly") or (timeframe != "Quarterly"):
    #     print("Sorry, I didn't get that. Please try again.")
    #     askInput()

def printDirections():
    print("Type 'go back' to go back to main menu. "
          "\n Type 'review' to enter Review mode. "
          "\n Type 'add' to add a new item.")

def printDestination():
    print("The item (" + theItem + ") will be added to " + addTo)
    print("the " + addTo + " list now contains:")  # good, this worked


# ===============
#    showtime
#     . . .
# ===============

initializer()
printDirections()
askInput()
