# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
#!/usr/bin/env python3

#...initialize looping variable, assume 'yes' as the first answer
continueYN = "y"
 
#initiate loop that runs until user quits
while continueYN == "y":
	
	#get user input
	message = input('Enter message: ')
	translated = ''

	#counting starts at 0 - we need to get the length of the input, but starting at 0
	i = len(message) - 1
	
	#create a loop to work backwards, will only go as long as we have characters left
	while i >= 0:
		#new variable to hold the reversed message
		translated = translated + message[i]
		i = i - 1
	
	#ooutput the reversed message onto the screen
	print("Encrypted message is: ", translated)

	#check to see if the user wants to go again
	continueYN = input("Input another?")
 
#exit the program