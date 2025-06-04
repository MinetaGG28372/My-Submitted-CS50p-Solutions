# My partial solution:
'''amount_due = 50
while amount_due > 0:
    print("Amount due: ",amount_due)    #format issues
    user_inserted_coin = int(input("Insert coin: "))
    amount_due = amount_due  - user_inserted_coin

change_owed = -1 *  amount_due
print("Change owed: ",change_owed)'''

accepted_coins = [25, 5, 10]
amount_due = 50
while amount_due > 0:
    print("Amount Due:",amount_due) #this format automatically creates a blank after the ":" in "Amount Due"
    user_inserted_coin = int(input("Insert Coin: "))
    if user_inserted_coin in accepted_coins:
        amount_due = amount_due  - user_inserted_coin
    else:
        amount_due = amount_due #we can skip the "else" branch, but this is for the sake of clarity

change_owed = -1 *  amount_due
print("Change Owed:",change_owed)
