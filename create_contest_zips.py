import os
import zipfile
import shutil

CURR_DIR = os.path.dirname(os.path.abspath(__file__))

print(f"Current directory: {CURR_DIR}")

def create_zip(directory_path, output_path):
    # Ensure the specified directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    # Create a ZipFile object for writing to the output file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(directory_path):
            for filename in filenames:
                # Calculate the file's path
                file_path = os.path.join(foldername, filename)
                # Calculate the relative path within the ZIP file
                relative_path = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, relative_path)

    print(f'Successfully zipped the contents of {directory_path} to {output_path}')
    
def list_files_in_dir(directory_path):
    file_list = []
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
def list_dirs_in_dir(directory_path):
    directory_list = []
    try:
        for entry in os.listdir(directory_path):
            entry_path = os.path.join(directory_path, entry)
            if os.path.isdir(entry_path):
                directory_list.append(entry_path)
        return directory_list
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def create_dir(directory_path):
    try:
        os.makedirs(directory_path)
        print(f"Created directory: {directory_path}")
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"Moved '{source_path}' to '{destination_path}'")
    except FileNotFoundError:
        print(f"File '{source_path}' not found.")
        exit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
def delete_dir(directory_path):
    try:
        shutil.rmtree(directory_path)
        print(f"Deleted directory and its contents: {directory_path}")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
def rename_file(file_path, new_name):
    try:
        directory = os.path.dirname(file_path)
        new_file_path = os.path.join(directory, new_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed '{file_path}' to '{new_file_path}'")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        
# move_file("c:/Users/jacob/Documents/GitHub/CSC-23-24/c1/p1/cases/batch1/0.in", CURR_DIR)
        
CONTEST = 'c1'
NUM_PROBLEMS = 9
PROBLEMS = [8]
        
for i in PROBLEMS:
    create_dir(f"{CURR_DIR}\\{CONTEST}\\p{i}\\data\\secret")
    test_case = 0
    cases_dir_list = list_dirs_in_dir(f"{CURR_DIR}\\{CONTEST}\\p{i}\\cases")
    for dir in (cases_dir_list if cases_dir_list is not None else []):
        print(dir)
        for j, file in enumerate(list_files_in_dir(dir)):
            print(file)
            new_file_name = f"{test_case // 2}.in" if file.endswith(".in") else f"{test_case // 2}.ans"  
            rename_file(file, new_file_name)
            move_file(f"{dir}\\{new_file_name}", f"{CURR_DIR}\\{CONTEST}\\p{i}\\data\\secret\\")
            
            test_case += 1
    delete_dir(f"{CURR_DIR}\\{CONTEST}\\p{i}\\cases")
    create_zip(f"{CURR_DIR}\\{CONTEST}\\p{i}", f"{CURR_DIR}\\{CONTEST}\\zips\\{CONTEST}p{i}.zip")