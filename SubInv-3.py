# In this exercise you need to create the inverse of matrix A using only row subtraction

# Procedure SubtractRows(i,j,M) subtracts jth row from ith row
# Procedure SqProd(M1,M2,N) compute the product of M1 x M2 and stores it in N

# -------------------------------------------
# Prints the content of matrix M 
# -------------------------------------------

def PrintMatrix(M):
    
    for i in range(0, 5):
        print('|{:>3d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4]))


# -------------------------------------------
# Prints embedded matrices M and N
# -------------------------------------------

def PrintEmbedded(M,N):
    
    for i in range(0, 5):
        print('|{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} ¦'.format(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4])
              +'{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(N[i][0],N[i][1],N[i][2],N[i][3],N[i][4]))


# -------------------------------------------
# Prints embedded product M x N = P
# -------------------------------------------

def PrintProduct(M,N,P):
    
    for i in range(0, 5):
        if (i==2):
            print('|{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4])
              +' x |{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(N[i][0],N[i][1],N[i][2],N[i][3],N[i][4])
              +' = |{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(P[i][0],P[i][1],P[i][2],P[i][3],P[i][4]))
        else:
            print('|{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4])
              +'   |{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(N[i][0],N[i][1],N[i][2],N[i][3],N[i][4])
              +'   |{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(P[i][0],P[i][1],P[i][2],P[i][3],P[i][4]))
 

# -------------------------------------------
# In Matrix M subtracts row_j from row_i
# -------------------------------------------

def SubtractRows(i,j,M):    

    for k in range(0, 5):
        M[i][k]-=M[j][k]    # row_i = row_i -row_j


# -------------------------------------------
# Computes product N of square matrices M1, M2
# -------------------------------------------
def SqProd(M1,M2,N):

    for i in range(0, 5):
        for j in range(0, 5):
            N[i][j]=0
            for k in range (0, 5):
                N[i][j]+=(M1[i][k]*M2[k][j])
# -------------------------------------------

# Data initialisation

A=[[1,1,1,1,1],
   [0,1,1,1,1],
   [0,0,1,1,1],
   [0,0,0,1,1],
   [0,0,0,0,1]]

B=[[1,0,0,0,0],
   [0,1,0,0,0],
   [0,0,1,0,0],
   [0,0,0,1,0],
   [0,0,0,0,1]]

C=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]]


print ("The original matrix A, the task is to compute A^-1\n")
PrintMatrix(A)

print ("\n We adopt the embedded representation with matrix A on the left and the Identity matrix B on the right\n")
PrintEmbedded(A,B)


# -------------------------------------------
# DO NOT CHANGE ANYTHING ABOVE THIS LINE
# -------------------------------------------

# Below you write your code including
# Comment on the manipulated rows using print operation
print("\n\n Subtraction of raw_2 from row_1, i.e., row_1 = row_1 - row_2\n")

# apply function SubtractRows to manipulate A and B accordingly

SubtractRows(0,1,A)
SubtractRows(0,1,B)

# apply function PrintEmbedded to print the current content of embedded A and B
PrintEmbedded(A,B)



print("\n\n Subtraction of raw_3 from row_2, i.e., row_2 = row_2 - row_3\n")

SubtractRows(1,2,A)
SubtractRows(1,2,B)

PrintEmbedded(A,B)


print("\n\n Subtraction of raw_4 from row_3, i.e., row_3 = row_3 - row_4\n")

SubtractRows(2,3,A)
SubtractRows(2,3,B)

PrintEmbedded(A,B)

print("\n\n Subtraction of raw_5 from row_4, i.e., row_4 = row_4 - row_5\n")

SubtractRows(3,4,A)
SubtractRows(3,4,B)

PrintEmbedded(A,B)

# -------------------------------------------
# DO NOT CHANGE ANYTHING BELOW THIS LINE
# -------------------------------------------

# final test of correctness, by matrix multiplication of A and obtained B=A^-1

A=[[1,1,1,1,1],
   [0,1,1,1,1],
   [0,0,1,1,1],
   [0,0,0,1,1],
   [0,0,0,0,1]]

SqProd(A,B,C)

print ("\n\n We compute the product of A and A^-1 obtaining identity matrix on the right\n")

PrintProduct(A,B,C)



