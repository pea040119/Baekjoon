def gcd(a, b) -> int:
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)

num = int(input())
num_list = map(int, input().split())

mul = 1
max = 0
min = 1000000
for n in num_list:
    if n>max:
        max=n
    if n<min:
        min = n
    mul = int((mul*n)/gcd(mul, n))
    
if max==mul:
    mul*=min

print(mul)