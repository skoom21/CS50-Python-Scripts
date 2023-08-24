
import emoji

def main ():
    alias = input("Input: ")
    if " " in alias:
        alias=alias.split(" ")
        if "_" in alias[1]:
            print(f"Output: {alias[0]}", emoji.emojize(alias[1]))
        else:
            print(f"Output: {alias[0]}", emoji.emojize(f"{alias[1]}",language="alias"))    
    else:
        if "_" in alias:
            print(f"Output: {emoji.emojize(alias)}")
        else:
            print(f"Output: {emoji.emojize(f'{alias}',language='alias')}")

        
        
        
if __name__ == "__main__":
    main()