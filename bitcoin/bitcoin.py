import requests
import json
import sys

def main():
    try:    
        mult = float(sys.argv[1])
        
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        rate = float((response["bpi"]["USD"]["rate_float"]))
        print(f"${rate*mult:,.4f}")

        ...
    except ValueError:
        sys.exit("Commnad-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")
    except requests.RequestException:
        ...
        
        
        
if __name__ == "__main__":
    main()