#list comprehension
list = [1,2,3,4]
res = [i+1 for i in range(1,20)]
print(res)

#*********************

dict1 = {"a":12,"abc":1234,"dfe":234}
result = {key:value for key,value in dict1.items()}
print(result)


#****************************

for i in range(1,10):
  if i%2==0:
    print(i)