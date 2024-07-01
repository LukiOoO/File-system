# File System




Szczegóły:
### 1.Tworzenie katalogów
mkdir(path): Tworzy katalog w podanej ścieżce.

###  2.Tworzenie plików
create_file(path, content): Tworzy plik w podanej ścieżce i zapisuje do niego dane.

### 3.Zapisywanie danych do plików
write_to_file(path, content): Zapisuje dane do pliku. Jeśli plik już istnieje, dane zostaną nadpisane.

### 4.Odczytywanie danych z plików
read_from_file(path): Odczytuje dane z pliku i zwraca je.
### 5.Usuwanie plików
delete_file(path): Usuwa plik z podanej ścieżki.

### 6.Usuwanie katalogów
rmdir(path): Usuwa pusty katalog z podanej ścieżki.

### 7.Wyświetlanie struktury katalogów
ls(path): Wyświetla strukturę katalogów w podanej ścieżce.






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