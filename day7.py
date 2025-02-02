#generator
def square(i):
    for i in range(i):
        if i>=5:
            print(i)
        yield i
square(10)
for i in square(10):
    print(i)

#***************************

string = "do what i say to the world"

for word in string.split():
    if  len(word) % 2==0:
        print(word)

#*********************

#find the length of the string if the length of the string is more than 3 print the first letter of the word output:W

string = "do what i say to the world"

for i in string.split():
    if len(i)>3:
        print(i[0])

#****************************

#more than 3 print the first letter of the word output:W

string = "do what i say to the world"

for i in string.split():
    if len(i)>3:
        print(i[0])
        
#******************************

#convert the string to list & first letter of string
string = "do what i say to the world"
list1 = []
for i in string.split():
    list1.append(i)
    print(i[0])
print(list1)