'''write a python program to create a custom exception that shows invalid age error i.e., write a fuction that raises this exception
if age provided is less than 18 and greater than 100'''
class InvalidAgeError(Exception):
    pass
def validate_age(age):
    if age < 18 or age > 100:
        raise InvalidAgeError("Invalid age: must be between 18 and 100")
    return age
try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Valid age:",age)
except InvalidAgeError as e:
    print("Error:", e)
