current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

message = input("Tell me somthing, and I will repeat it back to you:")
print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program"

active = True
while active:
    message = input(prompt)
    if message =='quit':
        active = False
    else:
        print(message)

prompt = '\nPlease enter the name of a city you have visited'
prompt += "\nEnter 'quit' when you are finished"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would love to vist {city.title()}")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
print(bool(unconfirmed_users))

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'dragon', 'kangaroo', 'rabbit', 'cat', 'dog', 'cat', 'goldfish']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
print(len(pets))

