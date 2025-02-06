#data structure that stores data in the form of key value pairs.
my_dict={
    "name":"sita",
    "age":23,
    "city":"lalitpur"
}

# my_dict_2=dict(name="subu",age=23,city="lalitpur")
# print(my_dict["age"])
# print(my_dict.get("city"))

# fallback value
# print(my_dict.get("husband","ram"))

# add value
# my_dict["education"]="bachelors"
# print(my_dict)

# update value
# my_dict["age"]="24"
# print(my_dict)

# pop(key)-> removes the specified key and returns its value
# city=my_dict.pop("city")
# print(city)
# print(my_dict)

# popitem->removes and return last inserted key value pair
# item=my_dict.popitem()
# print(item)
# print(my_dict)

# del->removes the specific key 
# del my_dict["name"]
# print(my_dict)

# clear -> clears all the item in the dictionary
# my_dict.clear()
# print(my_dict)

# loop through keys
# for key in my_dict:
#     print(key,my_dict.get(key))

# loop through values   
# for value in my_dict.values():
#     print(value) 

# loop through key value pairs
# for key,value in my_dict.items():
#     print(key,value)



