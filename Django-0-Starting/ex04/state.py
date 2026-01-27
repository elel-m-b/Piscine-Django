import sys


def main():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if (len(sys.argv) != 2):
        return 
    
    capital = sys.argv[1]

    state_code = None

    for key, value in capital_cities.items():
        if (value == capital):
            state_code = key
            break
    if state_code is None:
        print("Unknown capital city")
        return
    state_name = None
    for name, value in states.items():
        if value == state_code:
            state_name = name
            break
    print(state_name)

if __name__ == '__main__' :
    main()