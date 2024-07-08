password = input("What is your password")
key = int(input("What is your shift key"))
password = password.upper() #converting all into uppercase
password = list(password)
for x in range(len(password)):              #converting each element to ascii code
     password[x] = ord(password[x])
print(password)

#shifting the ascii value with key
#think of using queue?
for x in range(len(password)):
     password[x] = password[x] + key
     
     if password[x] > 90: #limit
          password[x] = password[x] - 26 # loop

     password[x] = chr(password[x]) # converts back to letters
print(password)