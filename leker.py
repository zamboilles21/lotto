from os import system
import csv
system("cls")
file = open("otos.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()

multheti1 = str(rows[0]).split(";")
multheti2= str(rows[1]).split(";")

print(f"Múlt heti nyerőszámok: {multheti1[-5:]}")
print(f"Előző heti nyerőszámok: {multheti2[-5:]}")