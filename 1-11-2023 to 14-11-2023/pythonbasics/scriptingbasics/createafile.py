#automation to create a file   
from os import path

def createFile(dest):
    if not (path.isfile(dest)):
        f=open(dest,'w')
        f.write("Welcome to python scripting")
        f.close()

dest="C:\\Users\\107497\\Desktop\\Python\\pythonbasics\\scriptingbasics\\new.txt"        

createFile(dest)
print("Created file")