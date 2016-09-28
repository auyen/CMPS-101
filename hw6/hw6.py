# Q1

# Class for Node object
# Inserting an item into the BSTree creates a node object that stores information
class Node:
    # constructor
    # takes key, value, the node's parent, and its left and right children
    def __init__(self, key, value, parent, left, right):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    # Returns true if the node has a left child, else false
    def hasLeftChild(self):
        if self.left == None:
            return False
        else:
            return True

    # Returns true if the node has a right child, else false
    def hasRightChild(self):
        if self.right == None:
            return False
        else:
            return True

    # REturns true if the node is a right child of its parent
    def isRightChild(self):
        if self.parent.right == self:
            return True
        else:
            return False

    # Returns true if the node is a left child of its parent
    def isLeftChild(self):
        if self.parent.left == self:
            return True
        else:
            return False

    # Returns true if the node has no children
    def isLeaf(self):
        if (self.hasLeftChild() is True) or (self.hasRightChild() is True):
            return False
        else:
            return True

    # Returns true if the node has children
    def isParent(self):
        if self.hasLeftChild() or self.hasRightChild():
            return True
        else:
            return False

    # Returns true if the node has two children
    def hasTwoChildren(self):
        if self.hasLeftChild() and self.hasRightChild():
            return True
        else:
            return False

    # Returns true if the node is the root of the tree
    def isRoot(self):
        return not self.parent

    # Deletes the data from the node
    def delete(self):
        self.key = None
        self.value = None
        self.parent = None
        self.left = None
        self.right = None

# Class for the Binary Search Tree
# Takes and manipulates node objects
class BSTree:
    # constructor
    def __init__(self):
        self.size = 0 # records the size of the tree
        self.root = None # points to the root of the tree



    # inserts a node containing the key and value specified
    def insert(self, key, value):
        if self.root == None: # if the tree is empty, the first node is the root
            self.root = Node(key, value, None, None, None)
            self.size += 1
        else:
            # Determine the location of the node for placement
            currentNode = self.root # start from the root
            while(True):
                # if the key is already in the tree, add one to the node's value
                if key == currentNode.key:
                    currentNode.value += 1
                    break

                # if the key is smaller than the current key, move down its left side and keep comparing
                if key < currentNode.key and currentNode.hasLeftChild():
                    currentNode = currentNode.left
                    continue
                # if larger, move down its right side
                if key > currentNode.key and currentNode.hasRightChild():
                    currentNode = currentNode.right
                    continue

                # when an appropriate empty spot is found, add the node there and increment the size
                if key < currentNode.key and not currentNode.hasLeftChild():
                    currentNode.left = Node(key, value,currentNode,None,None)
                    self.size += 1
                    break
                # same as above
                if key > currentNode.key and not currentNode.hasRightChild():
                    currentNode.right = Node(key, value,currentNode,None,None)
                    self.size += 1
                    break


    # returns the node with the given key
    def find(self,key):
        result = self.findKey(key,self.root)
        return result

    # helper function for find
    # recursively searches and returns the node with the given key
    def findKey(self,key,currentNode):

        # if the node with the right key is found, return the node
        if key == currentNode.key or currentNode.key == None:
            return currentNode
        # if the key is smaller than the current node, move down its left side
        if key < currentNode.key and currentNode.hasLeftChild():
            return self.findKey(key,currentNode.left)
        # if larger, then right side
        if key > currentNode.key and currentNode.hasRightChild():
            return self.findKey(key,currentNode.right) 

    # returns the successor node to a particular node given its key
    def successor(self,key):
        suc = None
        result = self.find(key) # First find the node 
        if result == None: # If node is not in tree, return None
            return result
        else: # Else 
            if result.hasRightChild(): # If the found node has a right child
                suc = self.findMin(result.right) # Find the min of the right child
            else: # Else if the node does not have a right child 
                if result.isLeftChild(): # If the current node is the left child of the
                    suc = result.parent # The successor is the parent
                else: # If the node is the right child
                    suc = result
                    # Find the successor of the parent
                    while(True):
                        suc = suc.parent
                        if suc.key < suc.parent.key:
                            return suc.parent
                        if suc == self.root:
                            return self.root
            # If the node is the right-most node of the tree, there is no successor
            if result.isLeaf() and (result.key > self.root.key) and result == result.parent.right:
                suc = None
        return suc


    # helper function for successor
    # returns the leftmost node for a branch
    def findMin(self,currentNode):
        while currentNode.hasLeftChild():
            currentNode = currentNode.left
        return currentNode


    # deletes the node with the specified key
    # maintains the binary search tree properties
    def delete(self,key):

        # find the key
        result = self.find(key)

        # if the key isn't in the tree, return None
        if result == None:
            return

        # delete according to the cases
        else:
            currentNode = result

            # if the node is a leaf, delete it and set its parent's child pointer to None
            if currentNode.isLeaf() and (currentNode.isLeftChild or currentNode.isRightChild):
                if currentNode.parent == None:
                    return
                if currentNode == currentNode.parent.left:
                    currentNode.parent.left = None
                    currentNode.delete()
                elif currentNode == currentNode.parent.right:
                    currentNode.parent.right = None
                    currentNode.delete()

            # if the node has children
            elif currentNode.isParent():

                # if the node has two children
                if currentNode.hasTwoChildren():

                    # normally, the successor is the leftmost leaf on the node's right branch
                    successor = self.successor(currentNode.key)
                    currentNode.key = successor.key
                    currentNode.value = successor.value


                    # if it's the root, the successor is the immediate right child
                    if successor.hasLeftChild():
                        currentNode.left = successor.left
                    if successor.hasRightChild():
                        currentNode.right = successor.right

                    # move the successor to the position of the node to be deleted
                    # change the pointers of the successor so that its parent's appropriate child node points to its
                    #   children so that the move maintains the tree
                    if successor.isLeaf() and successor.parent.left == successor:
                        successor.parent.left = None

                    elif successor.isLeaf() and not successor.parent.left == successor:
                        successor.parent.right = None

                    else: # if it's the root
                        successor = None

                # if the node only has a left child
                elif currentNode.hasLeftChild():

                    left = currentNode.left
                    # set its child to take its place by modifying its parent's and child's pointers to point to each
                    #   other
                    if currentNode.parent.left == currentNode:
                        currentNode.parent.left = currentNode.left
                        currentNode.left.parent = currentNode.parent

                    elif currentNode.parent.right == currentNode:
                        currentNode.parent.right = currentNode.right
                        currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                    currentNode.left.parent = currentNode.parent

                    # remove the pointers from the deleted node
                    if currentNode.left.isLeaf():
                        currentNode.left = None

                    currentNode.key = left.key
                    currentNode.value = left.value

                # if it only has a right child, do the same as the left child case
                elif currentNode.hasRightChild():

                    right = currentNode.right

                    if currentNode.parent.left == currentNode:
                        currentNode.parent.left = currentNode.right
                        currentNode.right.parent = currentNode.parent

                    elif currentNode.parent.right == currentNode:
                        currentNode.parent.right = currentNode.right
                        currentNode.right.parent = currentNode.parent

                    if currentNode.right.isLeaf():
                        currentNode.right = None

                    currentNode.key = right.key
                    currentNode.value = right.value

    # prints the entire tree in order
    def inOrderTraversal(self):
        self.TraverseHelp(self.root)

    # helper function for inOrderTraversal
    # moves recursively across the tree and prints
    def TraverseHelp(self,currentNode):
        if currentNode == None:
            return
        self.TraverseHelp(currentNode.left)
        print(currentNode.key, currentNode.value)
        self.TraverseHelp(currentNode.right)

    # adds all the values of the tree to an array
    def inOrderTraversalValue(self):
        arr = []
        self.TraverseHelpValue(self.root,arr)
        return arr

    # helper function for inOrderTraversalValue
    def TraverseHelpValue(self,currentNode,arr):
        if currentNode == None:
            return
        self.TraverseHelpValue(currentNode.left,arr)
        arr.append(currentNode)
        self.TraverseHelpValue(currentNode.right,arr)


'''
# Q2
import heapq 
m = open('finefoods_cleaned.txt') # Opens text file with the reviews  
stop = open('stopwords.txt') # Opens text file with the stopwords  
bad = set() # Creates set for the stopwords   

for line in stop: # For each line in the stopwords file  
   f = line.replace('\n', '') # Get rid of the newline character 
   bad.add(f) # Place word inside of the stopword set 

# Create 2 trees, one for high ratings and the other for low ratings
highTree = BSTree() 
lowTree = BSTree()

for line in m: # For each line in the reviews
    all = [] 
    all = line.split(':') # Split the line into the rating and the review and place into all
    if (int(all[0]) > 3): # If the rating is greater than 3, set high to True
        high = True
    else: # Else set High to false
        high = False
    for word in all[1].split(): # For each word in the review
        if word in bad: # If the word is in the bad set, skip it
            continue
        if high: # If high is true, insert word into the high review tree
            highTree.insert(word,1)
        else: # Else, insert word into the low tree
            lowTree.insert(word,1)


# Q3
# Same as Q2
m = open('finefoods_cleaned.txt')
stop = open('stopwords.txt')
bad = set()

for line in stop:
   f = line.replace('\n', '')
   bad.add(f)

highTree = BSTree()
lowTree = BSTree()
for line in m:
    all = []
    all = line.split(':')
    if (int(all[0]) > 3):
        high = True
    else:
        high = False
    for word in all[1].split():
        if word in bad:
            continue
        if high:
            highTree.insert(word,1)
        else:
            lowTree.insert(word,1)


# Array of words to search for
w = ["asymptotic", "binary", "complexity", "depth", "mergesort", "quicksort", "structure", "theta"]

# Search the high review tree
print("High Tree: ")
for i in range(len(w)): # For each word in the w array
    print(w[i])
    a = highTree.find(w[i]) # Find the word in the tree
    if a == None: # If it is not found
        print("Frequency = 0")
        highTree.insert(w[i], 1) # Insert the word
        b = highTree.successor(w[i]) # Find the successor of the word
        print("Successor = %s" % (b.key))
        highTree.delete(w[i]) # Delete the word from the tree
    else:
        print("Frequency = %d" % (a.value))

print("--------------------")

# Search the low review tree
print("Low Tree: ")
for i in range(len(w)): # For each word in the w array
    print(w[i])
    a = lowTree.find(w[i]) # Find the word in the tree
    if a == None: # If it is not found
        print("Frequency = 0") 
        lowTree.insert(w[i], 1) # Insert the word
        b = lowTree.successor(w[i]) # Find the successor of the word
        print("Successor = %s" % (b.key))
        lowTree.delete(w[i]) # Delete the word from the tree
    else:
        print("Frequency = %d" % (a.value))


import heapq
# Q4

a = [] # array to hold the tuples from the high rating tree
b = [] # array to hold the tuples from the low rating tree


arrHigh = highTree.inOrderTraversalValue() # hold the contents of the high rating tree

# add the value, key pairs to the array
# because heapq only works well for min heaps and we want a max heap, turn the values to negative
# we will print a positive value
for i in range(0, len(arrHigh)):
    a.append((-arrHigh[i].value, arrHigh[i].key))

# same follows for the low rating tree
arrLow = lowTree.inOrderTraversalValue()
for i in range(0, len(arrLow)):
    b.append((-arrLow[i].value, arrLow[i].key))


af = [] # holds the top twenty for the high rating tree
bf = [] # holds the top twenty for the low rating tree
cf = [] # holds the top twenty for the new tree

# heapify each array
heapq.heapify(a)
heapq.heapify(b)

frequent = open("frequent.txt","w") # open the file for output
frequent.write("High Rating: \n")
frequent.write("\n")

# get the top twenty values for the high rating and print them in the file
for i in range (0,20):
    af.append(heapq.heappop(a))
    frequent.write("%s, %d" %(af[i][1], -af[i][0]))
    frequent.write("\n")

# formatting
frequent.write("\n")
frequent.write("----------\n")
frequent.write("\n")
frequent.write("Low Rating: \n")
frequent.write("\n")

# same for the low rating tree
for i in range (0,20):
    bf.append(heapq.heappop(b))
    frequent.write("%s, %d" %(bf[i][1], -bf[i][0]))
    frequent.write("\n")



# start the new one, which is when you delete everything on the low tree from the high tree
for j in range(0,len(arrLow)):
    key = arrLow[j].key
    highTree.delete(key)

arrHigh = highTree.inOrderTraversalValue()

# formatting
frequent.write("\n")
frequent.write("----------\n")
frequent.write("\n")
frequent.write("Distinct words after deleting words from low rating tree: ")
frequent.write("%d\n" %(len(arrHigh)))
frequent.write("\n")
frequent.write("----------\n")
frequent.write("\n")

c = []
frequent.write("\n")
frequent.write("New Top Twenty Frequency Words: \n")
frequent.write("\n")

# add the remaining words
for i in range(0, len(arrHigh)):
    if not arrHigh[i].value == None:
        c.append((-arrHigh[i].value, arrHigh[i].key))

# heapify and print the top twenty
heapq.heapify(c)
for k in range(0,20):
    crs = heapq.heappop(c)
    while(True):
        if k > 0 and cf[k-1] == crs:
            crs = heapq.heappop(c)
        break
    cf.append(crs)
    frequent.write("%s, %d" %(cf[k][1], -cf[k][0]))
    frequent.write("\n")

'''