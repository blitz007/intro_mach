from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
digits=datasets.load_digits()
'''print(digits.images[0])

plt.figure()
plt.imshow(digits.images[0],cmap = plt.cm.gray_r)
plt.show()'''

X_train = digits.data[0:10]
Y_train = digits.target[0:10]

X_test = digits.data[345]

def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

num=len(X_train)
distance=np.zeros(num)
for i in range(0,num):
    distance[i]=dist(X_train[i],X_test)
print (distance)
min_index=np.argmin(distance)
print(Y_train[min_index])

