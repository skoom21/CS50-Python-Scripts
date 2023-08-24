def has_valid_length(s):
    # print(2 <= len(s) <= 6)
    return 2 <= len(s) <= 6

def has_valid_start(s):
    # print(s[:2].isalpha())
    return s[:2].isalpha()

def has_valid_end(s):
    count = 0
    while count < len(s):
        c = str(s[count])
        if c.isalpha():
            count += 1
        else:
            break
    # print(count)
    if(count==6):
        return True
    end_part = s[count:]
    # print(end_part)
    # print(end_part.isnumeric() and end_part[0] != '0' and len(end_part) <= 3)
    return end_part.isnumeric() and end_part[0] != '0' and len(end_part) <= 3

def has_no_invalid_characters(s):
    # print(s.isalnum() and s.isupper() and '.' not in s and ' ' not in s)
    return s.isalnum() and s.isupper() and '.' not in s and ' ' not in s

def is_valid(s):
    # print(has_valid_length(s) and has_valid_start(s) and has_valid_end(s) and has_no_invalid_characters(s))
    return has_valid_length(s) and has_valid_start(s) and has_valid_end(s) and has_no_invalid_characters(s)

def main():
        user_input = input("Enter a vanity plate: ")
        if is_valid(user_input):
            print("Valid")
        else:
            print("Invalid")

            
if __name__ == "__main__":
    main()
