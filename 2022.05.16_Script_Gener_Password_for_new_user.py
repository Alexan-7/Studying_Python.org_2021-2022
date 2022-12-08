import random

while True:
    x = input("Enter the username, get the generated password and remember it: ")
    pas = ""

    for y in range(16):
        pas += random.choice("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789!@#$%^&*<>")

    print(x, ", your password: ", pas)
