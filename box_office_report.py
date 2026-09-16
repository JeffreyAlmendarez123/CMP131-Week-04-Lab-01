movie_name=input("Name of Movie: ")
adult_tickets=int(input("How much Adults tickets were sold? "))
child_tickets= int(input("How many childrens tickets were sold? "))
adult_price=10
child_price=6
theater_percantage=0.2
gross_profit=(adult_tickets * adult_price)+ (child_tickets * child_price)
net_profit=gross_profit*theater_percantage
distributor_amount=gross_profit-net_profit
print(movie_name)
print(adult_tickets)
print(child_tickets)
print()
print(adult_price)
print(child_price)
print(theater_percantage)
print(gross_profit)
print(net_profit)
print(distributor_amount)