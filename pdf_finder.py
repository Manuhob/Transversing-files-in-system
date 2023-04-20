import os
import argparse
from os.path import abspath, join


def traverse(path):
    displayed_files = []
    for top_dir, directories, files in os.walk(path): #Walking through the path tree
        for file in files:
            full_path = abspath(join(top_dir,file)) #Getting absolute path of the files
            file_size = os.path.getsize(full_path)/1024**2 #file size in megabytes           
            if file_size > 0.01 and '.pdf' in full_path: 
                displayed_files.append(full_path)
        if len(displayed_files) > 20: #Condition on the amount of files displayed
            break
    print(f'Printing the first 20 files in {os.path.abspath(path)} with size larger than 0.01 Mb')
    for file in displayed_files: #Printing files
        print(file)

def principalMethod():
    #This method uses argparser to retrieve input from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Insert path to transverse its subdirectories and files tree') #help menu to direct the user.
    args = parser.parse_args()
    #Another way to retrieve input from the command line using sys module:  path = str(sys.argv[-1]) 
    return traverse(args.path)


if __name__ == '__main__':
    principalMethod()


