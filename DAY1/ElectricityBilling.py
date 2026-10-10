n = int(input("enter units: "))
ans=1
if n >0:
    ans +=min(n,100)*3
if n > 100:
    ans += min(n-100, 100)*5
if n >200:
    ans +=(n-200)* 8
if n > 300:
    ans += ans *0.10
print(ans)