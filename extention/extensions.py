def main():
    filename= input("File name: ").casefold()

    #remove string before .
    filename = filename.split(".")
    extention = filename[-1].replace(" ","")

    match extention:
        case "jpg" | "png" | "gif" | "jpeg":
            if(extention == "jpg"):
                print("image/jpeg")
            else:
                print("image/"+extention)
        case "pdf" | "txt" | "zip":
            if(extention == "txt"):
                print("text/plain")
            else:
                print("application/"+extention)
        case _:
            print("application/octet-stream")

main()