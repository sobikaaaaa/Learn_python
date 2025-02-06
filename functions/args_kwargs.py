# This is positional argument
# def greet(name,age,nationality):
#     print(name,age,nationality)
# greet("Sobika",23,"Nepalese")
# this is keyword argument
# def encrypt(plaintext,algorithm):
#     print(plaintext,algorithm)
# encrypt(algorithm="plaintext",plaintext="sha256")    

# def my_function(*args):
#     for arg in args:
#         print(arg)
# my_function("subu",12,12.34,"a",[1,2,3,4],12,("orange","apple","mango"))

def my_function_2(**kwargs):
    for key,value in kwargs.items(): 
      print(f"{key}={value}")

my_function_2(name="subu",age=23,nationality="nepalese")
