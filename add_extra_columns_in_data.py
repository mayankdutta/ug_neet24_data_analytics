import json
import csv

rows_to_write = []

# Read the JSON data from the file
with open("./sorted_centers.json") as file:
    data = json.load(file)

# print("Center Names:")
# for item in data:
#     print(item["centerName"])


# Helper function for binary search
def binary_search(data, centerNumber):
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        temp = int(data[mid]["centerNumber"])

        if temp == centerNumber:
            return data[mid]
        elif temp < centerNumber:
            left = mid + 1
        else:
            right = mid - 1
    return None


with open("result.csv", mode="r") as file:
    reader = csv.reader(file)
    is_serial_number = True

    for row in reader:
        if not row[0].isdigit():
            continue

        centerNumber = int(row[0])
        item = binary_search(data, centerNumber)

        if item == None:
            print("not found: ", centerNumber)

        else:
            rows_to_write.append(
                [
                    row[0],
                    row[1],
                    row[2],
                    item["centerName"],
                    item["centerCity"],
                    item["centerState"],
                ]
            )

print("Finding and replacing DONE")
with open("final_result.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "centerNumber",
            "serialNumber",
            "Marks",
            "centerName",
            "centerCity",
            "centerState",
        ]
    )
    writer.writerows(rows_to_write)

print("Writting DONE")
