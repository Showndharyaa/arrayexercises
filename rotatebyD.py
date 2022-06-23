#Program to rotate an array by D values

pine =[29,18,45,60,5]
D = 2
n = len(pine)
pine[:] = pine[D+1:n]+pine[0:D+1] #using slicing
print (pine)
