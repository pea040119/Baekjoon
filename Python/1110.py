num = int(input())

n = 1
temp = (num%10)*10+((num%10)+(num//10))%10
while not(num == temp):
    temp = (temp%10)*10+((temp%10)+(temp//10))%10
    n+=1
print(n)