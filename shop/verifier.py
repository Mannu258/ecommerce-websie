import random
def otpgenerator():
    global otp
    otp = int(random.randint(0000,9999))
    return otp

def otpverifier(OTP):
    global verfier
    verfier = False
    if otp == OTP:
        verfier = True