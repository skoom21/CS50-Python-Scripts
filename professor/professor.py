import random


def main():
    count = 1
    errors = 0
    while True:
        try:
            if count > 10:
                print(f"Score: {count-errors}")
                break
            if(count == 1):
                level = get_level()
            
            a = generate_integer(level)
            b = generate_integer(level)
            z = a+b
            ans = int(input(f"{a} + {b} = "))
            if ans == z:
                count+=1
                continue
            elif ans != z:
                print("EEE")
                for i in range(2):
                    ans = input(f"{a} + {b} = ")
                    if ans == z:
                        count+=1
                        break
                    elif ans != z:
                        errors+=1
                        print("EEE")
                        continue
                print(f"{a} + {b} = {z}")
                count+=1
                continue

        except ValueError:
            pass
    ...


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in range(1,4):
                return n
            else:
                raise ValueError
        except ValueError:
            pass
    ...

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError
        
    ...


if __name__ == "__main__":
    main()