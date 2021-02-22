"""
    NOTE: File already has extensions implemented.
"""
import csv

class Comparator():
    def __init__(self, reader_in, writer_out):
        self.in_reader = reader_in
        self.out_writer = writer_out
        self.data_in = []

    def parse_info(self):
        for line in self.in_reader:
            self.data_in.append([])
            for data in line:
                if data == line[0]:
                    self.data_in[-1].append(data)
                elif data == "":
                    continue
                else:
                    self.data_in[-1].append(float(data))

    def calculate_ratio(self, row):
        ratios = []
        for index in range(2,len(row), 2):
            if index == 0:
                continue
            ratios.append(round(float(row[index]/row[index-1]), 2))
        return ratios

    def select_deal(self, ratios):
        answer = 65
        best = ratios[0]
        #this is the equivalent of using the min() function
        #The min() function doesn't work well with floats when
        #there is a floating-point comparison. This is why
        #the functionality was implemented manually
        for index in range(1,len(ratios)):
            if ratios[index] < best:
                best = ratios[index]
                answer = 65+index
        return chr(answer) #returns unicode character based on int

    def write_data(self, data):
        self.out_writer.writerow(data)

    def run(self): #Notice this code is exactly the same as last week's
        self.parse_info()
        for row in self.data_in:
            out_data = []
            out_data.append(row[0])
            temp = self.calculate_ratio(row)
            out_data.extend(temp)
            out_data.append(self.select_deal(temp))
            self.write_data(out_data)         

def main():
    #used a compound with statement.
    #It is the same as nesting it
    with open("price_list.csv", "r", newline="") as ifile,\
         open("price_output.csv", "w", newline="") as ofile:
        r_obj = csv.reader(ifile)
        w_obj = csv.writer(ofile)
        comp = Comparator(r_obj, w_obj)
        comp.run()
        
if __name__ == "__main__":
    main()
