from book import *
from manager import *

def main():
    try:
        #Asks the user for the name of the library
        libraryName = raw_input ( "Please enter the name of the Library@  " )
        
        if not libraryName:
            raise BadName
        lib = Manager(libraryName)
        
        #This appears when the user exits the library menu
        print '\nThis program brought to you by Ashley and Casey. Thanks! :)'
    except Exception:
        print 'There was a problem somewhere!'
        
main()
