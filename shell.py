import os

def cd(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Directory not found: {path}")

def ls(path='.'):
    try:
        print('\n'.join(os.listdir(path)))
    except FileNotFoundError:
        print(f"Directory not found: {path}")

def echo(args):
    print(' '.join(args))

def shell():
    while True:
        user_input = input("PyShell> ")
        
        if user_input.lower() == "exit":
            break

        parts = user_input.split()
        if not parts:
            continue

        command = parts[0].lower()
        args = parts[1:]

        if command == "echo":
            echo(args)
        elif command == "ls":
            ls()
        elif command == "cd":
            cd(args[0] if args else os.path.expanduser("~"))
        else:
            print(f"Command {command} not recognized")

shell()