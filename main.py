import os

class FileSystem:
    def __init__(self, path, name):
        self.path_to_location = path
        self.name = name
        self.path = os.path.join(self.path_to_location, self.name)
 
    def if_exist_decorator(func):
        def wrapper(self):
            if os.path.exists(self.name):
                print(f"{self.name} exist do you want overwritte it \n y / n")
                if self.user_input() == "y":
                    return func(self)
                else:
                    return
            return func(self)
        return wrapper

    def user_decision(self):
        while True:
            try:
                user_input = str(input()).lower()
                if user_input == "y" or user_input == "n":
                    return user_input
                else:
                    raise ValueError
            except ValueError:
                print("Only y or n wrong value")
    
    def mkdir(self):
        try:
            os.mkdir(self.path)
        except FileExistsError:
            print(f"Folder {self.name} alery exist") 
            
    @if_exist_decorator
    def create_file(self):
        with open(self.name, "w", encoding="utf-8"):
            print(f"File {self.name} was created")

    def write_to_file(self):
        with open(self.name, "a", encoding="utf-8") as f:
            print("type ...exit... to exit")
            list = []
            while True:
                user_input = str(input())
                if user_input == "...exit...":
                    break
                f.write(f"{user_input}\n")
                    
    def read_from_file(self):
        try:
            with open(self.name, "r", encoding="utf-8") as f:
                for i, x in enumerate(f, start=1):
                    print(f"{i}. {x.strip()}")
        except FileNotFoundError:
            print(f"File {self.name} does not exist")
        
    def delete_file(self):
        try:
            os.remove(self.path)
        except FileNotFoundError:
            print(f"File {self.name} does not exist")

    def rmdir(self):
        try:
            os.rmdir(self.path)
        except FileNotFoundError:
            print(f"Folder {self.name} does not exist")
        except OSError:
            print("Filder is not empty")

    def ls(self):
        for root, dirs, files in os.walk(self.path_to_location):
            level = root.replace(self.path_to_location, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))
                        
def make_operation(value, name, path):
    fs = FileSystem(path, name)
    operations = {
        1: fs.mkdir,
        2: fs.create_file,
        3: fs.write_to_file,
        4: fs.read_from_file,
        5: fs.delete_file,
        6: fs.rmdir,
        7: fs.ls
    }
    operation = operations.get(value)
    if operation:
        operation()

def main():
    while True:
        try:
            print("1.mkdir, 2.create_file, 3.write_to_file, 4.read_from_file, 5.delete_file, 6.rmdir, 7.ls(tree), 8.exit\n")
            path = input("Give path to folder: ")
            usr_input = int(input("Give option: "))
            
            if usr_input in range(1, 8):
                name = input("Give name file/folder to act on it: ")
                make_operation(usr_input, name, path)
            elif usr_input == 8:
                break
            else:
                print("Invalid option, please choose between 1-8.")
        except ValueError:
            print("Bad value, only 1-8")
        except FileNotFoundError:
            print("Path does not exist")

if __name__ == '__main__':
    main()



