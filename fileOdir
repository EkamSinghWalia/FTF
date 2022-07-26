import os
import sys
path = input("Enter your directory path : ")
if os.path.exists(path):
    list_of_files_or_dir = os.listdir(path) # will give all teh files and directory in the entered path
    for each_file_or_dir in list_of_files_or_dir:
        f_d_p = os.path.join(path, each_file_or_dir)
        if os.path.isfile(f_d_p):
            print(f'{f_d_p} is a file')
        else:
            print(f'{f_d_p} is a directory')
            
else:
    print("Please enter a valid path")
    sys.exit()
    
