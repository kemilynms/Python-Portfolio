import random
import string

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a 16-character random password
random_password = generate_password(16)
print(f"Random password: {random_password}")
