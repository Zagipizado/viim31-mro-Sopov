import numpy as np
import matplotlib.pyplot as plt
import os


class rectangle:
    def __init__(self, x, y, a, b, n):
        self.x = x
        self.y = y
        self.width = a
        self.height = b
        self.x_array = []
        self.y_array = []
        self.array_size = n
        self.gen_class()
        # self.draw([(x, y), ((x + a), y), ((x+a), (y + b)), (x, (y + b))])
    
    def gen_class(self):
        for i in range(self.array_size):
            self.x_array.append(np.random.uniform(self.x, self.x + self.width))
            self.y_array.append(np.random.uniform(self.y, self.y + self.height))

    def get_arrays(self):
        return self.x_array, self.y_array
    
    def get_inits(self):
        return self.x, self.y, self.width, self.height
    
    def draw(self, points): 
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        
        x.append(x[0])
        y.append(y[0])  
        plt.plot(x, y) 


classes = []
colors = ['yellow', 'orange', 'cyan', 'blue', 'purple', 'red', 'gray']

if os.path.exists('data/input.conf'):
    f = open('data/input.conf', 'r')
    k = 0
    n = int(f.readline())

    for line in f:
        values = line.split(' ')
        values[len(values)-1] = values[len(values)-1].replace('\n', '')
        x, y, a, b = [float(values[i]) for i in range(len(values))]
        classes.append(rectangle(x, y, a, b, n))
        k += 1

else:
    print("File not found, data needs to be input manual...")
    k = int(input('Amount of classes = '))
    for i in range(k):
        print("Set input values " + str(k+1) + " класса \n")
        x = float(input("x = "))
        y = float(input("y = "))
        a = float(input("width = "))
        b = float(input("height = "))
        n = int(input("Amount of points in every rectangle"))
        classes.append(rectangle(x, y, a, b, n))


results = open('data/output.conf', 'w')
for i in range(k):
    res_x, res_y = classes[i].get_arrays()
    x, y, a, b = classes[i].get_inits()
    results.write("Class nimber %s\n" % (i+1))
    results.write("Input values: \n")
    results.write("x = %s, y = %s, width = %s, height = %s\n" % (x, y, a, b))
    for j in range(len(res_x)):
        results.write("%s, %s; " % (res_x[j], res_y[j]))
    results.write("\n")

    plt.scatter(res_x, res_y, c=colors[i])

dots = []
dots_1 = classes[0].get_arrays()
dots_2 = classes[1].get_arrays()

for i in range(len(dots_1[0])):
    dots.append([dots_1[0][i], dots_1[1][i], 1])
    dots.append([-dots_2[0][i], -dots_2[1][i], -1])


def heviside(a):
    for i in range(len(a)):
        if a[i] < 0:
            a[i] = 0
    return a


dots_np = np.array(dots)


dots_plus = np.linalg.matrix_power(dots_np.T.dot(dots_np), -1).dot(dots_np.T)


yn = np.array([1 for i in range(len(dots))], dtype=np.float64)


vn = dots_plus.dot(yn)
n = 1


while not(dots_np.dot(vn).all() < 0):
    if np.all(heviside(dots_np.dot(vn) - yn)) < 0.000001:
        break
    yn = yn + heviside(dots_np.dot(vn) - yn)
    vn = dots_plus.dot(yn)
    n += 1


results.write("Linear equation is \n d(x) = " + str(vn[0]) + "*x1 " + str(vn[1]) + "*x2 + " + str(vn[2]) + "\n")
results.write("Linear eqution was found on " + str(n) + " iteration")

resx = [-vn[2]/vn[0], 0]
resy = [0, -vn[2]/vn[1]]
plt.axline(resx, resy)

plt.show()