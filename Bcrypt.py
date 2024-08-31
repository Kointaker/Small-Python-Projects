import bcrypt
from Password_Database import users
# The password to be hashed (in bytes)
#password = b"12121212"

# Generating a salt
#salt = bcrypt.gensalt()

# Hash the password with the generated salt
#hashed_password = bcrypt.hashpw(password, salt)

# the password "12121212" in it's hashed form
#print(hashed_password)

# Asking the user to put the password
#user = input("Please enter your password: ")

# Checking to see if the password is correct
#if bcrypt.checkpw(user.encode(), hashed_password):
    #print("Password is correct!")
#else:
 #   print("Password is incorrect!")

# Encode converts the user input to bytes so it 
# Can be used with bcrypt

# User-Search
def search(user, password):
    pas = users.get(user)
    if pas == password:
        print("correct!")


# Password database
choice = int(input("Returning user? (1-Yes, Any Other Key-No): ")) 

# User Verification
if choice == 1:
    user = input("Enter the username: ")
    password = input("Enter the password: ")
    print(search(user, password))



if choice == 16:
    print("Admin panel")
     
# User creation    
else:   
    
    