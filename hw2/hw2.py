
# import modules
import timeit
import numpy as np
import matplotlib.pyplot as plt
import time

# Question 1 ------

# selection sort
def selectionsort(arr):
    for i in range(len(arr)): # outer loop to traverse array
        minInd = i # minimum index starts at i
        for j in range(i+1,len(arr)): # inner loop begins at i + 1, ends at the end
            if arr[j] < arr[minInd]: # if a smaller value is found
                minInd = j # the minimum index becomes the index that it was found
        if minInd != i: # when the min index changes
            # swap positions so that the minimum index is at the beginning of the inner loop
            temp = arr[i]
            arr[i] = arr[minInd]
            arr[minInd] = temp
    return arr # return the sorted array

# insertion sort
def insertionsort(arr):
    for i in range(len(arr)): # outer loop to traverse array
        j = i # inner loop starts at i
        while(j>0 and arr[j-1]> arr[j]): # while the value at j is greater than min and greater than 0
            # swap
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j-1] = temp
            j -= 1 # j steps back
    return arr # return sorted array

# merge sort
def mergesort(arr):
    n = len(arr) # record array length

    # new arrays for splitting
    left = []
    right = []

    if n <= 1: # when the array length becomes 1, return the array
        return arr

    #split the array into left and right sides
    for i in range(0,n):
        if(i<(n-1)/2):
            left.append(arr[i])
        else:
            right.append(arr[i])

    leftsort = mergesort(left) # take all the left sides
    rightsort = mergesort(right) # take all the right sides

    return merge(leftsort,rightsort) # merge them back together

# helper function for merge sort, merges arrays together in sorted order
def merge(l,r):
    # numbers at the end of the arrays that tell the array to stop merging
    l.append(9999999)
    r.append(9999999)

    D = [] # merged array
    i = j = 0 # start at index 0
    while l[i] < 9999999 or r[j] < 9999999: # while not at the end of either array
        if l[i] < r[j]: # find the lower of the two values in the two arrays
            D.append(l[i]) # add it to the new array
            i = i + 1 # increase index

        else: # same as above
            D.append(r[j])
            j = j + 1
    return D # return merged array





index = [] # array for recording array size


# Question 2 ----

'''
# arrays for holding time values and numbers for sorting
sortedarr = []
reversearr = []
reversearrtwo = []
selectsortedtime = []
selectreversetime = []
insertsortedtime = []
insertreversetime = []
mergesortedtime = []
mergereversetime = []

# how many numbers in the array at the given time; used for incrementing so we don't have to keep making the ordered
# and reverse ordered arrays over and over again
sortedarrayCount = 1
reversearrayCount = 0


for i in range(1, 101): # outer loop; creates arrays of size n = 100 to n = 10000
    index.append(i*100) # add the size of the array currently being created to the list for plotting
    print(i) # progress report; displays the current size being worked on to console
    for j in range(sortedarrayCount,i*100 + 1): # creates the sorted array of size i*100
        sortedarrayCount += 1 # used so that we don't have to keep making new arrays
        sortedarr.append(j) # add the new values up to i*100
    for k in range(i*100, reversearrayCount, -1): # creates the reverse sorted array of size i*100
        reversearrayCount += 1
        reversearrtwo.append(k)
    reversearrtwo.extend(reversearr) # because it is reverse sorted, we need to add the new values to the beginning
    reversearr = list(reversearrtwo) # take that list and prep it for the next iteration i
    reversearrtwo = []


# for this section, make code that you don't want to see on the plot comments
# for example if you want a selection sort plot, make all insertion and merge sort related code comments
# if you just want to compare sorted array times, make all reverse sorted related code comments


#    selectionsorted = list(sortedarr) # duplicate sorted array
    selectionreverse = list(reversearr) # duplicate reverse sorted array
#    ssort = timeit.Timer (lambda: selectionsort(selectionsorted)) # time selection sort for sorted array
    srevt = timeit.Timer (lambda: selectionsort(selectionreverse)) # time selection sort for reverse sorted array
#    selectsortedtime.append(ssort.timeit(number=1)) # add the time to the appropriate array
    selectreversetime.append(srevt.timeit(number=1)) # same


# same as selection sort but for insertion sort

#    insertionsorted = list(sortedarr)
    insertionreverse = list(reversearr)
#    isort = timeit.Timer (lambda: insertionsort(insertionsorted))
    irevt = timeit.Timer (lambda: insertionsort(insertionreverse))
#    insertsortedtime.append(isort.timeit(number=1))
    insertreversetime.append(irevt.timeit(number=1))


# same as selection sort but for merge sort

#    mergesorted = list(sortedarr)
#    mergereverse = list(reversearr)
#    msort = timeit.Timer (lambda: mergesort(mergesorted))
#    mrevt = timeit.Timer (lambda: mergesort(mergereverse))
#    mergesortedtime.append(msort.timeit(number=1))
#    mergereversetime.append(mrevt.timeit(number=1))

# plotting the times
# for this section, make sure to call plot however many times you want to have a function on the graph
# if you want one for forward sort and reverse sort, you call it twice and label both
plt.plot(index, selectreversetime, label='Selection Sort') # selection sort function, blue line
plt.plot(index, insertreversetime, color='r', label='Insertion Sort') # insertion sort function, red line
plt.ylabel('Time') # y axis holds time
plt.xlabel('n') # x axis holds n
plt.title('Average Random Array Sort Time') # title of plot
plt.legend() # display legend
plt.show() # display plot



'''

np.random.seed(101) # seed for random number generator



# Question 4 -----
'''

selectionTotalTime = [] # array to hold all average times for selection sort
insertionTotalTime = [] # array to hold all average times for insertion sort
mergeTotalTime = [] # array to hold all average times for merge sort


for i in range(2, 101, 2): # setup for n = 200 to 10000; n = i*100 for each iteration; only every n = 200

    # arrays to hold the times for 100 permutations at size n
    selectionIndexTime = []
    insertionIndexTime = []
    mergeIndexTime = []


    index.append(i*100) # records n for the plot
    print(i) # progress report printed to console
    arr = np.random.rand(i*100) # generates an array of i*100 random numbers

    # creates 100 permutations for the random array arr and times each algorithm's sorting time for each permutation
    for j in range(0, 100):
        array = np.random.permutation(arr) # duplicate array

        selectionArr = list(array) # duplicate array
        ssort = timeit.Timer (lambda: selectionsort(selectionArr)) # time selection sort
        selectionIndexTime.append(ssort.timeit(number=1)) # add the time to the appropriate array

        # same follows for the next two algorithms
        insertionArr = list(array)
        isort = timeit.Timer (lambda: insertionsort(insertionArr))
        insertionIndexTime.append(isort.timeit(number=1))

        mergeArr = list(array)
        msort = timeit.Timer (lambda: mergesort(mergeArr))
        mergeIndexTime.append(msort.timeit(number=1))

    # variables to add up all the times for index i
    avgSelection = 0
    avgInsertion = 0
    avgMerge = 0

    # add up everything for each algorithm
    for k in range(0, 100):
        avgSelection += selectionIndexTime[k]
        avgInsertion += insertionIndexTime[k]
        avgMerge += mergeIndexTime[k]

    # calculate averages and add them to the average time array to be plotted
    selectionTotalTime.append(avgSelection/100)
    insertionTotalTime.append(avgInsertion/100)
    mergeTotalTime.append(avgMerge/100)

print('%s seconds' % (time.time() - start ))

# plotting using matplotlib

plt.plot(index, selectionTotalTime, label='Selection Sort') # selection sort function, blue line
plt.plot(index, insertionTotalTime, color='r', label='Insertion Sort') # insertion sort function, red line
plt.plot(index, mergeTotalTime, color='g', label='Merge Sort') # merge sort function, green line
plt.ylabel('Time') # y axis holds time
plt.xlabel('n') # x axis holds n
plt.title('Average Random Array Sort Time') # title of plot
plt.legend() # display legend
plt.show() # display plot
'''

'''
# Question 5 ----
arr = np.random.rand(1000000) # generate the array with n = 10^6 random numbers



selectionarr = list(arr) # duplicate array
selectionstart = time.time() # start time
selectionsort(selectionarr) # selection sort it
print('%s seconds selection' % (time.time() - selectionstart )) # print the time it took by current time - start time

# same but for insertion sort
insertionarr = list(arr)
insertionstart = time.time()
insertionsort(insertionarr)
print('%s seconds insertion' % (time.time() - insertionstart ))


# same but for merge sort
mergearr = list(arr)
mergestart = time.time()
mergesort(mergearr)
print('%s seconds merge' % (time.time() - mergestart ))
'''