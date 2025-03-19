import random
import string

def generate_password(length, use_special_chars=True):
    """Generate a random password of a specified length"""
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combining character sets based on user preferences
    all_characters = lowercase + uppercase + digits
    if use_special_chars:
        all_characters += special_chars
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    # Get user input for password length and complexity
    try:
        length = int(input("Enter the desired password length: "))
        
        if length < 6:
            print("It's recommended to have a password length of at least 6 characters.")
            return
        
        use_special_chars = input("Include special characters (Y/N)? ").lower() == 'y'
        
        # Generate and display the password
        password = generate_password(length, use_special_chars)
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()