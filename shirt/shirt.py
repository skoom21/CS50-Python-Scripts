import sys 
import csv
import errno
from os.path import splitext 
from PIL import Image, ImageOps

def main():
    if len(sys.argv) == 3:
        filepath = sys.argv[1]
        filepath2 = sys.argv[2]
        ext1 = splitext(filepath)[1]
        ext2 = splitext(filepath2)[1]
        shirt = Image.open("shirt.png")
    elif len(sys.argv) < 3:
         sys.exit("Too few command-line arguements")
    else:
        sys.exit("Too many command-line arguements")
    try:
        formats = [".jpg", ".png", ".jpeg"]
        if  ext1.casefold() and ext2.casefold() in formats :
            if ext1 == ext2:
                with Image.open(filepath) as img:
                    # resize and crop image
                    img = ImageOps.fit(img,size=(600,600), bleed=0.0, centering=(0.5, 0.5))
                    img.paste(shirt,mask=shirt)
                    img.save(filepath2)
                                    
            else:
                sys.exit("Input and Output have different extensions")
        else:
            sys.exit("Invalid Extension")
            
            
    except OSError as e:
        if e.errno == errno.ENOENT:
            print(e.errno)
            sys.exit("Could not read ")
    

    
    
    
    
    
if __name__ == "__main__":
    main()
