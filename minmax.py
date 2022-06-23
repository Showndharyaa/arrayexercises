#Program to identify second largest number in the list

mango=[10,90,7,66,55]
largest = max(mango)

def second_largest(mango):
    mango.remove(largest)
    print(max(mango))

second_largest(mango)
