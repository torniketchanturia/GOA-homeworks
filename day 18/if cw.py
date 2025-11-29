number = int(input("Input a number: "))

if number > 50:
    print(number*5)
else:
    print(number*number)

password = input("Enter the password: ")

if password == "moths123":
    print("The password is correct!:D")
else:
    print("The password is incorrect:(")

num = int(input("Input a number: "))
a = 1

if num > 1:
    for i in range(1, num+1):
        print(i)

if num > 1:
    while a <= num:       # I prefer while loops:P they seem much more flexible idk
        print(a)
        a += 1