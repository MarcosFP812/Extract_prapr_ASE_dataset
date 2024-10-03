import os
import json
import random
from tqdm import tqdm  # Import tqdm for the progress bar

# Function to read a file, attempting to decode it with UTF-8
def read_file(path):
    try:
        # Try reading the file with UTF-8 encoding and replace errors with a placeholder
        with open(path, 'r', encoding='utf-8', errors='replace') as file:
            return file.read()
    except UnicodeDecodeError:
        # If UTF-8 fails, print a message and try another encoding
        print(f"Failed to read {path} with UTF-8. Trying another encoding...")

# Function to load JSON data from the prapr dataset and save it
def load_json_prapr(source_directory, json_file):
    data = []  # List to store the data from files

    # Count the total number of leaf folders (folders without subfolders)
    leaf_folders = [root_folder for root_folder, subfolders, _ in os.walk(source_directory) if not subfolders]

    # Use tqdm in the loop to show progress while processing the leaf folders
    for root_folder in tqdm(leaf_folders, desc="Processing leaf folders"):
        files = os.listdir(root_folder)  # Get all files in the current folder

        # Variables to store the content of the relevant files
        original_content = None
        fixed_content = None
        correct_file_exists = False  # Flag to track if the "correct" file is present

        # Loop through the files in the folder and collect necessary data
        for file in files:
            full_path = root_folder + "/" + file  # Create full path for the file

            # If the file name starts with "ori-", it's the original file
            if file.startswith("ori-"):
                original_content = read_file(full_path)

            # If the file starts with "fixed-" or "man-", it's a fixed file
            elif file.startswith('fixed-') or file.startswith('man-'):
                fixed_content = read_file(full_path)

            # If the file starts with "patched-" and there's no fixed content yet, read it
            elif file.startswith('patched-') and fixed_content is None:
                fixed_content = read_file(full_path)

            # If the file is named "correct", mark that the correct file exists
            elif file == "correct" and not correct_file_exists:
                correct_file_exists = True

        # Only add to the data list if both original and fixed content are found
        if original_content and fixed_content:
            data.append({
                'path': root_folder,
                'original': original_content,
                'fixed': fixed_content,
                'correct': correct_file_exists
            })
    
    # Save the collected data to a JSON file after the loop ends
    with open(json_file, 'w', encoding='utf-8') as json_output:
        json.dump(data, json_output, indent=4, ensure_ascii=False)  # Save with indent for readability

# Function to load JSON data from the ASE dataset and save it
def load_json_ASE(source_directory, json_file, correct):
    data = []  # List to store the data from files

    # Count the total number of leaf folders
    leaf_folders = [root_folder for root_folder, subfolders, _ in os.walk(source_directory) if not subfolders]

    if os.path.exists(json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as json_input:
                existing_data = json.load(json_input)
        except: existing_data = []
    else: existing_data = []

    # Use tqdm to show progress while processing the leaf folders
    for root_folder in tqdm(leaf_folders, desc="Processing leaf folders"):
        files = os.listdir(root_folder)  # Get all files in the current folder

        # Variables to store the content of relevant files
        original_content = []  # List to hold multiple original file contents
        fixed_content = []  # List to hold multiple fixed file contents
        not_overlap = False  # Flag for "NOT_OVERLAP" file

        # Loop through the files in the folder and collect the necessary data
        for file in files:
            full_path = root_folder + "/" + file  # Create full path for the file

            # If the file starts with "buggy", it's an original (buggy) file
            if file.startswith("buggy"):
                original_content.append(read_file(full_path))  # Append to the list

            # If the file starts with "tool-patch", it's a fixed file
            elif file.startswith("tool-patch"):
                fixed_content.append(read_file(full_path))  # Append to the list
            
            # If the file is named "NOT_OVERLAP", set the not_overlap flag to True
            elif file == "NOT_OVERLAP" and not not_overlap:
                not_overlap = True

        # Ensure that both original and fixed content exist and have the same length before appending
        if original_content + fixed_content != [] and len(fixed_content) == len(original_content):
            # Loop through the contents to add each pair of original and fixed files
            for i in range(len(original_content)):
                data.append({
                    'path': root_folder,
                    'original': original_content[i],
                    'fixed': fixed_content[i],
                    'correct': correct,
                    'Not_overlap': not_overlap
                })

        # Save the updated data to the JSON file
        with open(json_file, 'w', encoding='utf-8') as json_output:
            json.dump(existing_data+data, json_output, indent=5, ensure_ascii=False)  # Save with indent for readability

# Function to count how many entries in the JSON file have the 'correct' field set to a specific value
def count_correct(json_path, correct):
    # Open and read the JSON file
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)  # Load JSON data into a Python list

    # Count how many elements have the 'correct' field equal to the specified value
    count = sum(1 for element in data if element.get('correct') == correct)
    
    return count  # Return the count


def shuffle_json(file_path):
    with open(file_path, 'r') as archivo:
        datos = json.load(archivo)
    
    if isinstance(datos, list):
        random.shuffle(datos)
    elif isinstance(datos, dict):
        items = list(datos.items())
        random.shuffle(items)
        datos = dict(items)
    else:
        print("El formato del archivo no es ni lista ni diccionario. No se puede desordenar.")
        return

    with open(file_path, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    
    print(f"Archivo desordenado y guardado como '{file_path}'.")


