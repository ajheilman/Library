from book import *

class Manager ( object ):
    def __init__ ( self, libraryName ):
        """Constructor for the Manager class"""

        # set up instance variables
        self._library = Library( libraryName )
        
        print self._library.getName() + " Library Manager" #Creates the name of the library
        print self.drawSep() #The equal signs appear
        while True:
            print self.drawMenu() #Shows the user the menu
            print "Please enter a selection:"
            try:
                sel = input ( "@  " )
                if sel == 11:    # end the program
                    print "Program ending"
                    break

                elif sel == 1:  # add a new patron
                    self.createPatron()

                elif sel == 2:  # remove a patron
                    self.removePatron()

                elif sel == 3:  # list all patrons
                    self.listPatrons()

                elif sel == 4:  # Add a book
                    self.createBook()

                elif sel == 5:  # Remove a book
                    self.removeBook()

                elif sel == 6:  # list all books
                    self.listBooks()

                elif sel == 7:  # check out a book
                    self.checkout()

                elif sel == 8:  # return a book
                    self.returnbook()

                elif sel == 9:  # find book info
                    self.bookInfo()

                elif sel == 10: # get patron info
                    self.patronInfo()


                else: #If the user enters a number that isn't in the menu, lets the user know that the program is ending
                    print "Bad input. Program ending"
                    break #Breaks the loop
            except Exception:
                print "Bad selection, try again"

            
            # print the separator after each loop through
            print self.drawSep()
            

    def createLibrary ( self , name ):
        return Library ( name ) #Returns the name of the library

    def drawSep ( self ):
        return "=================================" #No real use. Just to make the menu more organzied when the user uses the library

    def drawMenu ( self ):
        #Prints the menu
        print "MAIN MENU"
        print self.drawSep() #The equal signs appear
        text  = "1.  Add a new patron\n"
        text += "2.  Remove a patron\n"
        text += "3.  List all patrons\n"
        text += "4.  Add a new book\n"
        text += "5.  Remove a book\n"
        text += "6.  List all books\n"
        text += "7.  Check out a book\n"
        text += "8.  Return a book\n"
        text += "9.  Get book information\n"
        text += "10. Get patron information\n"
        text += "11. Exit the library manager\n"
        return text

    def createPatron ( self ):
        #This function lets the user create new patrons in the library so that they can check out and returns books
        print self.drawSep() #The equal signs appear
        print "Add a new patron"
        try:
            name = raw_input ( "Patron Name@  " ) #User types in name of patron
            if not name:
                raise Exception()
            self._library.addPatron( Patron ( name ) ) #Adds the patron to the library
            print 'Patron added' #Confirms that the patron is in the library
            print '\n'
        except Exception:
            print '\n'

    def listPatrons ( self ):
        #List all the patrons that are currently in the library
        print self.drawSep() #The equal signs appear
        print "List all patrons"
        print self._library.listPatrons() #Lists all of the patrons in the library
        print '\n'

    def removePatron( self ):
        #This function has the option to remove any patron from the library
        print self.drawSep() #The equal signs appear
        print "Remove a patron"
        try:
            name = raw_input ( "Patron Name@  " )
            if not name:
                raise Exception()   # generic exception
            self._library.removePatron ( name ) #Removes the patron
            print "Patron removed."
            print '\n'
        except Exception:
            print 'Patron could not be removed.' #If the user types a name that isn't a patron, lets the user know that the patron couldn't be removed
            print '\n'

    def createBook ( self ):
        #This function creates a new book in the library
        print self.drawSep() #The equal signs appear
        print "Add a book"
        try:
            title  = raw_input ( "Book Title @  " ) #User types in the name of the book
            if not title: #If the name of the book isn't in the library, it lets the user the book isn't in the library
                raise Exception()
            try:
                author = raw_input ( "Book Author@  " ) #User types in the name of the author
                if not author: #If an author's name isn't in the library, it lets the user the author isn't in the library
                    raise Exception()   # generic exception, caught below
                self._library.addBook ( Book ( title , author) ) #Adds the title and author of the book in the library
                print '\n'
            except Exception:
                print 'Error creating book (bad author name)' #If for some reason there is a problem with the author's name, lets the user know something is wrong
                print '\n'
        except Exception:
            print 'Error creating book (bad title)' #If for some reason there is a problem with the book title, lets the user know something is wrong
            print '\n'

    def removeBook ( self ):
        #This function removes a book from the library
        print self.drawSep() #The equal signs appear
        print "Remove a book"
        try:
            title = raw_input ( "Book Title@  " ) #User types in the name of the book
            if not title: #If the name of the book isn't in the library, it lets the user the book isn't in the library
                raise Exception()
            self._library.removeBook(title) #Removes the book
            print '\n'
        except Exception:
            print 'Cannot remove book' #If there is no book by the title the user typed, lets the user know the book couldn't be removed
            print '\n'

    def listBooks ( self ):
        #This function lists all the books in the library
        print self.drawSep() #The equal signs appear
        print "List all books"
        print self._library.listBooks() #Lists all books in the library
        print '\n'

    def checkout ( self ):
        #This function lets a patron check out a book
        print self.drawSep() #The equal signs appear
        print "Check out book"
        try:
            book   = self._library.findBook   ( raw_input ( "Book Title @  " )) #User types in the book title
            try:
                patron = self._library.findPatron ( raw_input ( "Patron Name@  " )) #User types in the name of the patron that wants to checkout a book
                book.checkout ( patron ) #User checks out the book, unless it has 3 books already
                print '\n'
            except Exception:
                print '\n'
        except Exception:
            print '\n'

    def bookInfo ( self ):
        #This function shows if a certain book is checked out, if it is it tells us who checked it out and if any people are on the waitlist
        print self.drawSep() #The equal signs appear
        print "Book info"
        try:
            book = self._library.findBook ( raw_input ( "Book Title@  " ) ) #Asks the user for the name of the book
            print book
            if book.isCheckedOut():
                print "This book is checked out by " + book.getPatron() #Tells us who checked it out if someone did
                print 'People on waitlist\n'
                book.showWaitlist() #Shows the waitlist if anyone is, if not it shows nothing
        except Exception:
            print '\n'

    def returnbook  (self ):
        #This function lets the user return a book
        print self.drawSep() #The equal signs appear
        print "Return a book"
        book = self._library.findBook ( raw_input ( "Book Title@  " ) ) #Asks for the title so it can be returned
        book.returnbook() #Returns the book
        print '\n'

    def patronInfo ( self ):
        #This function show the patron's info by showing how many books the patron is checked out
        print self.drawSep() #The equal signs appear
        print "Patron information"
        try:
            patron = self._library.findPatron ( raw_input ( "Patron Name@  " ) ) #User types in the name of the patron to see their info
            print patron #Prints out if that patron has any books checked out and how many
        except Exception:
            print '\n'
