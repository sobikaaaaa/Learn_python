def is_palindrome(name):
    reverse=''
    for i in range(len(name)-1,-1,-1):
        reverse+=name[i]
    print(name,reverse)
    if name==reverse:
        return True
    return False
palindrome=is_palindrome("shiv")
print(palindrome)