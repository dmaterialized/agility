# AGILE Toolkit
# by DM Cook
# begun 2016.07.24
# version 0.3 - 12.3.2016

#  TODO
# - addTo doesn't get values added to it from the timeframe evaluator
# - need to store list items in an array
# - make sure that we handle "Go Back" being issued as first command
# - make sure we have method for printing any specific list at any time in the process.
# - make sure lowercase works as well as uppercase for specifying list names.
# - error correction when typing name of a list (otherwise it doesn't work right)
# - create an error printer and request errors from the error printer

# NICE TO HAVE

def initializer():
    print("hello!")
    print("do you want to view the current list, or add a new item?")


# set some vars

weeklyTasks = ['no items']
monthlyTasks = ['no items']
quarterlyTasks = ['no items']

addTo = "xxx"
theItem = ""
global theItem

import string

print('addTo in globals, ' 'addTo' in globals())


#  ---- functions -------
def reviewMode():
    print("welcome to Review Mode.")
    # more to come


def getTimeframe(text: object) -> object:  # follows up with a request for timeframe
    if "add" in text:  # where does it look for text var? - unanswered question
        timeframe = input("Where does this entry go? \n Weekly, Monthly or Quarterly?: ")
        evaluateInput(timeframe)  # sends the timeframe to evaluateInput

#
#
#
# print("Do you want to go back?")
#    else:
#        reviewMode()




# takes an item and checks its timeframe
def evaluateInput(timeframe):
    global addTo
    global theItem;
    if timeframe == "Weekly":
        addTo = "weeklyTasks"
        printDestination();
        weeklyTasks.insert(0, theItem)

    if timeframe == "Monthly":
        addTo = "monthlyTasks"
        monthlyTasks.insert(0, theItem)
        printDestination()
    if timeframe == "Quarterly":
        addTo = "quarterlyTasks"
        quarterlyTasks.insert(0, theItem)
        printDestination()
    # check for mistakes to list name
    if (timeframe != "Monthly") or (timeframe != "Weekly") or (timeframe != "Quarterly"):
        print("Sorry, I didn't get that. Please try again.")
        timeframe = input("Which list did you want? (Weekly, Monthly or Quarterly?)")
        evaluateInput(timeframe)
       #  doesn't work:
        # getTimeframe(text)

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


#############################

#############################

def printDirections():
    print(
        "Type 'go back' to go back to main menu. \n Type 'review' to enter Review mode. \n Type 'add' to add a new item.")


def printDestination():
    print("The item (" + theItem + ") will be added to " + addTo)
    # prints where something is going
    print("the " + addTo + " list now contains:")  # good, this worked
    print(weeklyTasks)  # good, this worked (but the method to push doesn't work)
    # end print destination


# Review phase needs to be set up


# ===============
#    showtime
#     . . .
# ===============

initializer()
printDirections()
initInput = input("What next? ")
getTimeframe(initInput)  # passes everything over for eval
printDestination()
