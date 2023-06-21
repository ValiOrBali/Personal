import json

def process_json_data(file_path):
    def read_json_file(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    
    # Read JSON data from file
    json_data = read_json_file(file_path)
    
    # Initialize dictionaries
    hdfsdf = {}
    asdas = {}
    asdad = {}
    
    # Iterate over JSON data and store key-value pairs in respective dictionaries
    for index, item in enumerate(json_data):
        if index == 0:
            target_dict = hdfsdf
        elif index == 1:
            target_dict = asdas
        elif index == 2:
            target_dict = asdad
        else:
            break
            
        for key, value in item.items():
            target_dict[key] = value
    
    # Return the dictionaries
    return hdfsdf, asdas, asdad

# Example usage
file_path = "data.json"
hdfsdf, asdas, asdad = process_json_data(file_path)

# Print the dictionaries
print("hdfsdf:", hdfsdf)
print("asdas:", asdas)
print("asdad:", asdad)

