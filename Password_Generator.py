import random
import string
def pass_generate():
    print("=" * 64)
    head = "PASSWORD GENERATOR"
    print(head.center(64))
    print("=" * 64)
    lth = int(input("ENTER THE LENGTH OF THE PASSWORD YOU WANT TO CREATE : "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(lth))
    
    print(f"Your Password : {password}") 
while True:
    pass_generate()
    again = input("Would you like to generate another password (Yes/No) : ").lower()
    if again != "yes":
        print("Exiting...Your Password has been generated.")
        break
