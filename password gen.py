import random
import string

print("Password Generator")
def main():
    
    length = int(input("Enter the Length of password"))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbols = string.punctuation
    combine = lower+upper+digit+symbols
    x = random.sample(combine,length)
    password ="".join(x)
    print(password)
    main()
main()