from testing_functions import get_formatted_name

print("Enter 'q' if you want to quit")

while True:
    first_name = input("\n Please give me first name:")
    if first_name == 'q':
        break
    last_name = input("\n Please give me your second name:")
    if last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print(f"\t Neatly formatted name: {formatted_name}")
