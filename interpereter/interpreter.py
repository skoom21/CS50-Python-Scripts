def main():
    exp=input("Expression: ")
    exp= exp.split(" ")
    x = float(exp[-3])
    y = exp[-2]
    z = float(exp[-1])
    
    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "*":
            print(x * z)
        case "/":
            print(x / z)
        case _:
            print("Invalid Operator")


main()