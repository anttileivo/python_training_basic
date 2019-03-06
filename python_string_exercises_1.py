# Python String Exercices 1 (these should be practised on Python console, but this time they will be here)

# Exercise 1
str1="bark"
str2="park"
str3=","
print(str1[0]+str3+str1[1]+str3+str1[2]+str3+str1[3])
print(str2[0]+str3+str2[1]+str3+str2[2]+str3+str2[3])

# Exercise 2
str1="pin"
print(str1[0]+str1[1]+str3+str1[1]+str1[2])

# Exercise 3 bad

str1="abracadabra"
#str2=str1.split("c")
#print(str2)

print(str1[0:4]+","+str1[4: ])

# Exercise 3 weird

#firstpart, secondpart = string[:len(string)/2], string[len(string)/2:]
#print(firstpart)
#print (secondpart)


# Exercise 4
str1="four"
print(len(str1))

# Exercise 5
str1="viisi"
print(len(str1))

# Exercise 6
str1="breathe"
print(str1[0:6])

# Exercise 7
str1="weight"
print(str1[0:5])

# Exercise 8
str1="weight"
print(str1[1:6])

# Exercise 9
str1="hearth"
print(str1[1:6])

# Exercise 10
str1="intermediate"
print(str1[5:10])

# Exercise 11
str1="premediates"
print(str1[3:8])

# Exercise 12
str1="grand"
str2="ma"
print(str1+str2)

# Exercise 13
str1="grand"
str2="dad"
print(str1+str2[1:3])

# Exercise 14
str1="grand"
str2="ma"
print(str1*3+str2)

# Exercise 15
str1="grand"
str2="dad"
print(str1*4+str2[1:3])

# Exercise 16

var=3
print(str(var))

# Exercise 17

var=4
print(str(var)*3)

# Exercise 18

str1="Another bad example, what a good day"
str1 = str1.replace("bad", "good",1); str2 = str1.replace("good", "bad",1)
print(str2)

