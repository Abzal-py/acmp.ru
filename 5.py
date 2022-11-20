input()
arr =list(map(int,input().split()))
arr_odd = [_ for _ in arr if _%2!=0]
arr_even = [_ for _ in arr if _%2==0]
print(*arr_odd)
print(*arr_even)
print("YES" if len(arr_even)>len(arr_odd) else "NO")