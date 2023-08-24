import re

pattern = r'(\d{1,2}(?::\d{2})? ?[APap][Mm] ?to ?\d{1,2}(?::\d{2})? ?[APap][Mm])'
text = "9:00 AM to 5:00 PM"

match = re.search(pattern, text)

if match:
    print("Match found:", match.group(0))
else:
    print("No match found.")
