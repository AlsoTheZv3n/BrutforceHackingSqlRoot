import subprocess
import os

# Define the MySQL bin directory path (raw)
mysql_bin_dir = r"C:\Program Files\MySQL\MySQL Server 8.0\bin"

# Array of passwords to try
passwords = [
    "password1",
    "password2",
    "password3",
    "123",
    "1234",
    "12345",
    "123456",
    "1234567",
    "12345678",
    "123456789",
    "12345678910",
    "hallo",
    "hallo26",
    "password",
    "randompassword",
    "securepassword",
    "mysql123",
    "admin123",
    "qwerty",
    "letmein",
    "password123",
    "1234567890",
    "password!",
    "welcome",
    "monkey",
    "abc123",
    "123qwe",
    "passw0rd",
    "master",
    "football",
    "dragon",
    "123123",
]

# Boolean flag to track success
login_successful = False

# Loop through each password
for password in passwords:
    # Construct the command to execute
    executable = os.path.join(mysql_bin_dir, "mysql.exe")
    arguments = f"-u root -p{password}"

    # Execute the command
    process = subprocess.Popen([executable] + arguments.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, _ = process.communicate()

    # Check if MySQL login was successful
    if process.returncode == 0:
        print("Login successful!")
        login_successful = True
        break  # Exit the loop if login is successful
    else:
        print("Login unsuccessful. Trying next password...")

# If none of the passwords worked
if not login_successful:
    print("Unable to login to MySQL with any of the provided passwords.")
