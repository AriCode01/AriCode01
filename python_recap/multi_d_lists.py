# Matrices or 2 diamentional lists or multi diamentional lists

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matrix[0][1])

#-----------------------adding-------------------------------------------------
# adding elements to a multi dimensional list using methods .append and .insert

matrix.append([100,101])  # .append(val) method changes the list in place

matrix.insert(3,999)      # .insert(pos,val) method insert a given value at pos in a list

matrix[2].insert(2,500)   # but for multidimensional list if we need to insert or
                          # append something we need the entire adrress of the
                          # internal list to which we are inseting or appending

matrix[0].append([-1,-2]) # testing abouve hypothesis

print(matrix)

#------------------------removing-----------------------------------
# removing elemts from list using .pop() .clear() .remove() methods

matrix.pop()       # by default pops from the end and returna popped value
print(matrix)

popped = matrix.pop(0)  # .pop(index) will pop and rerturn the value at given index
print(matrix)
print(popped)

removed = matrix.remove(999)  # .remove(val) will remove the first occurance of an
                              # element in list, returns null
print(matrix)
print (removed)

matrix.clear()  # clears the entire list from the memory
print(matrix)

#----------------------important points---------------------------------------

# python lists both uni/multi dimensional unlike c arrays can store values of 
# dissimilar data types withou any problem, list name point to list in memeory
# and indexing must be accurate to access/modify individual elements

###############################################################################