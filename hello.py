def PowerA3(A):
    B =A **3
    return B
print(PowerA3(3))#Proc 1

def PowerA234(A):
    B = A**2
    C = A**3
    D = A**4
    return B, C, D
print (PowerA234(2))#Proc 2

def Mean(X,Y):
    Amean =  (X + Y) / 2
    GMean = (X * Y) ** 0.5
    return Amean, GMean

print(Mean(4, 6))#Proc 3

import math
def  TrianglePS(a):
    P = 3 * a
    S = a ** 2 * math.sqrt(3 / 4)
    return P , S

print(TrianglePS(3))#Proc 4

def RectPS(x1, y1, x2, y2):
    P = (abs(x1 - x2) + abs(y1 - y2)) * 2
    S = abs(x1 - x2) * abc(y1 - y2)
    return P , S

print(RectPS(6, 2 , 8 , 3))#Proc 5




    def DigitCoutSum(K):
        count = 0
        sum = 0
        for i in str(K):
            count += 1
            sum += int(i)
    
        return count, sum  
    print(DigitCoutSum(1234567))#Proc 6




    

