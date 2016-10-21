# AGILE Toolkit
# by DM Cook
# begun 2016.07.24
# version 0.2

#  TODO
# - addTo doesn't get values added to it from the timeframe evaluator
# - need to store list items in an array
# - make sure that we handle "Go Back" being issued as first command
# - make sure we have method for printing any specific list at any time in the process.
# - make sure lowercase works as well as uppercase for specifying list names.


# NICE TO HAVE
# - systemwide indicator of current list and current active item
# - systemwide monitor for a help key.

def initializer():
    print("hello!")
    print("do you want to view the current list, or add a new item?")


# set some vars

weeklyTasks = []
monthlyTasks = []
quarterlyTasks = []
global addTo
addTo = "xxx"
global addedItem
import string


#  ---- functions -------

def getResponse(text):  # follows up with a request for timeframe
    if "add" in text:
        timeframe = input("Where does this entry go? \n Weekly, Monthly or Quarterly?: ")
        evaluateInput(timeframe)  # sends the timeframe to evaluateInput
    #need additional options to handle other modes (review, etc.)
    if "review" in text:
        reviewMode()
    if "go back" in text:
        print("Going back to the beginning now.")
        initInput=input("what should I do?")

# adds an item to a list
def addAnItem(list):
    global addedItem
    addedItem = input('what is the item?')
    # figure out which list gets appended to
    if list == weeklyTasks:
        weeklyTasks.insert(0, addedItem)

    if list == monthlyTasks:
        monthlyTasks.insert(0,addedItem)

    if list == quarterlyTasks:
        quarterlyTasks.insert(0,addedItem)


# takes an item and checks its timeframe
def evaluateInput(timeframe):
    global addTo
    if timeframe == "Weekly":
        addTo = "weeklyTasks"
        addAnItem(weeklyTasks)
        printDestination()
        print(weeklyTasks)

    if timeframe == "Monthly":
        addTo = "monthlyTasks"
        addAnItem(monthlyTasks)
        printDestination()
        print(monthlyTasks)

    if timeframe == "Quarterly":
        addTo = "quarterlyTasks"
        addAnItem(quarterlyTasks)
        printDestination()
        print(quarterlyTasks)
    else:
        print('sorry, didn\'t get that. try again?')
        global addedItem
        addAnItem(addTo)


    # this doesn't work right - error catch happens but then process exits


        # next, ask for the item
    # def askForItem():
    #     theItem = input('what is the item?')

    # how to call a list by a variable name?
    # so far, tried
    # addTo.insert(0, theItem)
    # weeklytasks.append(theItem)
    # print(addTo)
    # def askForItem(theItem):
    #     addTo.push(theItem)
    #     print(addTo)


#############################

#############################

def printDirections():
    print(
        "Type 'go back' to go back to main menu. \n Type "
        "'review' to enter Review mode. "
        "\n Type 'add' to add a new item.")





# def getActiveList(activeList):
#     activeList =

def goBack():
    printDirections()
    initInput = input("What next? ")
    getResponse(initInput)  # passes everything over for eval

def printDestination():
    # prints where something is going
    global addedItem
    global addTo
    print("The item %s will be added to %s" % (addedItem, addTo))
    print("the %s list now contains:" % (addTo))
    goBack()


def reviewMode():
    # Review phase needs to be set up
    print("welcome to Review Mode.")
    print("here is what is on the weekly list: \n"
          "%s " % (weeklyTasks))
    print("here is what is on the monthly list: \n"
          "%s" % (monthlyTasks))
    print("here is what is on the quarterly list: \n"
          "%s" % (quarterlyTasks))
    # more to come

# ===============
#    showtime
#     . . .
# ===============

initializer()
printDirections()
initInput = input("What next? ")
getResponse(initInput)  # passes everything over for eval
