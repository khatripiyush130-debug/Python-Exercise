import random
import string
def generate_otp():
    characters = string.ascii_uppercase + string.digits
    otp = ""
    for i in range(6):
        otp += random.choice(characters)
    print("Generated OTP:", otp)
generate_otp()