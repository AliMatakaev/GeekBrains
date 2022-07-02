
import os

current_dir = os.path.abspath(os.curdir)

directories = ['my_project']
nestedDirectories = ['settings', 'mainapp', 'adminapp', 'authapp']
i = 0
try:
    while i < len(nestedDirectories):
        path = os.path.join(current_dir, directories[0], nestedDirectories[i])
        os.makedirs(path)
        i +=1
except:
    print('Такая директория уже есть')