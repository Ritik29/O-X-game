money = int(input())
if money // 6769 >= 1:
    print(str(money // 6769) + ' sheep')
elif (money // 3848) >= 1:
    if (money // 3848) == 1:
        print(str(money // 3848) + ' cow')
    else:
        print(str(money // 3848) + ' cows')
elif (money // 1296) >= 1:
    if (money // 1296) == 1:
        print(str(money // 1296) + ' pig')
    else:
        print(str(money // 1296) + ' pigs')
elif money // 678 >= 1:
    if money // 678 == 1:
        print(str(money // 678) + ' goat')
    else:
        print(str(money // 678) + ' goats')
elif money // 23 >= 1:
    if (money // 23) == 1:
        print(str(money // 23) + ' chicken')
    else:
        print(str(money // 23) + ' chickens')
else:
    print('None')