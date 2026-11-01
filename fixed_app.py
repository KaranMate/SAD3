import hashlib
import os


# Fix 1: Read Password from Environment Variable
password = os.getenv("APP_PASSWORD")


# Fix 2: Use SHA-256 for General-Purpose Hashing
def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


# Fix 3: Avoid Unsafe Shell Execution
def execute_command(username):
    print(f"Hello {username}")


# Main Application
if __name__ == "__main__":

    print("SAST Security Testing - Secure Application")

    print("Testing SHA-256 Hashing:")
    print(generate_hash("Hello World"))

    username = input("Enter username: ")

    execute_command(username)

    print("Security Testing Completed")
