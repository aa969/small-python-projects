def greet_user():
    """Display's a simple greeting."""
    print("Hello!")


greet_user()


def greet_users(username):
    """Display a simple greeting"""
    print(f"Hello {username.title()} !")


greet_users('david')


def describe_pet(animal_type, pet_name):
    """Displays information about a pet"""
    print(f"\n I have a {animal_type}.")
    print(f"my {animal_type} is called {pet_name.title()}.")


# The function call below is refered to as a keyword argument, it assigns the parameter to the desired argument.
describe_pet(animal_type='hamster', pet_name="Richard")


def describe_pet(pet_name, animal_type='fish'):
    print(f"\n I have a {animal_type}")
    print(f"my {animal_type} is called {pet_name}")


describe_pet(pet_name='Goldeen')


# We defining a function you need to put a positional/keyword argument first followed by a default argument. When
# calling on a argument you can not mix and match the argument, either you use positional argument or keyword arguments

def get_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_name('jimi', 'hendrix')
print(musician)

musician = get_name('james', 'hendrix', 'marshall')
print(musician)


def greet_users(names):
    """greet the user in the list in a friendly manner"""
    for name in names:
        greeting = (f"Hello {name.title()}")
        print(greeting)


usernames = ['david', 'richard', 'steve', 'jay']
greet_users(usernames)


def print_models(unprinted_designs, completed_models):
    """Simulate printing each desgin until none are left.
    moves each printed design to completed design list"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['cars', 'swimming pool', 'phone', 'spaceship']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)






