import sys  # sys is a built-in Python module

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
    state = sys.argv[1]
    if state not in states:
        print ("Unknown state")
        return
    
    state_code = states[state]
    capital = capital_cities[state_code]
    print (capital)
if __name__ == '__main__' :
    main()