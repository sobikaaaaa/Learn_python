try:
    with open("non_existent.txt") as file:
        content=file.read()
except  FileNotFoundError:
    print("the file doesnot exist")    
    with open("non_existent.txt","w") as file:
        file.write("This is newly created file")
        print("The file is created")
    