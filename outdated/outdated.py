month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        try:
            date = input("Date: ")
            date = check_date(date)
            print(date)
            break
        except:
            pass


def check_date(d):
    if " " and "," in d:
        
        d = d.replace(",", "")
        date = d.split(" ")
        if date[0] in month:
            
            if date[1].isnumeric() and int(date[1]) <= 31:
                
                if date[2].isnumeric():
                    
                    date = f"{int(date[2])}-{month.index(date[0])+1:02}-{int(date[1]):02}"
                    return date
                else:
                    raise
            else:
                raise
        else:
            raise 

    elif "/" in d:
        date = d.strip().split("/")
        if date[0].isnumeric() and int(date[0]) <= 12:
            
            if date[1].isnumeric() and int(date[1]) <= 31:
                
                if date[2].isnumeric():
                    
                    date = f"{int(date[2])}-{int(date[0]):02}-{int(date[1]):02}"
                    return date
                else:
                    raise
            else:
                raise
        else:
            raise
    else:
        raise


if __name__ == "__main__":
    main()
