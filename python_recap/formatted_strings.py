#formatted strings

name = 'ari'
age = 26

print('hi '+ name + ' you are ' +str(age) + ' years old.')

print(f'Hi {name}, you are {str(age)} years old.') #formatteed strings print(f''')

print('Hii {}, you are {} years old.'.format('ari', '26')) #.format on a sring, python 2 code

print('Hii {}, you are {} years old.'.format(name, age)) # .format alternate types

print('Hii {1}, you are {0} years old.'.format(name, age))  # .format alternate types

