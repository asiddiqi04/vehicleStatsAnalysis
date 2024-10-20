import json
from ckanapi import RemoteCKAN

# Initialize CKAN API client
rc = RemoteCKAN('https://open.canada.ca/data/en/')

# Resource ID of the dataset
#resource_id = "edba4afa-dc19-480c-bbe4-57992fc9d0d6"
resource_id = "f2e53a2b-e075-473a-9a9c-5d7bef68d07d"

# Define limit per query
limit = 100  # The number of records to fetch in each request
offset = 0   # Start with the first batch
all_records = []  # List to store all records

# Loop through paginated results
while True:
    result = rc.action.datastore_search(
        resource_id=resource_id,
        limit=limit,
        offset=offset
    )
    
    records = result['records']
    
    # If no more records are returned, break out of the loop
    if not records:
        break
    
    # Add the retrieved records to the all_records list
    all_records.extend(records)
    
    # Increment the offset by the limit to get the next batch of records
    offset += limit

# Now all_records contains all the records
# print(f"Total records retrieved: {len(all_records)}")
# print(all_records)

with open("output_2021.json", "w") as json_file:
    json.dump(all_records, json_file, indent=4)
