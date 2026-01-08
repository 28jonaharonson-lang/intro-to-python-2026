a = 10
b = 5
c = 4.5
print(a)
print(b)
print(c)
user = input ("Change A? (yes or no):")
if user == "yes":
    userTemp = input ("What do you want to change it to?:")
    a = userTemp
else: print ("Okay.")

user = input ("Change B? (yes or no):")
if user == "yes":
    userTemp = input ("What do you want to change it to?:")
    b = userTemp
else: print ("Okay.")

user = input ("Change C? (yes or no):")
if user == "yes":
    userTemp = input ("What do you want to change it to?:")
    c = userTemp
else: print ("Okay.")
print ("A is equal to " + a + ", B is equal to " + b + ", and C is equal to " + c + ".")
