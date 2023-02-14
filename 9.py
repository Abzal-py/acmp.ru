def solution(arr) -> list:
    pos_sum = sum([i for i in arr if i>0])
    proz = 1
    min1 = arr.index(min(arr))
    max1 = arr.index(max(arr))
    if max1>min1:
        for i in arr[min1+1:max1]:
            proz*=i
    else:
        for i in arr[max1+1:min1]:
            proz*=i
    return [pos_sum, proz]
input()
arr = list(map(int,input().split()))
sol = solution(arr)
print(*sol)