import os

folder_name = "TestFolder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder Created")
else:
    print("Folder Already Exists")