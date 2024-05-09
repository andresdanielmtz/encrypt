import zipfile
import os

def get_file_names(folder_path):
    file_names = []
    # Ensure folder_path is a valid directory
    if os.path.isdir(folder_path):
        # Iterate over all files in the directory
        for file_name in os.listdir(folder_path):
            # Join the folder path with the file name to get the full path
            file_path = os.path.join(folder_path, file_name)
            # Check if the path is a file (not a directory)
            if os.path.isfile(file_path):
                file_names.append(file_path)
    else:
        print(f"Error: '{folder_path}' is not a valid directory.")

    return file_names


def crack_password(password_list, zip_file_path):
    idx = 0

    with open(password_list, 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()  # Remove any leading/trailing whitespace
            idx += 1
            try:
                with zipfile.ZipFile(zip_file_path) as zf:
                    zf.extractall(path="archivos", pwd=password.encode())  # Try decoding password to bytes
                    print(f"Password found in '{zip_file_path}' at line {idx}: {password}")
                return True
            except Exception as e:
                continue
    return False


folder_path = 'archivos'
zipFiles = get_file_names(folder_path)
print("Files in folder:", zipFiles)

password_list = "passwords.txt"

for zip_file_path in zipFiles:
    try:
        with zipfile.ZipFile(zip_file_path) as zf:
            print(f"Testing '{zip_file_path}'...")
            if crack_password(password_list, zip_file_path):
                # Close the zip file
                zf.close()
                if os.path.exists(zip_file_path):
                    # Delete the file
                    os.remove(zip_file_path)
                    print(f"File '{zip_file_path}' deleted successfully.")
                else:
                    print(f"File '{zip_file_path}' does not exist.")
            else:
                print("Password not found in this file.")
    except zipfile.BadZipFile:
        print(f"Error: '{zip_file_path}' is not a valid zip file.")
    except Exception as e:
        print(f"Error: An unexpected error occurred with '{zip_file_path}': {e}")
