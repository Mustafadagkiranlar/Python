print("Made by Mustafa Dagkiranlar visit: mustafadagkiranlar.ga")
loose = ("The Computer wins")
win = ("You win!")
lives = 5
score = 0
draw = 0
computer_lives = 7

while True:
    print("To begin fill below information")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    searchfile = open("accounts.csv", "r")
    for line in searchfile:
        if username and password in searchfile:
            print("Acces Granted! ")
            print("Live rules")
            print("You start with ", lives, " lives.")
            print("If you loose you lose a live")
            print("If you win you win a live")
            print("-----------------------------------")
            print("Dont use capitals")
            print("-----------------------------------")
            print("To see list of rules type rules")
            print("-----------------------------------")
            print("At any point type exit to exit the game")
            print("-----------------------------------")
            print("The computer has lives aswell")
            print("Can you beat the computer")
            print("Good luck")
            while True:
            	rps = input("Rock, Paper, Scissors: ")
            	import random
            	computer = ("rock","paper","scissors")
            	computer = random.choice(computer)
            	#rock if statement
            	if rps == "rock" and computer == "paper":
            		print("the computer choose", computer)
            		print("")
            		print(loose)
            		print("")
            		lives = lives - 1
            		print("You got", lives, " lives")

            	if rps == "rock" and computer == "scissors":
            		print("the computer choose", computer)
            		print("")
            		print(win)
            		print("")
            		lives = lives + 1
            		print("")
            		print("You got ", lives, " lives")
            		score = score + 1

            	#paper if statement
            	if rps == "paper" and computer == "scissors":
            		print("the computer choose", computer)
            		print("")
            		print(loose)
            		print("")
            		lives = lives - 1
            		print("You got", lives, "lives")

            	if rps == "paper" and computer == "rock":
            		print("the computer choose", computer)
            		print("")
            		print(win)
            		print("")
            		lives = lives + 1
            		print("")
            		print("You got ", lives, " lives")
            		score = score + 1

            	#scissors if statement
            	if rps == "scissors" and computer == "rock":
            		print("the computer choose", computer)
            		print("")
            		print(loose)
            		print("")
            		lives = lives - 1
            		print("You got", lives, "rock")

            	if rps == "scissors" and computer == "paper":
            		print("the computer choose", computer)
            		print("")
            		print(win)
            		print("")
            		lives = lives + 1
            		print("")
            		print("You got ", lives, " lives")
            		score = score + 1

            	#duplicates
            	if rps == "rock" and computer == "rock":
            		print("the computer chooes", computer)
            		print("")
            		print("You Drew")
            		print("")
            		draw = draw + 1
            	if rps == "paper" and computer == "paper":
            		print("the computer chooes", computer)
            		print("")
            		print("You Drew")
            		print("")
            		draw = draw + 1
            	if rps == "scissors" and computer == "scissors":
            		print("the computer chooes", computer)
            		print("")
            		print("You Drew")
            		print("")
            		draw = draw + 1

            	#system
            	if rps == "rules":
            		print("Live rules")
		            print("You start with ", lives, " lives.")
		            print("If you loose you lose a live")
		            print("If you win you win a live")
		            print("-----------------------------------")
		            print("Dont use capitals")
		            print("-----------------------------------")
		            print("To see list of rules type rules")
		            print("-----------------------------------")
		            print("At any point type exit to exit the game")
		            print("-----------------------------------")
		            print("The computer has lives aswell")
		            print("Can you beat the computer")
		            print("Good luck")

		        if rps == "display lives":
		        	print(lives)

		       	if rps == "display score":
		       		print(score)

		       	if rps == "display draw":
		       		print(draw)
