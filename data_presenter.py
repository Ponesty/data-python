import csv

print("\nPrinting each row:\n")
open_file = open("CupcakeInvoices.csv")

for cupcake in open_file:
    print(cupcake)

open_file.close()

print("\nPrinting each cupcake type:\n")
csv_file = open("CupcakeInvoices.csv")
for type in csv.reader(csv_file):
    print(type[2])

csv_file.close()
total = 0

print("\nTotal for each invoice:\n")
csv2_file = open("CupcakeInvoices.csv")
for sum in csv.reader(csv2_file):
    print(round(int(sum[3])*float(sum[4]),2))
    total += int(sum[3])*float(sum[4])

csv2_file.close()

print("The combined total is: ", round(total,2))