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
result = 0

if num > 1:
    for i in range(1, num+1):
        result += i
print(result)

if num > 1:
    while a <= num:       # I prefer while loops:P they seem much more flexible idk
        result += a
        a += 1
print(result)