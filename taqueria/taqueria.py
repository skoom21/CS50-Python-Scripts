def main ():

    data_dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    Total=0

    while True:
        try:
            item = input("Item: ").title()
            if(item not in data_dict.keys()):
                raise ValueError
            else:
                Total += data_dict[item]
                print(f"Total: $%.2f" %Total,sep="")
                continue
        
        except EOFError as e:
            break
        except KeyboardInterrupt:
            break
        except ValueError:
            continue

    ...


if __name__ == "__main__":
    main()