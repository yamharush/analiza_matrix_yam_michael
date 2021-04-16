'''
authors:
yam harush 318886058
michael harush 208829085
'''
def determinanta(mat):
    '''
    determinanta function
    :param mat: matrix
    :return: the determinanta of the matrix
    '''
    if len(mat)==2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    sum = 0
    for i in range(len(mat)):
        #The first line
        new_mat=list()
        for j in range(len(mat)-1):
            #add lines to the new matrix
            new_mat.append(list())
        for k in range(1,len(mat)):
            for p in range(len(mat)):
                #take all the argument that isn't in my line or rowes
                if p!=i:
                    new_mat[k-1].append(mat[k][p])
        if mat[0][i]%2==0:
            #in the even places there is +
            sum+=mat[0][i]*determinanta(new_mat)
        else:
            #in the odd places there is -
            sum-=mat[0][i]*determinanta(new_mat)
    return sum

def find_elementary(mat,i,j):
    '''
    find_elementary function
    :param mat: matrix
    :param i: the row index
    :param j: the cols index
    :return: the matrix that reset the matrix in the place i,j
    '''
    new_mat=list()
    for k in range(len(mat)):
        new_mat.append(list())
        for p in range(len(mat)):
            if k==p:
            #if the argument on the diagonal
                new_mat[k].append(1)
            else:
            #if the argument not on the diagonal
                new_mat[k].append(0)
    new_mat[i][j]=-(mat[i][j]/mat[j][j])
    return new_mat

def multy_matrix(mat1,mat2):
    '''
    multy_matrix function
    :param mat1: matrix 1
    :param mat2: matrix 2
    :return: the multy of the 2 matrix
    '''
    new_mat=list()
    sum=0
    for i in range(len(mat1)): #rows
        new_mat.append(list()) #cols
        for j in range(len(mat2)):
            for k in range(len(mat2)):
                sum+=mat1[i][k]*mat2[k][j] #add to the sum
            new_mat[i].append(sum)
            sum=0
    return new_mat

def unit_function(size):
    '''
    unit_function function
    :param size: the size of the matrix that we want
    :return: the unit matrix for this size
    '''
    new_mat = list()
    for k in range(size):
        new_mat.append(list())
        for p in range(size):
            if k == p:
                # if the argument on the diagonal
                new_mat[k].append(1)
            else:
                # if the argument not on the diagonal
                new_mat[k].append(0)
    return new_mat

def complements_one(mat):
    '''
    complements_one function
    :param mat: matrix
    :return: the matrix that if we will multy between her and the matrix we get we complete to 1
    '''
    new_mat=unit_function(len(mat))
    for k in range(len(mat)):
        if(mat[k][k]!=1):
            new_mat[k][k]=1/mat[k][k]
    return new_mat

def matrix_u(mat):
    '''
    matrix_u function
    :param mat: matrix
    :return: the upper matrix of this matrix
    '''
    new_mat=unit_function(len(mat))
    for i in range(len(mat)):
        for j in range(i):
            temp = find_elementary(mat, i, j)
            mat = multy_matrix(temp, mat)
            new_mat = multy_matrix(temp, mat)
    return mat

def matrix_L(mat):
    '''
    matrix_L function
    :param mat: matrix
    :return: the lower matrix of this matrix
    '''
    new_mat=unit_function(len(mat))
    for i in range(len(mat)):
        for j in range(i):
            temp = find_elementary(mat, i, j)
            mat = multy_matrix(temp, mat)
            if temp[i][j] != 0:
                new_mat[i][j] = -temp[i][j]
    return new_mat

def reverse_matrix(mat):
    '''
    reverse_matrix function
    :param mat: matrix
    :return: the reverse matrix of the matrix we get
    '''
    new_mat=unit_function(len(mat))
    pivoting_mat=unit_function(len(mat))
    for i in range(len(mat)):
        pivoting_mat = change_lines(mat,i)
        for j in range(i):
            temp = find_elementary(mat, i, j)
            pivoting_mat=multy_matrix(pivoting_mat,temp)
            mat = multy_matrix(temp, mat)
            new_mat = multy_matrix(temp, new_mat)
    for i in range(len(mat)):
        for j in range(i+1,len(mat)):
            temp = find_elementary(mat, i, j)
            mat = multy_matrix(temp, mat)
            new_mat = multy_matrix(temp, new_mat)
    for i in range(len(mat)):
        temp=complements_one(mat)
        mat=multy_matrix(temp,mat)
        new_mat=multy_matrix(temp,new_mat)
    return new_mat

def multy_matrix_vector(mat,vector):
    '''
    multy_matrix_vector function
    :param mat: matrix
    :param vector: vector
    :return: the multy between the matrix and the vector
    '''
    new_mat=list()
    sum=0
    for i in range(len(mat)): #rows
        new_mat.append(list()) #cols
        for j in range(len(vector[0])):
            for k in range(len(vector)):
                sum += mat[i][k]*vector[k][j] #add to the sum
            new_mat[i].append(sum)
            sum=0
    return new_mat

def change_lines(mat,indexOfCol):
    '''
    change_lines function
    :param mat: matrix
    :param indexOfCol: index of the cols
    :return: chck if the pivot is the biggest in the col, if he isn't change the places
    '''
    new_mat=unit_function(len(mat))
    temp1=0
    temp2=0
    for k in range(indexOfCol+1,len(mat)):
        if mat[k][indexOfCol]>mat[indexOfCol][indexOfCol]:
            temp1=k
    if temp1!=0:
        temp2=new_mat[indexOfCol]
        new_mat[indexOfCol]=new_mat[temp1]
        new_mat[temp1]=temp2
    return new_mat

def main():
    mat1 = [[1, 2, 1],
            [2, 6, 1],
            [0, 0, 0]]

    mat2=[[1,2],
            [2,3]]


    b = [[5], [7]]
    
    if determinanta(mat1)!=0:
        print("The matrix is reversible the calculate of A^(-1)*b is:")
        print(multy_matrix_vector(reverse_matrix(mat1),b))
    else:
        print("The matrix is irreversible,the LU decomposition is:")
        print("U matrix:",matrix_u(mat1))
        print("L matrix:",matrix_L((mat1)))
    if determinanta(mat2) != 0:
        print("The matrix is reversible the calculate of A^(-1)*b is:")
        print(multy_matrix_vector(reverse_matrix(mat2), b))
    else:
        print("The matrix is irreversible,the LU decomposition is:")
        print("U matrix:", matrix_u(mat2))

if __name__ == "__main__":
    main()
