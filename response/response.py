import validators


def main ():
    # Check if the input is a valid email address
    print( validate(input("What's your email address? ")))
    
def validate (email):        
    if validators.email(email):
        return("Valid")
    else:
        return("Invalid")


if __name__ == "__main__":
    main()