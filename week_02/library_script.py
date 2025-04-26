class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.summary = ""
            
    def get_summary(self):
        """
            This method prints the summary of the book or the book info
        """
        
        return self.summary
        
    def set_summary(self, summary):
        """
            This method set the book summary after it gets instanciated
        """    
        self.summary = summary
        


def main():
    new_book = Book('Game of thrones', 'Jorge R R Martin')
    new_book.set_summary('This book is about dragons & stuff')
    summ = new_book.get_summary()
    print(summ)
    
if __name__ == "__main__":
    main()