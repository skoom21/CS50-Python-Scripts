def main():
    amount =50

    while True:
        print(f"Amount Due: {amount}")
        coin= int(input("Insert Coin: "))
        if(coin == 25 or coin == 10 or coin ==5):
            amount = amount - coin
            print("hello")
            if(amount>0):
                continue
            else:
                print(f"Change Owed: {amount*-1}")
                break

        
    ...



if (__name__ == "__main__"):
    main()