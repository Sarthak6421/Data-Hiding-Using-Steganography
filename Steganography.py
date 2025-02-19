import cv2
import os
import string

# Load the image where the message will be hidden
img = cv2.imread("Chameleon.jpg")  # Replace with the correct image path

# Get the secret message and passcode from the user
msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Create dictionaries to map characters to ASCII values and vice versa
d = {}
c = {}

for i in range(255):  # Loop through ASCII values
    d[chr(i)] = i  # Store character-to-ASCII mapping
    c[i] = chr(i)  # Store ASCII-to-character mapping

# Initialize pixel position variables
m = 0
n = 0
z = 0

# Encode the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]  # Store ASCII value of each character in image pixels
    n = n + 1  # Move to the next pixel row
    m = m + 1  # Move to the next pixel column
    z = (z + 1) % 3  # Cycle through RGB channels

# Save the modified image with the hidden message
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the encrypted image on Windows

# Initialize decryption variables
message = ""
n = 0
m = 0
z = 0

# Get the passcode for decryption
pas = input("Enter passcode for Decryption")

# Check if the entered passcode matches the original
if password == pas:
    for i in range(len(msg)):  # Retrieve message from image pixels
        message = message + c[img[n, m, z]]  # Convert stored values back to characters
        n = n + 1
        m = m + 1
        z = (z + 1) % 3  # Cycle through RGB channels
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")  # Deny access if the passcode is incorrect
