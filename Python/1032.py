a = int(input())
string = str()
for i in range(a):
    if (i==0):
        string = list(input())
    else:
        temp = list(input())
        for j in range(len(string)):
            if (string[j] == '?'):
                continue
            if not(temp[j] == string[j]):
                string[j] = '?'
print(''.join(map(str, string)))