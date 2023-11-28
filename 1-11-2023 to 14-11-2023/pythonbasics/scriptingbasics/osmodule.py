import os

print(os.getcwd)

# os.chdir("C:\\Users\\107497\\Desktop\\Python\\Python-Scripting-Project-main")
# print(os.getcwd)


#function for cwd
def current_directory():
    cwd=os.getcwd()
    print(cwd)

#function for path
def file_path(filename):
    path=os.path.abspath(filename)
    print(path)


current_directory()    

filename="another.txt"
file_path(filename)