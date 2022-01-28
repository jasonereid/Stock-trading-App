amount = 0
portfolio = 0
investment = []
quantity = 0
price = 0
squantity = 0
sprice = 0
allocated_money = quantity * price
sallocated_money = squantity * sprice

trans_cost = 7

amount = input("How much money do you want to start with? Use whole numbers only.")
print("You have $" + amount + " to trade with.")
print("Each trade costs $" + str(trans_cost))

money_end = amount

def buy(quantity, price):
    global portfolio, money_end, allocated_money, investment
    print(money_end)
    allocated_money = quantity * price
    money_end = int(money_end) - int(allocated_money) - int(trans_cost)
    portfolio += quantity
    investment.append(allocated_money)
    print(money_end)

def sell(squantity, sprice):
    global portfolio, money_end, sallocated_money, investment
    print(money_end)
    sallocated_money = squantity * sprice
    money_end = int(money_end) + int(sallocated_money) - int(trans_cost)
    portfolio -= squantity
    investment.append(-sallocated_money)
    print(money_end)

while True:
    print("Do you want to buy or sell? Type buy or sale.")
    trans = input()

    if trans == "buy":
        quantity = int(input("How many shares?"))
        price = int(input("Price per share."))
        buy(quantity, price)
        print("You bought " + str(quantity) + " shares at $" + str(price) + " per share, for a total purchase of $" + str(allocated_money + trans_cost) + " including transaction fees.")
        print("Your portfolio contains " + str(portfolio) + " shares with $" + str(
            sum(investment)) + " dollars invested, and $" + str(money_end) + " in cash.")
    elif trans == "sell":
        squantity = int(input("How many share do you want to sell?"))
        sprice = int(input("What is the current share price?"))
        if squantity > quantity:
            print("You don't own that many shares.")
        else:
            sell(squantity, sprice)
            print("You sold " + str(squantity) + " shares at $" + str(sprice) + " per share, for a total sale profit of $" + str(allocated_money - trans_cost) + " ")
            print("Your portfolio contains " + str(portfolio) + " shares with $" + str(sum(investment)) + " dollars invested, and $" + str(money_end) + " in cash.")
    else:
        print(" ... ")
        break

print("Your portfolio contains " + str(portfolio) + " shares with $" + str(sum(investment)) + " dollars invested, and $" + str(money_end) + " in cash.")