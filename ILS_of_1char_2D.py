# Pure Python 3.6 program (Beginner++)

from random import randint

# Generates a random integer vector according to arguments
def RandIntVec(m = 10, min = 0, max = 1):
    vec = []
    for i in range(int(m)):
        vec.append(randint(int(min), int(max)))
    return vec

# Generates a random matrix according to arguments
def RandIntMat(n = 8, m = 10, min = 0, max = 1):
    mat = []
    for i in range(int(n)):
        mat.append(RandIntVec(m, min, max))
    return mat

# Translates a matrix from Python to math and prints it
def PrintMat(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m-1):
            print("{}, ".format(mat[i][j]), end = "")
        print(mat[i][j+1])
        print("")

def Concat(a, b):
    return str(a)+str(b)

def str_in_vec(str, vec):
    for item in vec:
        if str == item:
            return True
    return False

def SortAndIndex(lst):           # descend
    n = len(lst)
    index = []
    for i in range(n):
        index.append(i)
    for i in range(n-1):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                index[i], index[j] = index[j], index[i]
    return (index, lst)

def SortedSet(sorted_lst, tol = 0):
    n = len(sorted_lst)
    
    vec = []
    count_vec = []
    
    count = 1    
    i = 0

    while i < n-1:
        pivot = sorted_lst[i]
        for j in range(i+1, n):
            if abs(sorted_lst[j] - pivot) <= tol:
                count += 1
            else:
                break
        vec.append(pivot)
        count_vec.append(count)
        i += count
        pivot = sorted_lst[i]                
#        print(pivot, count)
        count = 1
    return [vec, count_vec]

def Incidence(sorted_vec):     # Incidence vector
    n = len(sorted_vec)
    weight_vec = []
    count = 1
    for i in range(1, n):
        if sorted_vec[i] == sorted_vec[i - 1]:
            count += 1
        else:
            weight_vec.append(count)
            count = 1
        if i == n - 1:
            weight_vec.append(count)
    return weight_vec

# Decides the starting place for the island to uncover
def StartIndex(mat, strs_passed):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j]:
                if len(strs_passed) == 0:
                    return [i, j]
                else:
                    check = Concat(i, j)
# Checks whether the place [i,j] is already part of an island
                    if not(str_in_vec(check, strs_passed)):
                        return [i, j]
    return [-1,-1]

# Finds the indexes of all the members of one island
# The vector "strs_passed" is used only as
# to avoid possible conflicts of resources.
# The relevant indexes are uniquely identified
# by a string made of indexes (i,j).
# Every correct element is closed to maximum 4 others.
# Every new correct element will trigger the function-call
# until all the termination conditions are met.
def FindObj(neighbors, strs_passed, mat, i, j):
    if i > 0:
        if mat[i-1][j]:
            if not(str_in_vec(Concat(i-1, j), strs_passed)):
                neighbors.append([i-1, j])
                strs_passed.append(Concat(i-1, j))
                FindObj(neighbors, strs_passed, mat, i-1, j)
    if j > 0:
        if mat[i][j-1]:
            if not(str_in_vec(Concat(i, j-1), strs_passed)):
                neighbors.append([i, j-1])
                strs_passed.append(Concat(i, j-1))
                FindObj(neighbors, strs_passed, mat, i, j-1)
    if i < len(mat)-1:
        if mat[i+1][j]:
            if not(str_in_vec(Concat(i+1, j), strs_passed)):
                neighbors.append([i+1,j])
                strs_passed.append(Concat(i+1, j))
                FindObj(neighbors, strs_passed, mat, i+1, j)
    if j < len(mat[0])-1:
        if mat[i][j+1]:
            if not(str_in_vec(Concat(i, j+1), strs_passed)):
                neighbors.append([i, j+1])
                strs_passed.append(Concat(i, j+1))
                FindObj(neighbors, strs_passed, mat, i, j+1)
#    print(strs_passed)
    return neighbors


mat = RandIntMat(n = 5, m = 10, min = 0, max = 1)

strs_passed = []
indexes = StartIndex(mat, strs_passed)
strs_passed = [Concat(indexes[0], indexes[1])]
neighbors = [[indexes[0], indexes[1]]]
lengths = []

while indexes[0] != -1:
#    print(indexes)
    bricks = FindObj(neighbors, strs_passed, mat, indexes[0], indexes[1]) 
    lengths.append(len(bricks))

    for item in bricks:
        strs_passed.append(Concat(item[0], item[1]))

    indexes = StartIndex(mat, strs_passed)
    neighbors = [[indexes[0], indexes[1]]]
    
#print(len(set(strs_passed)))
#print(lengths)

#print(lengths)
arr = SortAndIndex(lengths)
#print(arr)
sorted_vec = arr[1]
sorted_set = SortedSet(sorted_vec, tol = 0)
#print(sorted_set)

vec = Incidence(sorted_vec)
#print(vec)
count_vec = []
count = 1
vec = []
for i in range(len(sorted_vec)):
    if i > 0:
        if sorted_vec[i] == sorted_vec[i-1]:
            count += 1
        else:
            vec.append(sorted_vec[i-1])
            count_vec.append(count)
            count = 1
vec.append(sorted_vec[len(sorted_vec)-1])
count_vec.append(count)

PrintMat(mat)
#print(count_vec)
#print(vec)
for i in range(len(vec)):
    print("There are {} islands with {} bricks".format(count_vec[i],vec[i]))

