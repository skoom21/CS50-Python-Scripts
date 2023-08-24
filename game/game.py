import random

def main():
    
    while True:
        level = input("Level: ")
        if level.isnumeric() and int(level) > 0:
            ans = random.randint(1,int(level))
            while True:
                guess = input("Guess: ")
                if guess.isnumeric() and int(guess) > 0:
                    if int(guess) == ans:
                        print("Just right!")
                        break
                    elif int(guess) > ans:
                        print("Too Large!")
                        continue
                    elif int(guess) < ans:
                        print("Too small!")
                        continue
                else:
                    continue
            break
        else:
            continue
           
           
    
    ...
    
if __name__ == '__main__':
    main()