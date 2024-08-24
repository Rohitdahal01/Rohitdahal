import random
three_digit_code = ""
for _ in range(3):
    digit = random.randint(0, 9)
    three_digit_code += str(digit)
four_digit_code = ""
for _ in range(4):
    digit = random.randint(1, 6)  #
    four_digit_code += str(digit)
print("3-digit combination lock code:", three_digit_code)
print("4-digit combination lock code:", four_digit_code)
