# Output არის ის რაც კომპიუტერს გამოქვს და ჩვენ, მომხმარებელი ამას ვხედავთ
# როგორც მაგალითად პრინტ ფუნქცია
# Input არის რაც ჩვენ, მომხმარებელს შეგვყავს და ამას კომპიუტერი იმახსოვრებს სტრინგის სახით

name = input("Enter your name: ")
last_name = input("Now your last name: ")
print("Hello, " + name + " " + last_name)

num01 = float(input("now enter the first number: "))
num02 = float(input("the second number: "))
num03 = float(input("the third one: "))
num04 = float(input("the fourth: "))
num05 = float(input("and the fifth: "))

result = (num01+num02+num03+num04+num05)/5
print("The average of the numbers given by " + name + " is:")
print(result)