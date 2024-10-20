import json
import glob

# List to hold all combined data from the files
combined_data = []

# Path to the folder containing your JSON files
# Replace 'path/to/your/json/files' with the actual path where your files are located
json_files = glob.glob('*.json')

# Loop through each JSON file and load the data
for file in json_files:
    with open(file, 'r') as f:
        data = json.load(f)  # Load the JSON data (assuming each file contains a list of dictionaries)
        combined_data.extend(data)  # Append the data to the combined list

# Write the combined data to a new JSON file
with open('vehicleStats2015_2024.json', 'w') as outfile:
    json.dump(combined_data, outfile, indent=4)

print(f"Combined {len(json_files)} files into 'combined_data.json'.")
