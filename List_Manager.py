"""
Welcome to -List Manager- (2017)

This program was created to manage lists in a variety of ways.

All code created by Mabdo (Under Kebabdo Inc) is public, and free to use
and edit. No credits are required.
"""

# Note, Sufficient comments are not present in this code.

#==============================================================================#
import time, random, sys
#==============================================================================#
# Constants defined here
defaultList = ["zebra", "rhino", "kangaroo", "fox", "cat", "bear", "ant","snake","mouse","mabdo"]
globalList = defaultList # List which will be accessed as global var.
globalLimit = 10 # Maximum size of the list (Static)
globalWatch = False
#==============================================================================#
# Delay made easier to call through short function
def delay():
    time.sleep(1.5) # Pauses the interpretor for 1500ms
    return # Returns empty

class Disp:
    def display1():
        print("\n=============================================================")
        return
    def display2():
        print ("\n------------------------------------------------------------")
        return
#==============================================================================#
# The main class where the accessing occurs
class Main:
    def __init__(self):
        global globalList # Global list declared in function
        self.lis = globalList # List stored in var.
        """Main program loop"""
        loop = True
        while loop:
            Disp.display1()
            print ("\nYour current list is:", str(self.lis))
            delay()
            print ("\n~Would you like to Search, Sort or Edit a list?~")
            In = input ("Search [s]\nSort [o]\nEdit [e]")
            In = In.lower()
            if (In == "search") or (In == "s"):
                self.searches()
            elif (In == "sort") or (In == "o"):
                self.sorts()
            elif (In == "edit") or (In == "e"):
                self.editting()
    #--------------------------------------------------------------------------#
    # Access to Searches
    def searches(self):
        print ("\n~What search would you like to perform on your list?~")
        In = input("Linear[l]\nBinary[b]")
        In == In.lower()
        if (In == "linear") or (In == "l"):
            delay()
            LinearSearch()
        if (In == "binary") or (In == "b"):
            delay()
            BinarySearch()
    #--------------------------------------------------------------------------#
    # Access to Sorts
    def sorts(self):
        global globalWatch
        print ("\n~Would you like to watch your sort?")
        In = input("Yes[y]\nNo[n]")
        In == In.lower()
        if (In == "yes") or (In == "y"):
            print ("\nApplying optimisation...")
            delay()
            globalWatch = True
        else:
            pass
        print ("\n~What sort would you like to perform on your list?~")
        In = input("Bubble[b]\nInsertion[i]\nMerge[m]\nQuick[q]\nCocktail[c]\nBogo[g]")
        In == In.lower()
        if (In == "bubble") or (In == "b"):
            print ("\nPerforming Bubble sort...")
            delay()
            BubbleSort()
        elif (In == "insertion") or (In == "i"):
            print ("\nPerforming Insertion sort...")
            delay()
            InsertionSort()
        elif (In == "merge") or (In == "m"):
            print ("\nPerforming Merge sort...")
            delay()
            MergeSort()
        elif (In == "quick") or (In == "q"):
            print ("\nPerforming Quick sort...")
            delay()
            QuickSort()
        elif (In == "cocktail") or (In == "c"):
            print ("\nPerforming Cocktail sort...")
            delay()
            CocktailSort()
        elif (In == "bogo") or (In == "g"):
            print ("\nPerforming Bogo sort...")
            delay()
            BogoSort()
    #--------------------------------------------------------------------------#
    # Access to Array Types
    def editting(self):
        print ("\n~Stack format, Queue format or Empty list?~")
        In = input ("Stack[s]\nQueue[q]\nMix[m]\nEmpty[e]")
        if (In == "stack") or (In == "s"):
            print ("\nCompiling into Stack format...")
            delay()
            Stack()
        elif (In == "queue") or (In == "q"):
            print ("\nCompiling into Queue format...")
            delay()
            # Creating an instance of Queue class
            Queue()
        elif (In == "Mix") or (In == "m"):
            print ("\nShuffling the list...")
            delay()
            random.shuffle(self.lis)
        elif (In == "empty") or (In == "e"):
            print ("\nResetting list...")
            delay()
            self.lis.clear()
#==============================================================================#
# Class for Queue formatting
class Queue():
    def __init__(self):
        global globalList
        self.queue = globalList
        global globalLimit
        self.maxLength = globalLimit
        self.start()

    def add(self, value):
        if self.endPointer >= self.maxLength:
            print ("\nQueue is Full!")
        else:
            print ("\nAdding item:", value)
            self.queue.append(value)
        delay()
        return

    def remove(self):
        if len(self.queue) < 0:
            print ("\nQueue is Empty!")
        else:
            print ("\nRemoving item...")
            self.queue.pop(0)
        delay()
        return

    def start(self):
        loop = True
        while loop:
            self.endPointer = len(self.queue)
            print ("\n<Head>",self.queue,"<Tail>")
            delay
            print ("\n~Add or Remove values in the queue?~")
            In = input ("Add [e]\nRemove [r]\nEnd Editting [e]")
            In = In.lower()
            if (In == "add") or (In == "a"):
                v = input ("Input a value to add...")
                self.add(v)
            elif (In == "remove") or (In == "r"):
                self.remove()
            elif (In == "end") or (In == "e"):
                loop = False
        print ("\nReturning to menu...")
        delay()
        return
#==============================================================================#
# Class for Stack formatting
class Stack:
    def __init__(self):
        global globalList
        self.stack = globalList
        global globalLimit
        self.maxLength = globalLimit
        self.start()

    def add(self, value):
        if self.endPointer >= self.maxLength:
            print("\Stack is full!")
        else:
            print ("\nAdding item:" + str(value))
            self.stack.append(value)
        delay()
        return

    def remove(self):
        if self.endPointer < 0:
            print("\nStack is empty!")
        else:
            print ("\nRemoving item...")
            self.stack.pop()
        delay()
        return

    def start(self):
        loop = True
        while loop:
            self.endPointer = len(self.stack)
            print ("\n",self.stack,"<Head>")
            delay
            print ("\n~Add or Remove values in the stack?~")
            In = input ("Add [e]\nRemove [r]\nEnd Editting [e]")
            In = In.lower()
            if (In == "add") or (In == "a"):
                v = input ("Input a value to add...")
                self.add(v)
            elif (In == "remove") or (In == "r"):
                self.remove()
            elif (In == "end") or (In == "e"):
                loop = False
        print ("\nReturning to menu...")
        delay()
        return
#==============================================================================#
# Class for Linear/Serial search
class LinearSearch:
    def __init__(self):
        global globalList
        self.searchList = globalList
        print("\nList of items is:"+ str(self.searchList))
        itemToFind = input("Enter item to search for:")
        self.found = 0
        self.index = self.found
        while self.index < len(self.searchList):
        	if self.searchList[self.index] == itemToFind:
        		self.found = 1
        		break
        	self.index = self.index + 1
        print ("\nSearching...")
        delay()
        if self.found == 1:
        	print("\nItem found in list at position:", self.index + 1)
        else:
       	    print("\nItem not found in this list :[")
        delay()
        return
#==============================================================================#
# Class for Binary search
class BinarySearch:
    def __init__(self):
        global globalList # Makes use of the global variable that holds
        self.searchList = globalList
        print("\nList of items is:"+ str(self.searchList))
        self.itemToFind = input("Enter item to search for:")
        self.lower = 0
        self.upper = len(self.searchList)
        while self.lower < self.upper:   # use < instead of <=
            self.midpoint = self.lower + (self.upper - self.lower) // 2
            val = self.searchList[self.midpoint]
            if self.itemToFind == val:
                print ("Searching...")
                delay()
                print ("\nItem found in list at position:", str(self.midpoint + 1))
                return
            elif self.itemToFind > val:
                if self.lower == self.midpoint:
                    break
                self.lower = self.midpoint
            elif self.itemToFind < val:
                self.upper = self.midpoint
        print ("\nItem not found in this list :[")
        delay()
        return
#==============================================================================#
# Class for Bubble sort
class BubbleSort:
    def __init__(self):
        global globalList
        self.sortArray = globalList
        swapped = True
        while swapped == True:
            swapped = False
            for pointer in range(0, len(self.sortArray)-1):
                if self.sortArray [pointer] > self.sortArray [pointer + 1]:
                    temp = self.sortArray[pointer]
                    self.sortArray [pointer] = self.sortArray[pointer + 1]
                    self.sortArray [pointer + 1] = temp
                    swapped = True
                    global globalWatch
                    if globalWatch:
                        print(self.sortArray)
                        time.sleep(0.1)
        print ("\nYour list is sorted :]")
        return
#==============================================================================#
# Class for Insertion sort
class InsertionSort:
    def __init__(self):
        # Brings global list into the class and stores it in a local variable
        global globalList
        self.sortArray = globalList
        # Loops until every itme in list
        for index in range(1, len(self.sortArray)):
            # The current item is at list index
            itemAtIndex = self.sortArray[index] # [x, A(), B(Index)]
            # Assigns index to value before the current item
            leftItemIndex = index - 1 # [x, A(L.Index), B(Index)]
            # Checks index is 0 or bigger & that item is smaller than previous
            while leftItemIndex >= 0 and itemAtIndex < self.sortArray[leftItemIndex]:
                    # Item at previous shifts to right and takes place of item
                    self.sortArray[leftItemIndex +1] = self.sortArray[leftItemIndex] # [x, -(L.Index), A(Index)]
                    # Left index moves back to do further check on item
                    leftItemIndex -= 1 # [x(L.Index), -, A(Index)]
            # Makes the empty spot become what the original item was, swap!
            self.sortArray[leftItemIndex + 1] = itemAtIndex # [x(L.Index), -(itemAtIndex), A(Index)]
            # Checks if the user wanted to view the sort
            global globalWatch
            if globalWatch == True:
                print (self.sortArray)
                time.sleep(0.1)
        print ("\nYour list is sorted :)")
        return
#==============================================================================#
# Class for Merge sort
class MergeSort:
    def __init__(self):
        global globalList # Brings global list
        # Feeds the merge sort function with the list & stores it in var.
        sortedList = self.mergesort(globalList)
        print ("\nYour list is sorted")

    def mergesort(self, unsorted): # Takes in the list
        global globalWatch # Brings global watch var.
        # Checks if the list has less than 1 item
        if len(unsorted) <= 1:
            return unsorted # Returns the list as it will already be sorted
        else:
            # Finds the midpoint of the unsorted list
            middle = len(unsorted) // 2
            # Checks global watch for true and prints the midpoint to the user
            if globalWatch:
                print ("\nCurrent midpoint value:",unsorted[middle])
            # Adds the items to the left of the midpoint in list A
            listA = self.mergesort(unsorted[:middle])
            # Same for list B but to the right of the midpoint
            listB = self.mergesort(unsorted[middle:])
            # Client relay which shows the list contents for every partition
            if globalWatch:
                print ("Partition list A:", listA,"\nPartition list B:", listB,"\n")
            time.sleep(0.5)
            # Runs the merge function on the two lists and returns the list
            return self.merge(listA,listB) #

    def merge(self, listA, listB): #merge is defined
        mergedList = [] # creates a merge list where the elements can be placed in

        while len(listA) != 0 and len(listB) != 0:
            if listA[0] < listB[0]: # checks to see if the value in list A is smaller than the element in list B
                mergedList.append(listA[0]) #if it is, it will move the element from list A to the merge list
                listA.remove(listA[0]) #it then removes this element from list A because it cant stay in both lists
            else:
                mergedList.append(listB[0])
                listB.remove(listB[0]) # it then removes this element from list B
            global globalWatch
            if globalWatch:
                print ("Current merged List:",mergedList)
                time.sleep(0.2)

        if len(listA) == 0:
            mergedList += listB
        else:
            mergedList += listA
        return mergedList
#==============================================================================#
# Class for Quick sort
class QuickSort:
    def __init__(self):
        global globalList
        alist = globalList
        print (alist)
        start = 0
        end = len(alist)-1
        sort = self.quicksort(alist, start, end)
        print ("\nYour list is sorted :}")

    def partition(self, alist, start, end):
        pivot = alist[start]
        left = start +1
        right = end
        done = False
        global globalWatch
        if globalWatch:
            print ("\nCurrent List Partition:",alist,"\nPivot:",pivot,"\nLeft",alist[left],"Right",alist[right])
            time.sleep(0.2)
        while done == False:
            while left <= right and alist[left] <= pivot:
                left = left +1
            while alist[right] >= pivot and right >= left:
                right = right -1

            if right < left:
                done = True
            else:
                temp = alist[left]
                alist[left] = alist[right]
                alist[right] = temp

        temp = alist[start]
        alist[start] = alist[right]
        alist[right] = temp
        return right

    def quicksort(self, alist, start, end):
        if start < end:
            split = self.partition(alist, start, end)
            self.quicksort (alist, start, split-1)
            self.quicksort (alist, split+1, end)
        return alist
#==============================================================================#
# Class for Cocktail sort
class CocktailSort:
    def __init__(self):
        global globalList
        a = globalList
        n = len(a)
        swapped = True
        start = 0
        end = n-1
        while (swapped == True):
            swapped = False
            for i in range (start, end):
                if (a[i] > a[i + 1]) :
                    a[i], a[i + 1]= a[i + 1], a[i]
                    swapped = True
            if (swapped == False):
                break
            print ("\nRight run (->",a,")")
            swapped = False
            end = end-1
            for i in range(end-1, start-1, -1):
                if (a[i] > a[i + 1]):
                    a[i], a[i + 1] = a[i + 1], a[i]
                    swapped = True
            start = start + 1
            print ("Left run (",a,"<-)")
            time.sleep(0.5)
        return
#==============================================================================#
# Class for Bogo sort
class BogoSort:
    def __init__(self):
        global globalList
        self.sortArray = globalList
        random.seed()
        self.tries = 0
        self.timer = time.time()
        self.sortArray = self.bogo()
        global globalWatch
        if globalWatch:
            print ("\nBogo sort went through:", str(self.tries) ,"attempts")
            print ("This took your CPU %.2f seconds" % (time.time() - self.timer))
            delay()
        print ("\nYour list is sorted :>")
        return

    def ordered(self):
        i = 0
        j = len(self.sortArray)
        while i + 1 < j:
            if self.sortArray[i] > self.sortArray[i + 1]:
                return False
            i += 1
        return True

    def bogo(self):
        while not self.ordered():
            random.shuffle(self.sortArray)
            self.tries += 1
        return self.sortArray
#==============================================================================#
# List settings

def start():
    Disp.display1()
    print ("~Would you like to use a default list or your own~")
    In = input ("Default[d]\nOwn[o]")
    In = In.lower()
    if (In == "default") or(In == "d"):
        pass
    elif (In == "own") or (In == "o"):
        defaultList.clear()
        loop = True
        while loop:
            Disp.display2()
            print ("Your current list is:", defaultList)
            print ("~Enter values or press enter to end~")
            value = input ("Enter value")
            value = value.lower()
            if (value == ""):
                loop = False
            elif len(defaultList) >= globalLimit:
                print ("\nYour list is currently full!")
                delay()
            else:
                defaultList.append(value)
        return
#==============================================================================#
# Starts program
start()
Main()

