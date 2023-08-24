import sys
import random
from pyfiglet import Figlet 

def main ():
    figlet= Figlet()
    font = figlet.getFonts()
    # print(font)
    
    if len(sys.argv) == 1:
        text = input("Input: ")
        rfont = random.choice(font)
        figlet.setFont(font= rfont)
        print("Output:\n",figlet.renderText(text))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in font:
                text = input("Input: ")
                figlet.setFont(font= sys.argv[2])
                print("Output:\n",figlet.renderText(text))
            else:
                sys.exit("Error: Font not found")
        else:
            sys.exit("Error: Invalid argument")
    else: 
        sys.exit("Error: Invalid argument")
        
    
    
    
    ...
    
    
    
if __name__ == "__main__":
    main()