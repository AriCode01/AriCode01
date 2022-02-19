# lists in python

li0 = [0,1,2,3,4,5,6,7,8,9]
li1 = ['a','b','c']
li2 = [1,22.2,'a',True]  #they can store data of different data types

amazon_cart = [
  'notebooks',
  'sunglasses',
  'watches',
  'books',
  'toys',
  'chips'
]

print(amazon_cart[2])

# list slicing using start index, stop index and step over value

print(amazon_cart[0:5:2])

# strings are iummutable but lists are mutable

amazon_cart[0] = 'laptop'
print(amazon_cart)

# once again to emphasize that using list slicing or string slicing or built in
# functions or methods upon lists or strings do not alter the contents of the
# original list , the printed values are taken from dupicate tempiorary lists whic
# were created to execute the operaion stated on the list and return accordingly

# to update the original list only certain functions and assignment directly can do it

############################################################################

### VVI similarity with c, list names like in c points to the list in memory
### so if we try to assign the contents of a list to another using only the names it
### may not work as expecccted

print('#########################################')

new_cart = amazon_cart  # trying to store the values in one list to a sepearte list using only name
new_cart[0] = 'failure'

print(new_cart)
print(amazon_cart)

print('#########################################')