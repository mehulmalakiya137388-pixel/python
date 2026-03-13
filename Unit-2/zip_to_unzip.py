import zipfile

def zip_files():
    zip_name = input("Enter zip file name (example: files.zip): ")
    files = input("Enter file names to zip (separated by space): ").split()

    with zipfile.ZipFile(zip_name, 'w') as z:
        for file in files:
            z.write(file)
    print("Files zipped successfully!")

def unzip_files():
    zip_name = input("Enter zip file name to unzip: ")

    with zipfile.ZipFile(zip_name, 'r') as z:
        z.extractall()
    print("Files extracted successfully!")

while True:
    print("\nMenu")
    print("1. Zip Files")
    print("2. Unzip Files")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        zip_files()
    elif choice == '2':
        unzip_files()
    elif choice == '3':
        print("Exiting program")
        break
    else:
        print("Invalid choice")
