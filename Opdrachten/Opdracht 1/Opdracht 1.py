'''
Prioritized requirements:
    Multiply 2 matrices
    Multiply 2 matrices with different dimensions
    Use one function that can be used for multiple dimensions

Main design choices:
    Keep the calculations and the result seperate to keep the code easy to read and understand

Test specifications/report:
    Multiply a 3x3 and a 3x4
        Result: a 3x4 matrix
    Multiply a 3x4 and a 4x2
        Result: a 3x2 matrix
    Multiply two matrices that can't be resolved
        Result: Error message
'''

# 3x3
A = [[1,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4
B = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# 4x4
C = [[5,8,1,2],
    [6,7,3,0],
    [8,1,6,4],
    [4,5,9,1]]

# 4x2
D = [[5,2],
    [6,0],
    [8,6],
    [4,5]]

def multiply(X, Y):
    if (len(Y) == len(X[0])):
        result = [[0 for x in range (len(Y[0]))] for y in range(len(X))] # Maak een matrix van de juiste grotte

        for i in range(len(X)):
            for j in range(len(Y[0])):
                for k in range(len(Y)):
                    result[i][j] += X[i][k] * Y[k][j]
        printResult(result)
    else:
        print("This multiplication can't be done")


# Print de matrix
def printResult(Z):
    for r in Z:
        print(r)

print("AxB")
multiply(A, B)

print("\n BxC")
multiply(B, C)

print("\n BxD")
multiply(B, D)

print("\n AxD")
multiply(A, D)
