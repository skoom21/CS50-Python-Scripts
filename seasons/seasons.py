import inflect
from datetime import datetime, date
import re
import sys

p = inflect.engine()

def validDate(d):
    pattern = r'\d{4}-\d{2}-\d{2}'
    if(re.match(pattern,d)):
        parsed_date = datetime.strptime(d, "%Y-%m-%d").date()
        if parsed_date <= date.today():

            d = d.split("-")
            d = date(int(d[0]),int(d[1]),int (d[2]))
            d = date.today() - d    
            song = d.days *24 *60
                            
            return f"{p.number_to_words(song,andword='').capitalize()} minutes"

    sys.exit("Invalid Date")


def main():
    print( validDate(input("Date of birth: ")))
    

    ...


...


if __name__ == "__main__":
    main()