
# 插入排序
a = [61, 41, 59, 26, 41, 58]
for j in range(len(a)):
    i = j-1
    key = a[j]
    # print(i)
    # 非升序
    while a[i] < key:
        # print(a[i])
        a[i + 1] = a[i]
        i = i - 1
        if i < 0:
            break
    a[i+1] = key

print(a)

#%%
a = [1, 2, 3, 4, 5, 6]
v = 2
for i in range(len(a)):
    if v == a[i]:
        print(i)
print('nil')

#%%
a = [1, 1, 0, 1, 0, 0, 1, 1]
b = [1, 0, 1, 1, 0, 1, 0, 1]
c = 0
e = [0]*(len(a)+1)
for i in reversed(range(len(a))):
    if c == 0:
        d = a[i] + b[i]
        if d == 2:
            e[i+1] = 0
            c = 1
        else:
            e[i+1] = d
            c = 0
    elif c == 1:
        d = a[i] + b[i] + c
        if d == 1:
            e[i+1] = 1
            c = 0
        elif d == 2:
            e[i+1] = 0
            c = 1
        elif d == 3:
            e[i+1] = 1
            c = 1
e[0] = c
print(e)

