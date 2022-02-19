selfish = '0123456789'

print(selfish[1])

print(selfish)

print(selfish[3:8])  # stringname[start : stop]

print(selfish[0:9:3]) # stepping over ----> stringname[start_index : stop_index : step_oer_by_no_of_index]

print(selfish[-1]) #using negative indx starts the traversal from the end

print(selfish[::-1]) # using stepping over no as -1 or negative reveres the order of stepping over

# stings in python are immmutable, we can not ater/reassign a part of a string, to chamge it will have 
# to be updated entirely, just luike in c, python does not support altering choosen parts of a string

a = len(selfish)  #len is a bulit in function on strings which return length
print (a)

quote = 'to be or not to be'

print(len(quote))  # len(string_name) is the syntax for a function

print(quote.upper())  # pthon also offers various methods --> string_name.method()

print(quote.capitalize())  # string_name.format() used in formatted_strings code is also a method


#dealing with immutability -----> stings are immutable and therefore we cant change only certain parts of it, the  enitrituy has to be  midified

quote = quote.replace('be','me')  # temporarily creating a new string using the quote stings with certain parts replaced and then assigning the new string to qoute basically overwriting the variable quote

print (quote)
