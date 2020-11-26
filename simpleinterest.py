principle = int(input('Enter your principle :'))
rate = int(input(' Enter your Rate :'))
time = int(input(' Enter your Time:'))
amount = principle * rate * time / 100
si = amount-principle
print('amount',amount)
print('si',si)