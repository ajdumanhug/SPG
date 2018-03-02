import sys

if sys.version_info < (3, 0):
	input = raw_input

print ("""
   _____ _____   _____ 
  / ____|  __ \ / ____|
 | (___ | |__) | |  __ 
  \___ \|  ___/| | |_ |
  ____) | |    | |__| |
 |_____/|_|     \_____|
                       
                       
Simple Password Generator

- At least 8 characters in length
- Contain at least 1 lowercase and 1 uppercase letter
- Contain at least 1 special character 
- Contain at least 1 number
""")

chosenWord = input("Enter a random word: ")
if not chosenWord.isalpha():
    print("Only letters are allowed. Try again!")
    exit()
elif len(chosenWord) < 7:
	print ("Your word must contain at least 8 characters. Try again!")
	exit()
obfuscateWord =  input("Obfuscate the word? [Y/N]: ").upper()
chosenWebsite = input("Enter the name of the website where the password will be used: ")
obfuscateWebsite = input("Obfuscate the website? [Y/N]: ").upper()

if obfuscateWord == 'Y':
	isWordObfuscated = True
else:
	isWordObfuscated = False

if obfuscateWebsite == 'Y':
	isWebsiteObfuscated = True
else:
	isWebsiteObfuscated = False

def obfuscatingWord(chosenWord):
	if isWordObfuscated:
		chosenWord = chosenWord.replace('A', '4').replace('a','@').replace('B','8').replace('C','(').replace('e','3').replace('i','!').replace('I','|').replace('l','1').replace('o','0').replace('s','$').replace('S','5').replace('t','+').replace('T','7')
		return chosenWord
	else:
		return chosenWord

def obfuscatingWebsite(chosenWebsite):
	if isWebsiteObfuscated:
		chosenWebsite = chosenWebsite.replace('A', '4').replace('a','@').replace('B','8').replace('C','(').replace('e','3').replace('i','!').replace('I','|').replace('l','1').replace('o','0').replace('s','$').replace('S','5').replace('t','+').replace('T','7')
		return chosenWebsite
	else:
		return chosenWord

def generate():
	print ("Here is the generated password: " + obfuscatingWord(chosenWord) + obfuscatingWebsite(chosenWebsite))

generate()