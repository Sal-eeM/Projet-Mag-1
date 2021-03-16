import sys
import numpy as np


try : #Let's check the txt file
    A = np.loadtxt('ProjectMatrix.txt', dtype = 'i' )
except ValueError :       
    raise ValueError ('Please check if the txt file contains only numbers.The txt file must countain only numbers, No LETTER  and other specical characters as "," "?" ... ')
except OSError :
        raise OSError ('The txt file and MatrixReloded.py must be in the same directory') 
    
        
print('The matrix A is : ''\n',A,'\n') 
try: 
    if len(A[0]) == len(A[:,-1]) : #Let's check if the matrix is squared (same number of line, same number of column). If yes... 
        print('The transpose of A is :' '\n', A.transpose(),'\n')
        Asquare = np.dot(A,A); print('A square is equal to :' '\n',Asquare,'\n')
        print('A cube is equal to :' '\n', np.dot(Asquare,A),'\n')
        detA = np.linalg.det(A) # If yes, let's define the determinant         
        if detA ==  0 : #The case of non inversible matrix
            print(" A is not inversible" '\n')
            print("The determinant of A is", detA, '\n')
        if detA == -9.51619735392994e-16 :  # We have remarked that some version of python don't give exactly zero as a determinant but an approximation; So let's check this case.
            detA = 0 #We give the reel value 
            print(" A is not inversible" '\n')
            print("The determinant of A is", detA, '\n')
        if detA != 0 and detA != -9.51619735392994e-16 :
            print('The inverse of A is :' '\n', np.linalg.inv(A),'\n')
            print('The determinant of A is :' '\n',detA)
    else : #If the matrix is not squared 
        print('The transpose of A is :' '\n', A.transpose(),'\n')
        print('The matrix is not squared.' '\n' 'So, we cannot compute neither AxA nor AxAxA' '\n' 'Also, we cannot give the inverse of A and the determinant of A' '\n' )
except TypeError : #We need to adjust the script for line matrix and column matrix since we cannot in this case compare number of line and column in python
    print('The transpose of A is :' '\n', np.matrix(A).T,'\n') #We need to readjust the formaular of transpose for line matrix 
    print('The matrix is not squared.' '\n' 'So, we cannot compute neither AxA nor AxAxA' '\n' 'Also, we cannot give the inverse of A and the determinant of A')

try : 
    Corner =[ A[0][0], A[0][-1],A[-1][0],A[-1][-1] ] ; 
    print('The element of the corner are : ',Corner,'\n' '\n')
except IndexError : #We need to adjust corner element for line matrix and column matrix
    print("The corner element are :",[A[0], A[-1]],'\n')   

l= [] 
k = [] 
try : 
    for i in range(len(A[0])):
        l.append(A[i][i])  
    print("The elements of the main diagonale are : ",l,'\n')
except IndexError : 
    print ("The matrix is not square. Therefore we are not able to give the main diagonal")
except TypeError : #Exception for line and comumn matrix
    print ("The matrix is not square. Therefore we are not able to give the main diagonal")
    
i = 0 ; j = -1 ; k = [] #Let's give now the secondary diagonal  
try :
    if len (A[0]) == len(A[:,-1]) : # Raise the same exception as before but defferent way
        while i < len(A) :
            k.append(A[i][j])
            i = i + 1 ; j = j - 1    
        print('The elements of the secondary diagonal are : ',k,'\n')   
    else : 
        print("For the same reason, we can not also give the secondary diagonal")        
except TypeError : #exception for line and column matrix 
     print("For the same reason, we can not also give the secondary diagonal")   
    
print("The modified matrix with the intermediary steps:")  
try :
    for i in range(len(A[0])) :
        for j in range(len(A[:,-1])) : #Let's traverse all the elements of the Matrix A
            if i == 0 : #Let's traverse the first line...
                if j == 0 : #and first column ...
                    A[i][j] = A[i][j+1] + A[i+1][j]
                if j in range(1,len(A[0]) - 1) : #...the others column excepted the firts and the last...
                    A[i][j] = A[i][j-1] + A[i][j+1] + A[i+1][j]
                if j == len(A[0]) -1 : #Now the last
                    A[i][j] = A[i][j-1] + A[i+1][j]
            if i in range(1,len(A[:,-1]) - 1) : #Let's cross all the others lines exepted the first and the last
                if j == 0 : #The first lines
                    A[i][j] = A[i-1][j]+A[i+1][j]+A[i][j+1]
                if j in range(1,len(A[0]) - 1) : #Let's cross all the others lines exepted the first and the last
                    A[i][j] = A[i][j-1]+ A[i][j+1] + A[i+1][j]+ A[i-1][j]        
                if j == len(A[0])-1 : # Let's cross the last line
                    A[i][j] = A[i][j-1]+ A[i+1][j]+A[i-1][j]  
            if i == len(A[:,-1])-1  :  #Now let's cross te last line
                if j == 0 :  #The first column
                    A[i][j] = A[i][j+1] + A[i-1][j]
                if j in range(1,len(A[0]) - 1) : #The others excepted the first and the last
                    A[i][j] = A[i][j-1] + A[i][j+1]+ A[i-1][j]
            if j == len(A[:,-1])-1 : #The last column
                A[i][j] = A[i][j-1] + A[i-1][j] 
        print(A)
except TypeError : #Let's adjust the programme for line matrix
    for i in range (len(A)):
        if i == 0 :
            A[i] = A[i+1] 
        if i in range(1,len(A) - 1) :
            A[i] = A[i-1] + A[i+1]
        if i == len(A) -1 :
             A[i] = A[i-1]
        print(A)
             
             
            
        

    
