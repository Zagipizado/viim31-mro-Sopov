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
        self.draw([(x, y), ((x + a), y), ((x+a), (y + b)), (x, (y + b))])
    
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
    

results.close()


plt.show()