import json
import os


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_all_json_files(file_path):
    storage = []
    for file in os.listdir(file_path):
        ful_file_path = "%s/%s" % (file_path, file)
        data = read_json(ful_file_path)
        storage.append(data)
    return storage

def write_pickle(file_path, data):
    json_object = json.dumps(data)
    with open('golden_output.pickle', mode = 'w') as outfile:
        outfile.write(json_object)

def load_pickle(file_path):
    with open(file_path, 'r') as file:
        pickle = json.load(file)
    print(pickle)