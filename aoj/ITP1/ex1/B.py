num = int(input())
h = num // 3600
m = num % 3600 // 60
s = num % 60
print(f"{h}:{m}:{s}")
