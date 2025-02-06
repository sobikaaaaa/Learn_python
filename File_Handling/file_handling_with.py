with open("file_handling_with.txt","a") as file:
    content=file.write(",My name is Steve Rogers")
    print(content)
    """
    The benefit of using with syntax is you donot have to close
    after doing operation on it.
    """