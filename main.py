from functions import *
init()

while True:
    command = str(input(Fore.MAGENTA + f'Enter your command: {Fore.GREEN}'))
    command.lower()
    try:
        if command == 'mkd':
            createFolder()
        elif command == 'mkf':
            createFile()
        elif command == 'dlf':
            deleteFile()
        elif command == 'dld':
            deleteFolder()
        elif command == 'calc':
            calc()
        elif command == 'cd':
            open_folder()
        elif command == 'rfl':
            rename_folder()
        elif command == 'rfd':
            rename_file()
        elif command == 'l-fd':
            list_dirs()
        elif command == 'generate_password':
            password_generator()
    except:
        print(Fore.RED + 'Incorrect command')
