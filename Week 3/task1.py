import csv
from openpyxl import Workbook


wb = Workbook()
ws = wb.active


with open("input.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        ws.append(row)


wb.save("output.xlsx")

print("CSV converted to Excel successfully")