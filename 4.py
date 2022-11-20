a = int(input())
arr = [a,9,9]
s = ''
arr[2] -=a
for _ in arr:
    s +=str(_)
print(s)