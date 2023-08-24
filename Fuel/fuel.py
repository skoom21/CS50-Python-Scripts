def main():
            while True:
                try:
                    frac= input("Fraction: ")
                    frac = convert(frac)
                    print(gauge(frac))
                    break
                except ZeroDivisionError:
                    print("")
                    continue
                except ValueError:
                    print("")
                    continue

def convert(fraction):
    frac= fraction.split("/")
    x= int(frac[0])
    y= int(frac[1])
    if(x > y):
        raise ValueError
    elif(y==0):
        raise ZeroDivisionError
    return int(round((x / y) *100))


def gauge(percentage):
    if(percentage >= 99):
            return ("F")
    elif(percentage <= 1):
            return ("E")
    return f"{percentage}%"
    


if __name__ == "__main__":
    main()