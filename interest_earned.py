principal=float(input("Enter the principal deposit($):"))
annualrate_percantage=float(input("What is the annual interest rate (%):"))
compounded_time=int(input("What is the number of time the interest is compounded per year:"))
rate=annualrate_percantage/ 100.00
amount=principal*((1 +(rate / compounded_time)) **compounded_time)
interest_earned=amount- principal
print(f"Interest Rate: {annualrate_percantage:>10.2f}%")
print(f"Times Compounded: {compounded_time:10}")
print(f"Principal:  ${principal:>10.2f}")
print(f"Interest Earned:   ${interest_earned:>10.2f}")
print(F"Amount in Savings: ${amount:>10.2f}")
