import re

#implementing a function check password strenght

def check_password_strenght(password):

    """
    check the strength of a given password based on defined criteria

    Args:
    password (str): The password to be checked

    Returns:
    bool: True if the password meets all criteria, False otherwise
    """

    # Check if the password is not blank
    if not password:
        return False

    #First criteria: minimum length of the password should be atleast 8 characters long
    if len(password) < 8:
        return False
    
    #Second criteria: check for uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]',password):
        return False
    
    #Third criteria: check for atleast one digit
    if not re.search(r'[0-9]',password):
        return False
    
    #Fourth criteria: check for atleast one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        return False
    
    #if all criteria meets
    return True

# Defining main function to take user input for a password and validate it with given criteria
# Additionally it should also provide feedback based on password strength

def main():

    #Take user input for the password
    password = input("Enter a password to check its strength:")

    #Validate the password using check_password_strength function
    if check_password_strenght(password):
        print("The password is strong.")

    else:
        print("The password is not strong enough or the password is blank")
        print("Please ensure it meets the following criteria:")
        print("1) Atleast 8 characters long")
        print("2) Contains both uppercase and lowercase letters")
        print("3) Contains atleast one digit (0-9)")
        print("4) Contains atleast one special character (e.g., !, @, #, $,%)")  
        
if __name__=="__main__":
    main()       
