class LibraryItem:
    def __init__(self, title):
        self.title = title

    def get_summary(self):
        """
        This method should be overridden by subclasses.
        """
        return f"Library item: {self.title}"

# Book class extends LibraryItem
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
        self.summary = ""

    def get_summary(self):
        return f"Book: '{self.title}' by {self.author}. Summary: {self.summary}"

    def set_summary(self, summary):
        self.summary = summary

# DVD class extends LibraryItem
class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title)
        self.director = director
        self.duration = duration  # in minutes

    def get_summary(self):
        return f"DVD: '{self.title}', directed by {self.director}, Duration: {self.duration} minutes."

# Magazine class extends LibraryItem
class Magazine(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number

    def get_summary(self):
        return f"Magazine: '{self.title}', Issue No. {self.issue_number}."

# Example usage
def main():
    book = Book('Game of Thrones', 'George R.R. Martin')
    book.set_summary('This book is about dragons & political drama.')

    dvd = DVD('Intelestelar', 'Christopher Nolan', 169)

    magazine = Magazine('National Geographic', 202)

    # Testing
    print(book.get_summary())
    print(dvd.get_summary())
    print(magazine.get_summary())

if __name__ == "__main__":
    main()
