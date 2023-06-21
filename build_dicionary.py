import json

def process_json_data(file_path):
    def read_json_file(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    
    # Read JSON data from file
    json_data = read_json_file(file_path)
    
    # Initialize dictionaries
    dictionaries = [{}, {}, {}]
    
    # Iterate over JSON data and store key-value pairs in respective dictionaries
    for index, item in enumerate(json_data):
        if index < len(dictionaries):
            target_dict = dictionaries[index]
            for key, value in item.items():
                target_dict[key] = value
    
    # Return the dictionaries
    return dictionaries

# Example usage
file_path = "data.json"
result = process_json_data(file_path)

# Print the dictionaries
print("hdfsdf:", result[0])
print("asdas:", result[1])
print("asdad:", result[2])

