import json

def sort_json_by_center_number(json_data):
    return sorted(json_data, key=lambda x: x['centerNumber'])

with open('./data.json') as file:
    data = json.load(file)
    sorted_data = sort_json_by_center_number(data)

# Output file path
output_file = 'sorted_centers.json'

# Writing the sorted data to a new JSON file
with open(output_file, 'w') as file:
    json.dump(sorted_data, file)

print(f"Sorted data has been exported to {output_file}")
