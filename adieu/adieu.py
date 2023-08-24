def main():
    names = []

    while True:
        try:
            names.append(input("Name: "))

        except EOFError:
            break
        except KeyboardInterrupt:
            break
    print("\nAdieu, adieu, to ", end="")        
    for i in names:
        if i == names[-1] and len(names)>1 :
            print(f"and {i}", end="")
        elif len(names) ==2:
            if i == names[0]:
                print(f"{i} ", end="")
        else:
            if i == names[-1]:
                print(f"{i}", end="")
            else: 
                print(f"{i}, ", end="")  
        
            
    
    
if __name__ == '__main__':
    main()