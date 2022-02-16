with open('/Users/aa742/Desktop/pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Please enter your birthday in the format mmddyy")

if birthday in pi_string:
    print('Your birthday show up in the first 10,000 digits of Pi')
else:
    print('your birthday does not show in the first 10,000 digits of Pi')


# An absolute file pathway is provided above to retrieve the file.
# .readline function store the information in pi_digits.txt as a list
