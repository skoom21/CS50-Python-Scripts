
def main():
    
    text=input("Input: ")
    text = shorten(text)
    print(f"Output: {text}")
    
    
def shorten(text):
    vowels = "aeiou"
    for char in text:
        if char in vowels:
            text = text.replace(char,"")
    
    return text

if (__name__ == "__main__"):
    main()