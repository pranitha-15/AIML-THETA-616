string = "Do what i will do"
for word in string.split():
  if len(word)  % 2 == 0:
    print(word)

#*************************

string = "Do what i will do"
my_list = list(string.split())
print(my_list)
print(string[0])

#****************************

string = "welcome to python to lab"
my_list = list(string.split())
for i in my_list :
  if i == "to":
    print(i)