import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    if matches := re.findall(r' ?(\b[Uu][mM]\b[?,.]?) ?',s,re.IGNORECASE):
        print(matches)
        for i in matches:
            if "um" in i.lower():
                count +=1
        return count
    ...


...


if __name__ == "__main__":
    main()