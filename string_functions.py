#difference between casefold and lower
#firstString = "Fluß"
#secondString = "Fluss"
#num1="34"
#c0="hi"
#c1 = "1.23"
#c2 = "$*%!!!"
#c3 = "0.34j"
#c4= u"\u00B2"
#print(firstString.casefold())
#print(secondString.casefold())
#print(firstString.lower())
#print(secondString.lower())
#gives result in the form of boolean
#print(firstString.isalpha())
#print(secondString.isalpha())
#print(firstString.isalnum()) 
#print(num1.isalnum())
#print(c1.isalnum())
#print(c2.isalnum())
#print(c3.isalnum())
#print(firstString.isalnum()) 
#print(num1.isdecimal())
#print(c1.isdecimal())
#print(c2.isdecimal())
#print(c3.isdecimal())
#print(c4.isdecimal())

#print(num1.isdigit())
#print(c1.isdigit())
#print(c2.isdigit())
#print(c3.isdigit())
#print(c4.isdigit())

#print(num1.isdigit())
#print(c1.isdigit())
#print(c2.isdigit())
#print(c3.isdigit())
#print(c4.isdigit())

#print(num1.isnumeric())
#print(c0.isnumeric())
#print(c1.isnumeric())
#print(c2.isnumeric())
#print(c3.isnumeric())
#print(c4.isnumeric())

#a = " "
#print(a.isspace())

#a = "Bart"
#print(a.isspace())

#a = "\t"
#print(a.isspace())

#a = "\r\n"
#print(a.isspace())

#a = "-"
#print(a.join("123"))

#a = "."
#print(a.join("USA"))

#a = ". "
#print(a.join(("Dr", "Who","hi")))

#a = "hi"
#print(a.join(("DrWhohi")))

#a = "bee" 
#print(a.ljust(12, "-"))

#a = "bee" 
#print(a.ljust(5, "*"))

#a = "      Bee      "
#print(a.lstrip(), "!")

#a = "-----Bee-----"
#print(a.lstrip("-"))

#a = "Bee"
#print(a.lstrip(), "*")

#a = "  Bee   "
#print(a.lstrip())

#a = "      Bee      "
#print(a.rstrip(), "!")

#a = "-----Bee-----kjkkj------"
#print(a.rstrip("-"))

#a = "Bee    uu"
#print(a.rstrip(), "*")

#a = "  Bee   "
#print(a.rstrip())

#a = "Python-program"
#b="sony.ni.hu"
#c="world"
#print(a.partition("-"))
#print(a.partition("."))
#print(b.partition("-"))
#print(b.partition("."))
#print(c.partition("-"))
#print(c.partition("."))

#a = "Yes Fitness"

#print(a.rfind("Y"))
#print(a.rfind("e"))
#print(a.rfind("s"))
#print(a.rfind("ss"))
#print(a.rfind("z"))
#print(a.rfind("Homer"))

#a = "Yes Fitness"

#print(a.rindex("Y"))
#print(a.rindex("e"))
#print(a.rindex("s"))
#print(a.rindex("ss"))
#print(a.rindex("y"))
#print(a.rindex("z"))
#print(a.rindex("Homer"))

#a = "Homer"
#print(a.startswith("H"))
#print(a.startswith("h"))
#print(a.startswith("Homer"))
#print(a.startswith("z"))
#print(a.startswith("om", 1, 3))

#a = "36"
#print(a.zfill(5))

#a = "-36"
#print(a.zfill(5))

#a = "+36"
#print(a.zfill(5))

#a = "Banana"
#print(a.endswith("a"))
#print(a.endswith("nana"))
#print(a.endswith("z"))
#print(a.endswith("an", 1, 3))

#a = "Fitness"
#print(a.find("F"))
#print(a.find("f"))
#print(a.find("n"))
#print(a.find("ness"))
#print(a.find("ess"))
#print(a.find("z"))
#print(a.find("Homer"))

print("{} and {}".format("Tea", "Coffee"))

# Example 2
print("{1} and {0}".format("Tea", "Coffee"))

# Example 3
print("{lunch} and {dinner}".format(lunch="Peas", dinner="Beans"))

# Example 4
print("{0}, {1}, {2}".format(*"123"))

# Example 5
lunch = {"food": "Pizza", "drink": "Wine"}
print("Lunch: {food}, {drink}".format(**lunch))

#string_operators
#a = "Tea " + "Leaf"
#print(a)

#a = "Bee " * 3
#print(a)

#a = "Sea" #slice
#print(a[1])

#a = "Mushroom" #range-slice
#print(a[4:8])

#a = "Mushroom" #IN
#print("m" in a)
#print("b" in a)
#print("shroo" in a)

a = "Mushroom"
print("m" not in a)
print("b" not in a)
print("shroo" not in a)

