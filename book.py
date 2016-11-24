

class Book ( object ):

    def __init__ ( self , title , author , patron=None ):
        """Constructor class - requires the title and author of the book.
        Optionally, the user can specify which patron checks out the book"""
        self._title = title
        self._author = author
        self._patron = patron
        self._waitlist = []         # note, this is a list of patron names
                                    # and not patron objects!
        self._checkedOut = False    # boolean to see if the book is rented



    def __str__ ( self ):
        """String representation of the book and author"""
        return self._title + " by " + self._author

    def getTitle ( self ):
        """Returns the title of the book"""
        return self._title
        
        
    def getAuthor ( self ):
        """Returns the author of the book"""
        return self._author
    
    
    def getPatron ( self ):
        """Returns the name of the patron who has checked out the book"""
        return self._patron.getName()
        
        
    def showWaitlist ( self ):
        """Show all patrons in the waiting list"""
        for item in self._waitlist:
            print item.getName()

    def checkout ( self , patron ):
        """Checking out the book, please pass the patron object as the
        parameter. This method will check to see if the patron can check it
        out. If not, add the patron's name to the waitlist"""

        # check to see if the book is already out
        if self.isCheckedOut():
            # add the patron to the waitlist, and print a message
            self._waitlist.append ( patron )
            print 'Book is checked out. ' + patron.getName() + \
                   ' is now on the waitlist for this book'
        else:
            # Here, the book is not out, so try to check it out to the
            # patron (supplied in the arguments of this method)
            if patron.getNumBooks() < 3: #If the patron has less than 3 books, the book is checked out to that patron and incrememts it
                patron.incBooks()
                self._patron = patron
                self._checkedOut = True
                print "This book is now checked out by " + patron.getName()
            else: #If the patron has 3 books already checked out, it prints that the patron can't have the book checked out
                print 'This patron has too many books checked out already' 


    def isCheckedOut ( self ):
        """Check to see if the book is already out"""
        return self._checkedOut
        

    def returnbook ( self ):
        """Return the book. Then, try to check it out to see if there is
        anyone else on the waitlist"""
        self._checkedOut = False
        self._patron.decBooks() #Decrements the book from the patron
        
        while True:
            #if the patron can check out books,checkout the book and break the loop
            #otherwise, keep looping
            if len(self._waitlist) > 0 :
                newPatron = self._waitlist.pop(0)
                if newPatron.getNumBooks() < 3:
                    self.checkout(newPatron)
                    break
            else:
                break # no reason to do this if there is no one on the list!


class Patron ( object ):

    BOOKLIMIT = 3
    
    def __init__ ( self , name  ):
        #Sets the number of books to 0 for each patron. Also, sets the name function as name for later use
        """Constructor"""
        self._name = name
        self._numBooks = 0

    def __str__ ( self ):
        #Shows the name of the patron and how many books that patron has checked out
        text = self._name + " has checked out " + \
               str(self._numBooks) + " books"
        return text

    def getName ( self ):
        #Returns the name of the patron
        return self._name

    def getNumBooks ( self ):
        #Returns the number 
        return self._numBooks

    def incBooks ( self ):
        #Increments the number of books that the patron now has
        if self._numBooks < Patron.BOOKLIMIT:
            self._numBooks += 1
        else:
            return 'Patron has reached his/her book limit'

    def decBooks ( self ):
        #Decrements the number of books that the patron now has
        if self._numBooks <= 0:
            return 'Patron has no books checked out'
        else:
            self._numBooks -= 1  
            
            
            
class Library ( object ):
    def __init__ ( self , name ):
        #Sets the name function as name. The patron and book list will be in a dictionary
        self._name = name
        self._patrons = {}
        self._books = {}
    
    def __str__ ( self ):
        text = "Library: " + self._name + '\n' + \
               "Books:   " + str(len(self._books)) + '\n' + \
               "Patrons: " + str(len(self._patrons))
        return text
    
    def addBook(self , book ):
        #Adds the book
        self._books[book.getTitle()] = book
        
    def removeBook(self, bookTitle):
        #Removes the book from the patron
        try:
            self._books.pop( bookTitle ) #Removes the book from the patrons info
        except Exception: #If the book isn't in the library, lets the user know the book couldn't be removed
            print 'Book not found in Library \"' + self._name + '\"'
        
    def findBook(self, bookTitle):
        #Lets the user to find a book
        try:
            return self._books[bookTitle]
        except Exception: #If the book isn't in the library, lets the user know the book couldn't be found
            print 'Book not found in Library \"' + self._name + '\"'
    
    def addPatron(self, patron ):
        #Adds a patron in the library
        self._patrons[patron.getName()] = patron
    
    def removePatron(self , patronName ):
        #Removes a patron from the library
        try:
            self._patrons.pop( patronName )
        except: #If no patron by that name isn't in the library, lets the user know that there is no one by that name
            print 'Patron not found in Library \"' + self._name + '\"'
    
    
    def findPatron(self , patronName):
        #Finds a certain patron
        try:
            return self._patrons[patronName]
        except Exception: #If no patron by that name isn't in the library, lets the user know that there is no one by that name
            print 'Patron not found in Library \"' + self._name + '\"'

    def listPatrons ( self ):
        #Lists all the patrons that are currently in the library
        return '\n'.join(map(str,self._patrons.values()))

    def listBooks ( self ):
        #Lists all the books that are currently in the library
        return '\n'.join(map(str,self._books.values()))

    def getName ( self ):
        """Simply returns the name of the Library"""
        return self._name
    
