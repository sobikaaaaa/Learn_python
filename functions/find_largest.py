def find_largest(arr):
    largest=0
    for el in arr:
        if el>largest:
            largest=el
    return largest
largest=find_largest([1,3,2,4,0])
print(largest)