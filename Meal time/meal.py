def main():
    time = input("What time is it? ")
    time = convert(time)
    if(time >= 7 and time <= 8):
        print("breakfast time")
    elif(time >= 12 and time <= 13):
        print("lunch time")
    elif(time >= 18 and time <= 19):
        print("dinner time")
    
    ...


def convert(time):
    time = time.split(":")
    hour = float(time[0])
    minute = float(time[1])/60
    hour = hour + minute
    return hour

    ...


if __name__ == "__main__":
    main()