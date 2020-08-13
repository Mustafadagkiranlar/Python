import csv

def read_data():

    global paper_id

    with open('data.csv') as data:
        data_reader = csv.reader(data) #use DictReader for list the used headers.
        for row in data_reader:
            paper_id = int(row[0])

def data_writer():
    global paper_id
    paper_id +=1
    with open('data.csv', 'w') as data:
        data_writer = csv.writer(data)
        data_writer.writerow({paper_id})

read_data()
data_writer()
