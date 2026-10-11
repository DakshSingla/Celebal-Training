binary_str = str(int(input()))
decimal_number = 0
power = 0

for i in range(len(binary_str) - 1, -1,-1):
    decimal_number += int(binary_str[i]) * (2 ** power)
    power += 1

print(decimal_number)