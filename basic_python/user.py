from pathlib import Path

path=Path('sachith')
print(path.mkdir())  #create directory
print(path.exists())  #check directory
print(path.rmdir())   #remove directory

path1 = Path()
path.glob('*')  #search all directory and file
path.glob('*.*')  #search file only
path.glob('*.py')  #search all py file
path.glob('*.xls') #search all xl sheet

for i in path1.glob('*'):  #rpint all type file in this directory
    print(i)