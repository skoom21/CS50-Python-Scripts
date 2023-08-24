import sys
import errno

def main ():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    elif len(sys.argv) < 2:
         sys.exit("Too few command-line arguements")
    else:
        sys.exit("Too many command-line arguements")
    try:
        if ".py" in filepath:
            file = open(filepath, 'r')
            count = 0
            for line in file:
                # print(line)
                if line.lstrip().startswith("#") or line.isspace():
                    continue
                else:
                    count += 1
            print(count)
        else:
            sys.exit("Not a Python file")
            
            
    except OSError as e:
        if e.errno == errno.ENOENT:
            sys.exit("File does not exist")

    
    
if __name__ == "__main__":
    main()