#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

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

#???
indexBiggest = np.where(np.max(B))
print("12:\n", indexBiggest)

oddReversed = np.array(A[A%2==1][::-1])
print("13:\n", oddReversed)

arrToAdd = np.array([10,11,12,13])
A = np.append(A,arrToAdd).reshape(4,4)
print("14:\n", A)

onesV = np.ones_like(A)
onesB = np.ones_like(A)
AvB = A * onesV + onesB
print("15:\n", AvB)

#B fehlt eine zeile. A und B wegen aufgabe 14 nicht gleich groß
# l1 = np.linalg.norm(A-transpB,1)
# l2 = np.linalg.norm(A-transpB,2)
# print("16:\nL1 Distance: ", l1, "\nL2 Distance: ", l2)