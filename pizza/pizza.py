import sys 
import csv
import errno
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    elif len(sys.argv) < 2:
         sys.exit("Too few command-line arguements")
    else:
        sys.exit("Too many command-line arguements")
    try:
        table = []
        if ".csv" in filepath:
            with open(filepath) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    table.append(row)
            print(tabulate(table, headers='firstrow', tablefmt='grid'))  
        else:
            sys.exit("Not a CSV file")
            
            
    except OSError as e:
        if e.errno == errno.ENOENT:
            sys.exit("File does not exist")
    

    
    
    
    
    
if __name__ == "__main__":
    main()
