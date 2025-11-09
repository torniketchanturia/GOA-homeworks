# >, <, >=, <=, ==, !=

# examples of >
print(5 > 3) # will print "True"
print("strawberry" > "chocolate") # will print "True"
print(3 > 5) # will print "False"
print(5 > 5) # will print "False"
num = 5
print(11 > 1*num) # will print "True"

# examples of <
print(5 < 3) # will print "False"
print("summer" < "winter") # will print "True"
print(3 < 5) # will print "True"
print(5 < 5) # will print "False"
print(11/num < 10) # will print "True"

# examples of >=
print(5 >= 3) # will print "True"
print("strawberry" >= "chocolate") # will print "True"
print(3 >= 5) # will print "False"
print(5 >= 5) # will print "True"
print(11 >= 1*num) # will print "True"

# examples of <=
print(5 <= 3) # will print "False"
print("summer" <= "winter") # will print "True"
print(3 <= 5) # will print "True"
print(5 <= 5) # will print "True"
print(11/num < 10) # will print "True"

# examples of ==
print(5 == 3) # will print "False"
print("strawberry" == "strawberry") # will print "True"
print(3 == 5) # will print "False"
print(5 == 5) # will print "True"
num = 11
print(11 == 1*num) # will print "True"

# examples of !=
print(5 != 3) # will print "True"
print("strawberry" != "strawberry") # will print "False"
print("me" != "you") # will print "True"
print(5 != 5) # will print "False"
print(11 != 1*num) # will print "False"

''' logical operators ანუ ლოგიკური ოპერატორები აერთებენ და ცვლიან ბულიანის ოპერაციებს რომ შექმნან
უფრო კომპლექსური ოპერაციები/პირობები'''

# examples of logical operations:
# and
print(True and True) # will print "True"
print(False and True) # will print "False"
print(False and False) # will print "False"
# or
print(True or True) # will print "True"
print(True or False) # will print "True"
print(False or False) # will print "False"

print(True and 5+5 ==10 and 4/2 >= 3 or False and "wawa" == "qwerty" or 144/12 == 12) # will print "True"




username = input("what's your name? \n")
my_name = "Toko"

user_age = int(input("your age? \n"))
required_age = 18

user_num = int(float(input("input a random number from 1-100: \n")))
my_num = 67

print(user_num > my_num)
print(username == my_name)
print(user_age >= 18)