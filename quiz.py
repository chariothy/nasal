import csv
with open(r"./nasal_example.csv", encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)