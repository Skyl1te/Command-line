import os
from colorama import init, Fore
init()

inputColor = Fore.GREEN
textColor = Fore.MAGENTA

def createFolder():
    try:
        folder_name = str(input(textColor + f'Enter folder name: {inputColor}'))
        os.makedirs(folder_name, exist_ok=True)
    except:
        print(Fore.RED + 'ERROR')

def createFile():
    try:
        fileName = str(input(textColor + f'Enter the file name: {inputColor}'))
        fileType = str(input(textColor + f'Enter the type of file: {inputColor}'))
        f = open(f'{fileName}.{fileType}', 'w')
    except:
        print(Fore.RED + 'ERROR')
    
def deleteFolder():
    try:
        folderPath = str(input(textColor + f'Enter the path to your folder: {inputColor}'))
        os.rmdir(folderPath)
    except:
        print(Fore.RED + 'ERROR')


def deleteFile():
    try:
        filePath = str(input(textColor + f'Enter the path to your file: {inputColor}'))
        os.remove(filePath)
    except:
        print(Fore.RED + 'ERROR')

def calc():
    try:
        from apps.calc.main import calc
        calc()
    except:
        print(Fore.RED + 'ERROR')
    
def open_folder():
    try:
        folderPath = str(input(textColor + f'Enter the path to your folder: {inputColor}'))
        os.chdir(folderPath)
    except:
        print(Fore.RED + 'ERROR')
def rename_folder():
    try:
        folderPath = str(input(textColor + f'Enter the path to your folder: {inputColor}'))
        folderRename = str(input(textColor + f'Enter the new name to your folder: {inputColor}'))
        os.rename(folderPath, folderRename)
    except:
        print(Fore.RED + 'ERROR')

def rename_file():
    try:
        filePath = str(input(textColor + f'Enter the path to your file: {inputColor}'))
        fileRename = str(input(textColor + f'Enter the new name to your file: {inputColor}'))
        os.rename(filePath, fileRename)
    except:
        print(Fore.RED + 'ERROR')

def list_dirs():
    try:
        print(f'{textColor} {os.listdir()}')
    except:
        print(Fore.RED + 'ERROR')

def password_generator():
    try:
        from apps.password_generator.main import gen_password
        gen_password()
    except:
        print(Fore.RED + 'ERROR')
