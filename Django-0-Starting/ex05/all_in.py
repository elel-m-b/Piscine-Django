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

    # Must have exactly one argument
    if len(sys.argv) != 2:
        return

    input_string = sys.argv[1]

    # Split by comma
    expressions = input_string.split(',')

    for expr in expressions:
        expr_clean = expr.strip()  # remove spaces around
        if expr_clean == '':
            # skip empty expression
            continue

        expr_lower = expr_clean.lower()

        found = False

        # Check if it's a state
        for state_name, code in states.items():
            if expr_lower == state_name.lower().replace(' ', '') or expr_lower == state_name.lower():
                capital = capital_cities[code]
                print(f"{capital} is the capital of {state_name}")
                found = True
                break

        if found:
            continue

        # Check if it's a capital
        for code, capital_name in capital_cities.items():
            if expr_lower == capital_name.lower().replace(' ', '') or expr_lower == capital_name.lower():
                # Find the state for this capital
                for state_name, state_code in states.items():
                    if state_code == code:
                        print(f"{capital_name} is the capital of {state_name}")
                        found = True
                        break
            if found:
                break

        # If neither state nor capital
        if not found:
            print(f"{expr_clean} is neither a capital city nor a state")

if __name__ == "__main__":
    main()
