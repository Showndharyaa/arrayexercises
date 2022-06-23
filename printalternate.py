#Program to print alternate elemnts of an array/list

lst = [19,20,49,70,63,46,69,92,33]
n = len(lst)
new = []

def alternate(lst,n):
    for i in range(n):
        if (i % 2 == 0):
            new.append(lst[i])
    return(new)
new = alternate(lst,n)
print (new)
