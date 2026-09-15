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

print(Mean(4, 6))

