import csv
from datetime import datetime

input_file = "Sample - Superstore.csv"
output_file = "Superstore_Clean.csv"

with open(input_file, "r", newline="", encoding="latin-1") as infile,  \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        # Convert Order Date
        row[2] = datetime.strptime(row[2], "%m/%d/%Y").strftime("%Y-%m-%d")

        # Convert Ship Date
        row[3] = datetime.strptime(row[3], "%m/%d/%Y").strftime("%Y-%m-%d")

        writer.writerow(row)

print("Dates converted successfully!")
print("New file created:", output_file)