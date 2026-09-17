#Jeffrey Almendarez
#CMP131/Fundementals of programming
#Week-04
#Lab-01
#Box office Report
#9/16/26
movie_name=input("Name of Movie: ")
adult_tickets=int(input("How much Adults tickets were sold? "))
child_tickets= int(input("How many childrens tickets were sold? "))
adult_price=adult_tickets * 10.00
child_price=child_tickets * 6.00
theater_percantage=0.20
gross_profit=(adult_tickets * adult_price)+ (child_tickets * child_price)
net_profit=gross_profit*theater_percantage
distributor_amount=gross_profit-net_profit 
print()
print("Name of Movie:", movie_name)
print("Adult Tickets sold:", adult_tickets)
print("Child Tickets Sold:", child_tickets)
print(f"Gross Box profit:   ${gross_profit:,.2f}")
print(f"Net box profit:  ${net_profit:,.2f}")
print(f"Amount paid to distrubutor: ${distributor_amount:,.2f}")