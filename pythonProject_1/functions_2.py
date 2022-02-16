def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# The asterisk tells the function to make a tuple and add all the string to the tuple
# tuple = ('',) list = ['',] set = {'',} dictionary = {'':''}

def makeing_pizzas(*toppings):
    """Summarises the Pizza that has been ordered"""
    print("\nMaking pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")


makeing_pizzas('tuna', 'green peppers', 'extra cheese', 'mushrooms')
makeing_pizzas('black olives', 'chicken', 'beef', 'pineapple')


def make_pizza(size, *topping):
    """Summarises the pizza toppings and size"""
    print("The following pizza has been ordered by you")
    print(f"\nSize: {size}")
    print("Toppings")
    for topping in topping:
        print(f"- {topping}")


make_pizza('16 inch', 'mushrooms', 'cheese', 'tuna', 'pineapple')
make_pizza('20 inch', 'onions', 'tomatoes', 'beef', 'chicken')


# How to add stuff to the end of a dictionary  dictionary_name[key]=value

def build_profile(
        first, last,
        **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Einstein', 'Albert', location='princeton', occupation = 'physics')
print(user_profile)
