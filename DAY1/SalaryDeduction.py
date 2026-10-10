n = int(input("salary: "))
late = int(input("late days: "))
ab = int(input("ab days: "))
if late >10:
    n = n-(n* 10/ 100)
elif late>5:
    n = n-(n* 5/ 100)
    if ab>2:
        n = n-(n* 5/ 100)
print(int(n))