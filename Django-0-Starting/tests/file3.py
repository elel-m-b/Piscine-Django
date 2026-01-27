x = 50 # int
y = 60.5 # flout
string = "Hello world" # text
l = ["1", "1", "3"] # we used when data are changed
l[0] = 0
t = (1,2,3) # we use it when we want data be fixed
s = {1, 2, 3} # set is not indexed 

user = { # dictionary key --- > value
    "name" : "elel-m-b",
    "age" : 20
}

print (user["name"])
u = None

a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))


print ("tuple : ")
for i in range(len(t)):
    print(t[i])


print ("list : ")
for i in range(len(l)):
    print(l[i])


print ("set : ")
for item in s:
    print(item)
