def main():
    text=input("camelCase: ")

    for c in text:
        if(c.isupper()):
            text=text.replace(c,"_"+c.lower())

    print(f"snake_case: {text}")
    ...




if (__name__ == "__main__"):
    main()