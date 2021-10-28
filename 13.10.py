class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date

    def print_info(self):
        print("Book Information: ")
        print("    Book Title: ", self.title)
        print("    Author: ", self.author)
        print("    Publisher: ", self.publisher)
        print("    Publication Date: ", self.publication_date)

class Encyclopedia(Book):
    def __init__(self, title, author, publisher, publication_date, edition, num_volumes):
        Book.__init__(self, title, author, publisher, publication_date)
        self.edition = edition
        self.num_volumes = num_volumes

    def print_info(self):
        print("Book Information: ")
        print("    Book Title: ", self.title)
        print("    Author: ", self.author)
        print("    Publisher: ", self.publisher)
        print("    Publication Date: ", self.publication_date)
        print("    Edition: ", self.edition)
        print("    Number of Volumes: ", self.num_volumes)


if __name__ == "__main__":
    title = input("Input the title of the book: ")
    author = input("Input the author name: ")
    publisher = input("Input the pubisher: ")
    publication_date = input("Input the publication date: ")

    e_title = input("Input the title of the encyclopedia: ")
    e_author = input("Input the author name: ")
    e_publisher = input("Input the pubisher: ")
    e_publication_date = input("Input the publication date: ")
    edition = input("Input the edition: ")
    num_volume = input("input the number of volumes: ")

    my_book = Book(title, author, publisher, publication_date)
    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_volume)

    my_book.print_info()
    my_encyclopedia.print_info()
