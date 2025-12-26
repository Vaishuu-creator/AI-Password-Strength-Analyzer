import random
import string

def generate_password(strength):
    if strength == 0:  # Weak
        return random.choice([
            "password", "123456", "admin", "welcome", "qwerty"
        ]) + str(random.randint(0,99))
    
    elif strength == 1:  # Medium
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(8)) + "@"
    
    else:  # Strong
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(14))

with open("dataset.csv", "w") as f:
    f.write("password,label\n")
    for label in [0,1,2]:
        for _ in range(200):
            f.write(f"{generate_password(label)},{label}\n")

print("Large dataset generated!")
