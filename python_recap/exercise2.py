#to accept an user ID and password and print the lenght of the password
userID = input('Enter Your UserID: ')
password = input('Enter Your Password: ')

password_len = len(password)
encrypted_pass = '*' * password_len

print(f'Hey {userID}, your password, {encrypted_pass}, is {password_len} letters long.')