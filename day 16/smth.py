# SITUATION: mom said to buy as much as i can:3 BUT i have to buy milk for sure!
# (kinda inspired by the game "Milk outside a bag of milk outside a bag of milk" :3)

milk = 7
chocolate = 5
gum = 1
money = int(input("how much money do you have? "))
money_at_first = money # we remember this so that then we can check if the user bought milk
pay = 0

while money >= milk and chocolate or gum: # you HAVE to buy milk so there's an "and" after that one:3
    print(" milk - 7 \n chocolate - 5 \n gum - 1 \n press 0 if you're done with shopping ")
    if money > money_at_first - milk:   # we check if the person already has bought milk cause we don't need 2 milks lol
        milk_bought = False
    else:
        milk_bought = True
    pay = int(input("Enter the money of what you want to buy in sum: "))
    if pay <= money:     
        if milk_bought == True:
            if pay == 0:
                print("I don't wanna buy anything else:3")
                break
            elif pay >= 5:
                print("yay!! good ol' chocolate:3")
                money -= chocolate
            elif pay >= 1:
                print("yippie gum:D my breath is gonna smell good now")
                money -= gum
            else:
                print("chocolate and gum yay:D")
                money -= (chocolate + gum)
        else:
            if pay < 7:
                print("but mum said i have to buy milk...")
            elif pay == 7:
                print("okii milk bought:3")
                money -= milk
            elif pay >= 8:
                print("I got milk and gum yay:D") 
                money -= (milk + gum)
            elif pay >= 12:
                print("milk and choco!! i can make chocolate milk with this:>")
                money -= (milk + chocolate)
            elif pay >= 13:
                print("Milk, chocolate and gum:3 Nice!")
                money -= (milk + chocolate + gum)
    else:
        print("I don't have that much money:<")    

print("Oh i ran outta money:P time to go home:3")
