import pyminizip
import os
import random

def create_password() -> str:
    password = ''
    for i in range(0, 4):
        password += str(random.randint(0, 9))
    return password

def zip_folder_with_password(folder_path: str, output_zip_file: str, password: str) -> None:
    output_zip_file += ".zip"
    compression_level = 5
    src_files = []
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            src_files.append(file_path)
    
    pyminizip.compress_multiple(src_files, [], output_zip_file, password, compression_level)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to zip: ")
    output_zip_file = input("Enter the output zip file name: ")
    password = create_password()  # Optionally use user input instead
    print(f"Password: {password}")
    zip_folder_with_password(folder_path, output_zip_file, password)
    print("Folder has been zipped and password-protected.")
