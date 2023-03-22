import csv

class Member_DB:

    def __init__(self, header: list, mem: list):
        self.mem = mem
        self.header = ['name', 'email', 'password', 'phone number', 'status', 'level']

    def init_db(self, path):    #optional function (just to denote the name of a column)
        path = path
        with open(path, 'w', encoding = 'UTF8') as a:
            writer = csv.writer(a)
            writer.writerow(self.header)
            a.close()

    def add_book(self, mem, path):
        mem = self.mem
        path = path
        with open(path, 'w', encoding = 'UTF8') as a:
            #open csv file
            writer = csv.writer(a)

            #write to the csv
            writer.writerow(mem)

            #close the csv
            a.close()

    def get_info(self, path):
        header = []
        data = []
        with open(path, 'r') as a:
            #create csv reading object
            csvreader = csv.reader(a)

            #extracting header
            header = next(csvreader)

            #extracting data rows
            for row in csvreader:
                data.append(row)

            #number of rows
            print("Number of members: %d"%(csvreader.line_num))

            print("Header: " + ",".join(i for i in header))

            for b in data[:]:
                for col in b:
                    print("%10s"%col)
                    print("\n")