import zipfile
import itertools
import string
import os
import sys

def guess_password(zip_file_path):
    #verificam daca path-ul este existent
    if not os.path.exists(zip_file_path):
        print("File-ul nu exista. Introduceti un path corect.")
        return None

    try:
        #deschidem zip file-ul
        with zipfile.ZipFile(zip_file_path) as zip_file:
            #luam toate valorile alfanumerice
            caractere = string.ascii_letters + string.digits
            max_length = 10 
            for length in range(1, max_length + 1):
                #verificam toate combinatiile posibile de cifre/litere de lungime maxim 10
                combinations = itertools.product(caractere, repeat=length)
                for combination in combinations:
                    password = ''.join(combination)
                    try:
                        #copiem in copieArhiva continutul arhivei
                        zip_file.extractall(path='copieArhiva', pwd=bytes(password, 'utf-8'))
                        print("Parola gasita: " + password)
                        return password
                    except Exception as e:
                        continue
    except zipfile.BadZipFile:
        print("Zip invalid.")
        return None
    print("Parola nu a fost gasita.")
    return None

def main():
    if len(sys.argv) != 2:
        print("Utilizare: python Proiect.py <path_zip_file>")
        return

    zip_path = sys.argv[1]
    password = guess_password(zip_path)


if __name__ == "__main__":
    main()
