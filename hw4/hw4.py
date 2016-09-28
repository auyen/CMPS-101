import timeit
import numpy as np
import matplotlib.pyplot as plt
import scipy


# Q1
# multiplies two matrices together
# this is the O(n^2) algorithm
def matmult(A,x):
   if len(A) != len(x): # if the two matrices are not of the same size
      print ("Not same length")
      return
   p = []
   for i in range (len(x)): # calculate using equation 1 described in the homework
      m = 0
      for j in range (len(x)):
         m = m + (A[i][j] * x[j])

      p.append(m) # add it to the array to be returned
   return p


# Q2
# generates a hadamard matrix of size 2^k by 2^k
def hadmat(k):
    arr = np.array([[1]]) # base
    for i in range(0, k): # start adding on to the matrix
        if len(arr) >=2: # if the size is at least 2
            # concatenate two arr arrays together and one arr with a negative arr
            # then concatenate the resulting arrays
            arr = np.concatenate(((hadmatconcat(arr,arr)), hadmatconcat(arr,-arr)), axis=0)
        if len(arr) == 1: # if the size is 1 just concatenate without worrying about dimensions
            arr = np.concatenate((np.concatenate((arr, arr)), np.concatenate((arr, -arr))), axis=0)
            arr = np.reshape(arr, (-2,2))
    return arr


# concatenates two multidimensional arrays
# say that array A and array B are arrays of arrays
# we do this so that the array at A[i] can join with B[i] rather than just attach B to the end of A
def hadmatconcat(A,B):
    C = []
    for i in range(0, len(A)):
        C.append([np.concatenate(([A[i],B[i]]), axis = 0)]) # concatenate each index
    s = C[0]
    for i in range(1, len(C)):
        s = np.concatenate((s,C[i]),axis=0) # condense everything into one matrix
    return s



# Q4
# multiplies a matrix x with the Hadamard matrix H
def hadmatmult(H, x):

    # split x into halves
    n = len(x)
    h = len(H)
    if n == 2: # base
        return np.array([(x[0] + x[1]),(x[0]- x[1])])
    half = n//2
    left = x[:half]
    right = x[half:]

    # keep splitting until the size of x is 2
    leftadd = hadmatmult(hadmat(int(np.log2(np.sqrt(h))-1)),left)
    rightadd = hadmatmult(hadmat(int(np.log2(np.sqrt(h))-1)),right)
    return hadmatmerge(leftadd,rightadd) # merge the two arrays by adding

# merges two arrays together by adding on top and subtracting on bottom and concatenate
# equation 2 on the homework
def hadmatmerge(B,C):
    D = np.array(B+C)
    E = np.array(B-C)
    F = np.concatenate((D, E), axis=0)
    return F.flatten()




# Extra Credit
# multiplies a matrix x with the Hadamard matrix H efficiently
# does not generate the Hadamard matrix every time it is called

def efficienthadmatmult(x):

    # split x into halves
    n = len(x)
    if n == 2: # base
        return np.array([(x[0] + x[1]),(x[0]- x[1])])
    half = n//2
    left = x[:half]
    right = x[half:]

    # keep splitting until the size of x is 2
    leftadd = efficienthadmatmult(left)
    rightadd = efficienthadmatmult(right)
    return efficienthadmatmerge(leftadd,rightadd) # merge the two arrays by adding

# merges two arrays together by adding on top and subtracting on bottom and concatenate
# equation 2 on the homework
def efficienthadmatmerge(B,C):
    D = np.array(B+C)
    E = np.array(B-C)
    F = np.concatenate((D, E), axis=0)
    return F.flatten()

'''
# Q5
# recording run time
index = [] # array holding n values
hadmattimes = [] # array holding time it takes for hadmat to run with len(x) = n
mattimes = [] # array holding time it takes for matmult to run with len(x) = n

# try each function with n = 2^1 to 2^12
for i in range (1, 13):
   print(i)
   index.append(2**i) # n = 2^i
   rand = np.random.randint(11,size=2**i) # generate array with random numbers to be multiplied with Hadamard
   hmad = timeit.Timer (lambda: hadmatmult(hadmat(i),rand)) # time hadmatmult
   hadmattimes.append(hmad.timeit(number=1))
   mmad = timeit.Timer (lambda: matmult(hadmat(i),rand)) # time matmult
   mattimes.append(mmad.timeit(number=1))

# Plot the times
plt.plot(index, hadmattimes, color='b', label='hadmatmult')
plt.plot(index, mattimes, color='r', label='matmult')
plt.ylabel('Time')
plt.xlabel('n')
plt.title('Matrix Multiplication Time')
plt.legend()
plt.show()
'''
