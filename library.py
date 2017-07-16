class Library (object):
    def __init__ (self, name):
        #Sets the name function as name. The patron and book list will be in a dictionary
        self._name = name
        self._patrons = {}
        self._books = {}
    
    def __str__ (self):
        text = "Library: " + self._name + '\n' + \
               "Books:   " + str(len(self._books)) + '\n' + \
               "Patrons: " + str(len(self._patrons))
        return text
    
    def addBook(self , book):
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
    
    def addPatron(self, patron):
        #Adds a patron in the library
        self._patrons[patron.getName()] = patron
    
    def removePatron(self, patronName):
        #Removes a patron from the library
        try:
            self._patrons.pop(patronName)
        except: #If no patron by that name isn't in the library, lets the user know that there is no one by that name
            print 'Patron not found in Library \"' + self._name + '\"'
    
    
    def findPatron(self, patronName):
        #Finds a certain patron
        try:
            return self._patrons[patronName]
        except Exception: #If no patron by that name isn't in the library, lets the user know that there is no one by that name
            print 'Patron not found in Library \"' + self._name + '\"'

    def listPatrons (self):
        #Lists all the patrons that are currently in the library
        return '\n'.join(map(str,self._patrons.values()))

    def listBooks (self):
        #Lists all the books that are currently in the library
        return '\n'.join(map(str,self._books.values()))

    def getName (self):
        """Simply returns the name of the Library"""
        return self._name
