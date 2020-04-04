# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
#!/usr/bin/env python3

#...initialize looping variable, assume "yes" as the first answer
continueYN = "y"

listAlpha = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
listNum = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "99"]
 
#initiate loop that runs until user quits
while continueYN == "y":
	
	#get user input
	message = input("Enter message using only letters, numbers, and spaces: ")
	translated = ""

	#counting starts at 0
	i = 0
	
	#we need a couple temporary holder for converting character to number
	charIndex = ""
	charNumCode = ""
	
	#create a loop, will only go as long as we have characters left
	for x in message:
	
		#get the number associated with the character
		charNum = listAlpha.index(message[i])
		charNumCode = listNum[charNum]
		#add item by item to the coded message
		translated = translated + charNumCode
		
		i = i + 1
	
	#output the reversed message onto the screen
	print("Encrypted message is: ", translated)

	#check to see if the user wants to go again
	continueYN = input("Input another?")
 
#exit the program