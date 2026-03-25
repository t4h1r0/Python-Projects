import random

#Character list
lowerchars = ['a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upperchars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

specialchars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '?', '/', '.', ',']

numericchars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = random.choice(lowerchars) + random.choice(upperchars) + random.choice(specialchars) + random.choice(numericchars)

password = password + password

#Password generator function
def password_generator(length, use_lowerchars, use_upperchars, use_specialchars, use_numericchars):
    
    characters = lowerchars[:]  #copy the list, starting with lowercase letters

    if use_upperchars:
        characters += upperchars        #add uppercase letters
    if use_numericchars:
        characters += numericchars      #add numbers
    if use_specialchars:
        characters += specialchars      #add special characters

    #Pick random characters from the character list
    password_chars = []                 #empty list, to hold chosen characters
    for i in range(length):
        random_char = random.choice(characters)
        password_chars.append(random_char)

    #Join the list into a single string
    password = ''.join(password_chars)
    return password

#Main program
def main():
    print("Pasword-Generator")
    print("=" * 40)

    #Get password length
    while True:
        try:
            length = int(input("Enter password length (8-64): "))
            if 8 <= length <= 64:
                break
            else:
                print("Please enter a number between 8 and 64.")
        except ValueError:
            print("Please enter a valid number.")

    #Ask about character types
    use_upperchars = input("Include UPPERCASE letter? (y/n): ").lower() == "y"
    use_numericchars = input("Include DIGITS (0-9)? (y/n): ").lower() == "y"
    use_specialchars = input("Include SPEACIAL characters (!,@,#,$...)? (y/n): ").lower() == "y"

    #Ask how many passwords to generate
    while True:
        try:
            count = int(input("How many passwords would you like to generate? (1-10): "))
            if 1 <= count <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")

    
    print("Your generated passwords: ")
    print("=" * 40)

    passwords = []          #list to store genertated passwords

    #Generate and display the passwords
    for i in range(count):
        psw = password_generator(length, use_upperchars, use_upperchars, use_numericchars, use_specialchars)
        passwords.append(psw)
        print(f"  {i+1}. {psw}")

    print("=" * 40)
    print(f"\n {count} password(s) generated successfully! ")
    
#Run the program
main()   







