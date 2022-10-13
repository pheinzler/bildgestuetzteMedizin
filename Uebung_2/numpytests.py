#!/usr/bin/python3
import numpy as np

A = np.arange(1,13, dtype=np.float64).reshape(3,4)
print("1a:\n" , A)

np.random.seed(2)
B = np.random.rand(3,4)
print("1b:\n" , B)

transpB = np.transpose(B)
print("2:\n" , transpB)

dotAB = np.dot(A, transpB)
print("3:\n" , dotAB)

multAB = A * B
print("4:\n" , multAB)

summedColumnsB = np.sum(B, axis=0)
print("5:\n" , summedColumnsB)

middleB = np.mean(B)
print("6:\n" , middleB)

#multiplikation mit B'T nicht B 
AB = np.matmul(A,transpB)
BA = np.matmul(transpB,A)
print("8:\nAB:", AB.shape ,"\n", AB , "\n\n" ,"BA:", BA.shape ,"\n", BA)

B = np.sqrt(A)
print("9:\n" , B)

B = B * B
print("10:\n" , B)

smallestInB = np.min(B)
print("11:\n", smallestInB)

indexBiggest = np.max()