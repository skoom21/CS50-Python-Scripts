import re
import sys


def main():
    try:
        result = convert(input("Hours: "))
        print(result)
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    pattern = r'(\d{1,2}(?::\d{2})? ?[APap][Mm] ?to ?\d{1,2}(?::\d{2})? ?[APap][Mm])'
    if not re.match(pattern, s):
        raise ValueError()
    start_time, end_time = s.split(' to ')
    if(" " in start_time and " " in end_time):
        start_time_24h = convert_to_24h(start_time)
        end_time_24h = convert_to_24h(end_time)
    else:
        raise ValueError
    
    return f"{start_time_24h} to {end_time_24h}"


def convert_to_24h(time_str):
    time_pattern = r'(\d{1,2})(?::(\d{2}))? ?([APap][Mm])'
    
    match = re.match(time_pattern, time_str)
        
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2) or 0)
        period = match.group(3).lower()

        if hours > 12 or hours < 1:
            raise ValueError()
        if minutes > 59:
            raise ValueError()
        if period == 'am' and hours == 12:
            hours = 0
        elif period == 'pm' and hours != 12:
            hours += 12
        return f"{hours:02}:{minutes:02}"
    else:
        raise ValueError()


if __name__ == "__main__":
    main()
