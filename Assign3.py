money_left = int(input("How much money you have "))
price_apple = int(input("How much is an apple "))
apples_amount = money_left // price_apple
money = money_left % price_apple
print (f"You can buy {apples_amount} apples and your change is {money}")