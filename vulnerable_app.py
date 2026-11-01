import hashlib
import subprocess

# Vulnerability 1: Hardcoded Password
password = "admin123"


# Vulnerability 2: Weak Cryptographic Hash
def generate_hash(text):
    return hashlib.md5(text.encode()).hexdigest()


# Vulnerability 3: Command Injection
def execute_command(username):
    subprocess.run(
        f"echo Hello {username}",
        shell=True,
        check=True
    )


# Main Application
if __name__ == "__main__":

    print("SAST Security Testing Practical")

    print("Testing MD5 Hashing:")
    print(generate_hash("Hello World"))

    username = input("Enter username: ")

    execute_command(username)
