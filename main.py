import numpy as np

# # c = np.zeros([3, 4, 2])
# # print(c)

# e = np.array([[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]])
# # indexing
# print(e[0][0])
# # slicing in multidimention
# print(e[0:2,0:2]) 

# advanced indexing
c = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# to know the dimentions
print(d.ndim, d.shape)

e = np.array([4, 4, 10])
print(c[[1, 1, 1],[0, 1, 2],]) # advanced indexing, Became one dimentional array
print(c[1][0], c[1][1], c[1][2]) # can also be written as this
# broadcasting
print(e + d)
# reshaping
print(d.reshape(3, 2, order='F')) # new shape must have same amount of elements
# resizing
print(d.resize(3, 5)) # new shape do not need to have same amount of elements
print(d)
i = np.resize(c,(3, 5)) # new shape do not need to have same amount of elements
print('i', i)
# flatten # makes a copy
j = d.flatten()
k = d.ravel() # flatens and changes the original array
print(j)