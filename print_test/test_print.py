from escpos.printer import Usb
from datetime import datetime
import csv

current_date = datetime.now()

with open('data.csv') as data:
    data_reader = csv.reader(data) #use DictReader for list the used headers.
    for row in data_reader:
        paper_id = int(row[0])

p = Usb(0x0fe6, 0x811e,timeout=0)#vendor id product id us lsusb to see

p.set(align="center", height=2)
p.text("AlSANCAK BELEDIYESI")
p.text("\nAKILLI COP TOPLAMA TERMINALI\n\n")


p.set(align="left", height=1, text_type='bold')
p.text("\nFIS NO:    ")
p.text(str(paper_id))
p.text("\nTARIH:     ")

p.text(str(current_date.strftime("%d-%m-%Y %H:%M")))

p.text("\n\nCOP CINSI\n\n")
p.text("METAL:       ")
p.text("2\n")
p.text("PLASTIK:     ")
p.text("3\n")
p.text("CAM:         ")
p.text("5\n")
p.text("KARTON:      ")
p.text("9\n\n")

p.text("PUAN:        ")
p.text("55")
p.cut()

paper_id +=1
with open('data.csv', 'w') as data:
    data_writer = csv.writer(data)
    data_writer.writerow({paper_id})
    print(paper_id)