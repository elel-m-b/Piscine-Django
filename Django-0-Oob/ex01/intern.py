class Intern:

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return Intern.Coffee()


# ===== TESTS =====

if __name__ == "__main__":

    # First intern (no name)
    intern1 = Intern()

    # Second intern (Mark)
    intern2 = Intern("Mark")

    # Display names
    print(intern1)
    print(intern2)

    # Ask Mark to make coffee
    coffee = intern2.make_coffee()
    print(coffee)

    # Ask first intern to work (handle exception)
    try:
        intern1.work()
    except Exception as e:
        print(e)
