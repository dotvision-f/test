import csv

class Book_DB:

    def __init__(self, header: list, book: list):
        self.book = book
        self.header = ['title', 'author', 'book_id', 'subject', 'number_of_page', 'number_of_book']

    def init_db(self, path):    #optional function (just to denote the name of a column)
        path = path
        with open(path, 'w', encoding = 'UTF8') as a:
            writer = csv.writer(a)
            writer.writerow(self.header)
            a.close()

    def add_book(self, book, path):
        book = self.book
        path = path
        with open(path, 'w', encoding = 'UTF8') as a:
            #open csv file
            writer = csv.writer(a)

            #write to the csv
            writer.writerow(book)

            #close the csv
            a.close()

        def get_info(self, path):
            header = []
            data = []
            with open(path, 'r') as a:
                # create csv reading object
                csvreader = csv.reader(a)

                # extracting header
                header = next(csvreader)

                # extracting data rows
                for row in csvreader:
                    data.append(row)

                # number of rows
                print("Number of books: %d" % (csvreader.line_num))

                print("Header: " + ",".join(i for i in header))

                for b in data[:]:
                    for col in b:
                        print("%10s" % col)
                        print("\n")