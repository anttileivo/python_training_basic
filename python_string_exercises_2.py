# Python String Exercices 2 (these should be practised on Python console, but this time they will be here)

# Exercise 1

word="anomalocaris"
print("Index number of a is")
print(word.index("a"))

# Exercise 2

word="anomalocaris"
print("Index number of r is")
print(word.index("r"))

# Exercise 3

str1="Waging on the purple drone"
print("Index number of first 'on' is")
print(str1.index("on"))

str1="Waging on the purple drone"
print("Index number of last 'on' is")
print(str1.index("on",9))

# Exercise 4

str1="Superficial"
zs=str1.find("z")
if zs != -1:
    print("Index number of z is " + str(zs))
else:
    print("z does not appear in this string")

# Exercise 5

sentence="There truly is a dazzling bright world out there, waiting for us to explore."
print(sentence.rindex("a"))

# Exercise 6

sentence="There truly is a dazzling bright world out there, waiting for us to explore."
print(sentence.index("a"))


# Exercise 7
#str1="91342391"
#print(str1[3:5])

str1="91342391"
str1=str1[4:8]
print(str1)

# Exercise 8
str1="-== Warning! ==-"
str1= str1.replace("-== ","")
str1= str1.replace("! ==-","")
print(str1)

# Exercise 9

str1="-== Error! ==-"
str1= str1.replace("-== ","")
str1= str1.replace("! ==-","")
print(str1)

# Exercise 11

str1="Changing your dog for a bird? Some dog-lover you are."
str1 = str1.replace("dog", "cat")
print(str1)

# Exercise 12
str1="Being bold has some uses."
str1 = str1.replace("o", "a",1)
print(str1)

# Exercise 13

#str1="-== ERROR! ==-"
#str1=str1.title()
#print(str1)

str1="-== Error! ==-"
str1=str1.upper()
print(str1)

# Exercise 14

str1="abraham lincoln"
str1=str1.title()
print(str1)

# Exercise 15

str1="rEaDaBlE"
str1=str1.lower()
print(str1)

# Exercise 16

str1="first word is capitalized"
str1=str1.capitalize()
print(str1)

# Exercise 17
str1="loooooooooong"
str2=str1.count("o")
print(str2)

# Exercise 18
godzillion="1000000000000000000000000000000"
number_of_zeros=godzillion.count("0")
print("Number of zeros is " + str(number_of_zeros))

# Exercise 19
sentence="Something out of nothing? I really doubt we can do it anytime soon"
number_of_ns=sentence.count("n",)
print("Number of ns in total is " + str(number_of_ns))

# Exercise 20

godzillion="1000000000000000000000000000000"
ninezillion=godzillion.replace("0","9")
print(ninezillion)

# Exercise 21

sentence="what,if,we,have,no,choice?...."
new_sentence=sentence.replace(","," ")
new_sentence=new_sentence.replace(".","")
print(new_sentence)

sentence="what,if,we,have,no,choice?...."
new_sentence=sentence.replace(","," ").rstrip(".")
print(new_sentence)