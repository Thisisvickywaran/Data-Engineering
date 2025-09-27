from pathlib import Path
import os
#path=['spam','bacon','egg']


p=Path('C:/Users/admin/OneDrive/Documents/Data-Engineering/Python/')

print("*"*10)
print(list(p.glob('*'))) #gives the list of all the files in the path

print("*"*10)
print(Path.cwd()) #gives the current directory
print("*"*10)

os.chdir('C:\\Windows\\System32') # we are now in this location

print(Path.cwd())

print(Path.home()) # C:\Users\admin goes to this location

print("-"*10)
print("Currrent Working directory")
os.chdir('C:/Users/admin/OneDrive/Documents/Data-Engineering/Python/')
print(Path.cwd())

# create a folder called Newly created Folder
folder=Path("C:/Users/admin/OneDrive/Documents/Data-Engineering/Python/Newly created Folder")
folder.mkdir(exist_ok=True)
print("Created:", folder)

print(p.cwd().is_absolute())
print("changing the path to sytem32 and checking the absolute path \n")
os.chdir('C:\\Windows\\System32')
print(p.cwd())

