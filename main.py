from urllib.request import urlopen, hashlib
sha1hash = input("Please input the hash to crack.\n>")
LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/pratik0oo7/password_cracker/main/10-million-password-list-top-10000.txt').read(), 'utf-8')
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
    if hashedGuess == sha1hash:
        print("The password is ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Password guess ",str(guess)," does not match, trying next...")
print("Password not in database, we'll get them next time.")
    
