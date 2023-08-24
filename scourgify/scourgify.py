import sys 
import csv
import errno

def main():
    if len(sys.argv) == 3:
        filepath = sys.argv[1]
        filepath2 = sys.argv[2]
    elif len(sys.argv) < 3:
         sys.exit("Too few command-line arguements")
    else:
        sys.exit("Too many command-line arguements")
    try:
        data = []
        if ".csv" in filepath:
            with open(filepath) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    house = row["house"]
                    last,first= row["name"].split(", ")
                    data.append({"first":first, "last":last, "house":house})
                    
            with open(filepath2,'w') as csvfile:
                fieldnames = ["first","last","house"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)                    

        else:
            sys.exit("Not a CSV file")
            
            
    except OSError as e:
        if e.errno == errno.ENOENT:
            print(e.errno)
            sys.exit("Could not read ")
    

    
    
    
    
    
if __name__ == "__main__":
    main()
