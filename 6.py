step1, step2 = list(map(str,input().split("-")))
x = "ABCDEFGH"
y = "12345678"
move = [1,2]
def get_next_step(char,num):
    pass
step = [str(x[x.find(step1[0]) + move[0]])+str(y[y.find(step1[1]) + move[1]]),
        str(x[x.find(step1[0]) + move[0]])+str(y[y.find(step1[1]) - move[1]]),
        str(x[x.find(step1[0]) + move[1]])+str(y[y.find(step1[1]) + move[0]]),
        str(x[x.find(step1[0]) + move[1]])+str(y[y.find(step1[1]) - move[0]]),
        str(x[x.find(step1[0]) - move[0]])+str(y[y.find(step1[1]) + move[1]]),
        str(x[x.find(step1[0]) - move[0]])+str(y[y.find(step1[1]) - move[1]]),
        str(x[x.find(step1[0]) - move[1]])+str(y[y.find(step1[1]) + move[0]]),
        str(x[x.find(step1[0]) - move[1]])+str(y[y.find(step1[1]) -move[0]])]
print(str(y.find(step1[1])))
print(str(y.find(step1[1]) + move[1]))
print(step)
if step2 in step:
    print("YES")
