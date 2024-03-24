abc = "abcdefghijklmnopqrstuvwxyz"
message = input("Enter a sentence:")
message = message.lower()
key = 5
#Get shift key from user comented out
#while True:
    #key = input("Enter a shift number:")
    #if key.isdecimal():
       #key = int(key)
        #if key in range(26):
            #break
        #print("You need to enter a number between 0 and 25.")
#Find the letters
encrypted_char = ""
for char in message:
    if char in abc:
        index = abc.find(char)
        index = (index + key) % 26
        char = abc[index]
    encrypted_char += char

print("The encrypted sentence is:", encrypted_char)