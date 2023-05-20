import os

def create_directory_structure():
    directories = ['app', 'app/routes', 'app/models', 'app/services', 'app/utils']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

create_directory_structure()

