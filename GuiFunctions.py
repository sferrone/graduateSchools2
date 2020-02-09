import csv

my_list=[]

f = open("Gradschools.csv",'r')
reader = csv.reader(f)
headers = next(reader, None)
print(headers)
for row in reader:
    for col in range(len(row)):
        print(row[col])
#my_list.append(row[col])
            
#print(my_list

def change_dropdown(*args):
    print(tkvar.get())
