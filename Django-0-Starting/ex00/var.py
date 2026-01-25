def my_var():
    a = 42              # int
    b = "42"            # str
    c = "quarante-deux" # str
    d = 42.0            # float
    e = True            # bool
    f = [42]            # list
    g = {42: 42}        # dict
    h = (42,)           # tuple
    i = set()           # set

    # Print each variable and its type
    print(f"{a} has a type {type(a)}")
    print(f"{b} has a type {type(b)}")
    print(f"{c} has a type {type(c)}")
    print(f"{d} has a type {type(d)}")
    print(f"{e} has a type {type(e)}")
    print(f"{f} has a type {type(f)}")
    print(f"{g} has a type {type(g)}")
    print(f"{h} has a type {type(h)}")
    print(f"{i} has a type {type(i)}")

# Call the function as required
if __name__ == '__main__':
    my_var()
