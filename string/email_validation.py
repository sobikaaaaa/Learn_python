email="subu@gmail.com"
def validate_email(email):
    
    if "@" not in email:
        return False
    if "." not in email:
        return False
    splitted=email.split("@")
    print(splitted)
    first=splitted[0]
    if len(first)==0:
        return False
    splitted1=splitted[1].split(".")
    print(splitted1)
    before_dot=splitted1[0]
    print(before_dot)
    if len(before_dot)==0:
        return False
    after_dot=splitted1[1]
    print(after_dot)
    if len(after_dot)<2:
        return False
    return True
is_valid=validate_email(email)    
if is_valid:
    print("Email is valid")
else:
    print('Email is not valid')    