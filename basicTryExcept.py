try:
    text = int("hello")
except (ValueError,TypeError):
    print("Error:That was not a valid integer.Please enter a number")
