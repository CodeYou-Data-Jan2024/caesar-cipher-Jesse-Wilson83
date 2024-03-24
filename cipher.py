abc = "abcdefghijklmnopqrstuvwxyz"
message = input("Enter a message to encrypt:")
message = message.lower()
#Get shift key
while True:
    key = input("Enter a shift number:")
    if key.isdecimal():
        key = int(key)
        if key in range(26):
            break
        print("You need to enter a number between 0 and 25.")
#Find the letters
encrypted_char = ""
for char in message:
    if char in abc:
        index = abc.find(char)
        index = (index + key) % 26
        char = abc[index]
    encrypted_char += char

print("The encrypted message is:", encrypted_char)