# dry - do not repeat yourself in code

for i in range(100):
    print(i)        # ასამდე

for i in range(101):
    print(i)        # ასის ჩათვლით

for i in range(5):
    num = int(input("Enter a number: "))
    result = num * num                       # <-- nom nom xD
    print(result)

for i in range(4, 10, 2):
    print("Hi")

    # the number of iterations as i noticed:P
    # int((stop - start)/step)
    # so in this case it'd be uhhh (10-4)/2 = 6/2 = 3
    # and it's right:DD YAY
    # this is fun!:>

for i in range(0, 7, 3):  # Just to check that the answer isn't rounded and is instead turned into an int
    print("wawa")