# Unpacking
inputs = [
    'John',
    'Smith',
    'Canada',
    'Blue',
    'Brown',
    29
]

firstName, lastName, *_, age = inputs

print(f'{firstName} {lastName} is {age} years old')