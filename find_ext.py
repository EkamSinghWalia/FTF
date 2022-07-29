import os
req_path=input("Enter your directory path: ")

if os.path.isfile(req_path):
    print(f"The given path {req_path} is a file , PLease pass directory path only ")
else:
    all_files_dir = os.listdir(req_path)
    if len(all_files_dir)==0:
        print(f"The given path {req_path} is a empty path")
    else:
        req_ex=input("Enter the required file extention eg-> .py .sh .log .txt .bat etc: ")
        req_files=[]
        for each_file in all_files_dir:
            if each_file.endswith(req_ex):
                req_files.append(each_file)
        if len(req_files)==0:
            print(f"There are no {req_ex} files in the location {req_path}")
        else:
            print(f"There are {len(req_files)} files in the location {req_path}")
            print(f"So ,the files are: {req_files}")
            
