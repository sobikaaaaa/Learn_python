# def reverse_string(name):
#     result=""
#     for i in range(len(name)-1,-1,-1):
#         result+=name[i]  
#     return result
# reverse_count=reverse_string("Subu")
# print(reverse_count)
def reverse_count(name):
    result=""
    count=0
    for i in range(len(name)-1,-1,-1):
        result+=name[i] 
        count+=1 
    return result,count
reverse_count=reverse_count("Subu")
print(reverse_count)

