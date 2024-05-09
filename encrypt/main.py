import pyminizip
import os
import random
import tempfile

def create_password() -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(4))

def zip_folder_with_password(folder_path: str, output_zip_file: str, main_password: str) -> None:
    compression_level = 5  
    temp_dir = tempfile.mkdtemp()  

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_password = create_password() 
            temp_zip_path = os.path.join(temp_dir, f"{file}.zip")
            pyminizip.compress(file_path, None, temp_zip_path, file_password, compression_level)
            print(f"Zipped {file} with password {file_password}")

    output_zip_file += ".zip"
    src_files = [os.path.join(temp_dir, name) for name in os.listdir(temp_dir)]
    pyminizip.compress_multiple(src_files, [], output_zip_file, main_password, compression_level)

    for file in src_files:
        os.remove(file)
    os.rmdir(temp_dir)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to zip: ")
    output_zip_file = input("Enter the output zip file name: ")
    main_password = create_password()  # Generate a random main password.
    print(f"Main zip password: {main_password}")
    zip_folder_with_password(folder_path, output_zip_file, main_password)
    print("Folder has been zipped with individual passwords for each file and one main password for the zip.")
