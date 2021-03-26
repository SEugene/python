import os

project_name = 'my_project'
dir_names = ['settings', 'mainapp', 'adminapp', 'authapp']
for dir_path in dir_names:
    if not os.path.exists(os.path.join(project_name, dir_path)):
        os.makedirs(os.path.join(project_name, dir_path))
