# Python program for searching in
# unsorted array

def findElement(arr, n, key):
	for i in range (n):
		if (arr[i] == key):
			return True
	return False

def insert(arr,ins):
	arr.append(ins)
	return arr
	
def remove(arr,rem):
	arr.remove(rem)
	return arr

arr = [12, 34, 10, 6, 40]
key = 6
ins = 90
rem = 10
n = len(arr)

print(findElement(arr, n, key))
print(insert(arr,ins))
print (remove(arr,rem))
