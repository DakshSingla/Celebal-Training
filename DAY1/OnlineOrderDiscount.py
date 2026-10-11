bill = float(input("Enter total bill: "))
if (bill>=5000):
    print(bill-(bill*20/100))
elif (bill>=3000):
    print(bill-(bill*10/100))
elif (bill>=1000):
    print(bill-(bill*5/100))
else:
    print(bill)