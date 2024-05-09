import zipfile
import os

def zip_folder_with_password(folder_path, output_zip_file, password):
    with zipfile.ZipFile(output_zip_file, 'w') as zipf:
        zipf.setpassword(password.encode())
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, os.path.dirname(folder_path)))

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to zip: ")
    output_zip_file = input("Enter the output zip file name (including .zip extension): ")
    password = input("Enter the password for the zip file: ")

    zip_folder_with_password(folder_path, output_zip_file, password)
    print("Folder has been zipped and password-protected.")
