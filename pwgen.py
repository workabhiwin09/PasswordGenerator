#!/usr/bin/env python3
import cgi
import string
import random
import secrets

def main():

# Path to the Linux dictionary file (change it to the correct path)
    linux_dictionary_path = '/usr/share/dict/words'

# Number of words to choose
    num_words_to_choose = 3

# Get the chosen words

    chosen_words = choose_random_words(linux_dictionary_path, num_words_to_choose)
    result = pwd_gen(chosen_words)    
    return None

def choose_random_words(file_path, num_words):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
        # Filter out words with special characters
        words_without_special_chars = [word for word in words if all(char.isalpha() or char.isspace() for char in word)]
        chosen_words = random.sample(words_without_special_chars, num_words)
    return chosen_words

def pwd_gen(words):
    
    digits = "0123456789"
    special_characters = "!@#$%&^*|"

# Choose single random Digit and Special Char
   
    c_digit = random.choice(digits)
    c_special = random.choice(special_characters)
    c_words = words
    cntr = random.random()

#Generating Password

    if cntr < 0.5:
        password = words[0] + c_digit + words[1] + c_special + words[2]
        length = len(password)
        if length < 25:
        	main()
        else:
        	random_index = random.randint(0, len(password) -1)
        	f_pass = password[:random_index] + password[random_index].upper() + password[random_index + 1:]
        	print("Content-type: text/html\r\n\r\n")
        	print("<html>")
        	print("<body>")
        	print("<h1>Note Your Passphrases</h1>")
        	print(f"<h3>{c_words}</h3>")
        	print("<h1>Note your Password</h1>")
        	print(f"<h3>{f_pass}</h3>")
        	print("</body>")
        	print("</html>")
    else:
    	password1 = words[0] + c_special + words[1] + c_digit + words[2]
    	length = len(password1)
    	if length < 25 :
    		main()
    	else:
    		random_index = random.randint(0, len(password1) -1)
    		f_pass1 = password1[:random_index] + password1[random_index].upper() + password1[random_index + 1:]
    		print("Content-type: text/html\r\n\r\n")
    		print("<html>")
    		print("<body>")
    		print("<h1>Note Your Passphrases</h1>")
    		print(f"<h3>{c_words}</h3>")
    		print("<h1>Note your Password</h1>")
    		print(f"<h3>{f_pass1}</h3>")
    		print("</body>")
    		print("</html>")
    return None

#made with love by iAMShell

if __name__== "__main__":
    main()

