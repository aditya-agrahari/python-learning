principle = int(input('Enter your priciple :'))
rate = int(input(' Enter your Rate :'))
time = int(input(' Enter your Time:'))
amount = principle*pow(1+rate/100,time)
ci = amount-principle
print('amount',amount)
print('ci',ci)