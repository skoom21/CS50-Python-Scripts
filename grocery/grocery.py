def main():
    grocery_list = {}

    try:
        while True:
            item = input().strip()
            if not item:
                continue  
            item = item.lower()  
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
    except EOFError:
        pass  
    except KeyboardInterrupt:
        pass
    print("\n")
    for item, count in sorted(grocery_list.items()):
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
