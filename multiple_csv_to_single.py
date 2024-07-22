import csv
import re

rows_to_write = []

center = ""

center_arr = []
serial_number = []
marks = []
center_name = []


def is_number(s):
    pattern = r"^-?\d+(\.\d+)?$"
    return bool(re.match(pattern, s))


with open("output.csv", mode="r") as file:
    reader = csv.reader(file)
    is_serial_number = True

    for row in reader:
        if "Centre" in row[0]:
            c = row[0].split(" ")[1]
            center = c

        elif "Srl" in row[0]:
            s = row[0].split(" ")[0]
            m = row[0].split(" ")[2]

        elif is_number(row[0]):
            # print(row)
            if is_serial_number:
                serial_number.append(row[0])
                is_serial_number = False
                center_arr.append(center)

            else:
                marks.append(row[0])
                is_serial_number = True

        else:
            if "NEET" in row[0]:
                pass
            elif "Page" in row[0]:
                pass
            else:
                center_name.append(row[0])

# for i in range(len(serial_number)):
#     print(serial_number[i],' ', marks[i], ' ', center_arr[i])


print(len(serial_number), " ", len(marks), " ", len(center_name), len(center_arr))


for i in range(len(serial_number)):
    rows_to_write.append([center_arr[i], serial_number[i], marks[i]])

with open("result.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Center Number", "Serial Number", "Marks"])
    writer.writerows(rows_to_write)

print("Data successfully written to result.csv")
