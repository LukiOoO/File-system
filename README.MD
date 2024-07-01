# File System




Details:
### 1.Create directories
mkdir(path): Creates a directory in the specified path.

### 2.Create files
create_file(path, content): Creates a file in the specified path and writes data to it.

### 3.Writing data to files
write_to_file(path, content): Writes data to a file. If the file already exists, the data will be overwritten.

### 4.Reading data from files.
read_from_file(path): Reads data from a file and returns it.
### 5.Deleting files
delete_file(path): Deletes a file from the specified path.

### 6.Deleting directories
rmdir(path): Deletes an empty directory from the specified path.

### 7.Display directory structure.
ls(path): Displays the directory structure in the specified path.

Translated with DeepL.com (free version)






        fs = FileSystem()

        fs.mkdir('/home')
        fs.mkdir('/home/user')
        fs.create_file('/home/user/file1.txt', 'Hello, world!')
        fs.write_to_file('/home/user/file1.txt', 'Hello, Python!')
        print(fs.read_from_file('/home/user/file1.txt'))  # Output: Hello, Python!
        fs.ls('/home')  # Output: ['user']
        fs.ls('/home/user')  # Output: ['file1.txt']
        fs.delete_file('/home/user/file1.txt')
        fs.ls('/home/user')  # Output: []
        fs.rmdir('/home/user')
        fs.ls('/home')  # Output: []