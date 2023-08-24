

def main():
    question= input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    question = question.replace(" ","")
    match question:
        case "42" | "fortytwo" | "forty-two":
            print("Yes")
        case _:
            print("No")


main()
