balance = int(input("total amount: "))
n=int(input("size: "))
amount = []
for i in range(n):
    amount.append(int(input("number: ")))
for i in range(n):
    if(amount[i]<=balance and amount[i] %100==0):
        balance -= amount[i]
        print("SUCCESS")
    else:
        print("Fail")
print(balance)
        