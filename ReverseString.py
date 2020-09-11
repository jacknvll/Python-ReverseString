myString = input("Enter your word: ")
b = list()
a = int(len(myString)) - 1
while a >= 0:
    b += myString[a]
    a-=1
print("The results are: ",*b, sep='')