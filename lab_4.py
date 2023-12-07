import numpy as np

def create_wx(x, w, k):
    wx = 0
    for i in range(len(x[k])):
        wx += (x[k][i] * w[i])
    return wx;

x1 = [1,0,1,0]
x2 = [1,1,1,0]
x3 = [0,0,1,1]
x4 = [1,1,0,0]

x = np.array([x1,x2,x3,x4])
w = np.array([0,0,0,0])

k = 0
g = 0
flag = 0
while (flag < 4):
    flag = 0
    while k > 3:
        k -= 4

    
    wx = create_wx(x, w, k)
    
    if (k in (0,1) and wx <= 0):
        w = np.add(w, x[k])
    if (k in (2, 3) and wx >= 0):
        w = np.add(w, -x[k])
   
    print ("Новый шаг")
    print(wx)
    print(k)
    
    k += 1
    g += 1

    for i in range(4):
        if (i in [0, 1]) and (create_wx(x, w, i) > 0):
            flag += 1
        if (i in [2, 3]) and (create_wx(x, w, i) < 0):
            flag += 1

    

print ("Искомое w = " + str(w))
print("Было получено на за " + str(g) + " шагов")