'''
Author: George B. Gragas, Jr.
Program Description: A geography quiz game
Date Accomplished: March 31, 2019
Year level: New Freshman
Student nummber: 2018-02463
Lab section: UV-2L
Lab instructor: Ma'am Mayla Anacleto
'''
#importation
import os
import time

#function definition
def osclear():
	import os
	if os.name == 'nt':
		os.system("cls")
	else: os.system("clear")

def menu1():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Mamaw ka ba sa Geography? Unlock your full potential in this Country-Capital quiz game.")
	print("Press the corresponding choices of what you want to do.")
	print("[1] Play")
	print("[2] View High Scores")
	print("[0] Exit")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def menu2():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Press the corresponding choices of what you category to want to play to do")
	print("[1] Easy")
	print("[2] Medium")
	print("[3] Hard")
	print("[0] Back")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def menu3():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Press the corresponding choices of what you category to want to view high scores to do?")
	print("[1] Easy")
	print("[2] Medium")
	print("[3] Hard")
	print("[0] Back")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# displaying questionnaires, player input, scoring 
def quiz(q,a,c):
	count = 0
	for line1,line2,line3 in zip(q,a,c):
		questions = line1[:-1]
		answers = line2[:-1]
		choices = line3[:-1].split(",")
		print(questions)

		for i in choices:
			print(i, end=" ")
		print()
		temp = input("Your choice: ")
		userInput = temp.lower()

		if userInput == answers:
			count += 1
			print("You got it right!")
			print()

		else:
			print("Sorry, you got it wrong!")
			print()

	return count

# main program
# display menus, user input, categories
while True:
	osclear()
	menu1()

	choice1 = int(input("Enter number: "))

	if choice1 == 1:

		while True:
			osclear()
			menu2()

			choice2 = int(input("Enter number: "))

			if choice2 == 1:
				osclear()

				easyQ = open("easyq.txt","r")
				easyA = open("easya.txt","r")
				easyC = open("easyc.txt","r")
				count = quiz(easyQ,easyA,easyC)
				easyC.close()
				easyA.close()
				easyQ.close()

				print("You got",count,"questions right! Congrats!")

				name = input("What is your name? ")

				highScoreA = open("highScoreEasy.txt","a")
				highScoreA.write(name + "," + str(count) + "\n")
				highScoreA.close()

				print("Your score has been saved!")

				time.sleep(3)

			elif choice2 == 2:
				osclear()

				mediumQ = open("mediumq.txt","r")
				mediumA = open("mediuma.txt","r")
				mediumC = open("mediumc.txt","r")
				count = quiz(mediumQ,mediumA,mediumC)
				mediumC.close()
				mediumA.close()
				mediumQ.close()

				print("You got",count,"questions right! Congrats!")

				name = input("What is your name? ")

				highScoreA = open("highScoreMedium.txt","a")
				highScoreA.write(name + "," + str(count) + "\n")
				highScoreA.close()

				print("Your score has been saved!")

				time.sleep(3)

			elif choice2 == 3:
				osclear()

				hardQ = open("hardq.txt","r")
				hardA = open("harda.txt","r")
				hardC = open("hardc.txt","r")
				count = quiz(hardQ,hardA,hardC)
				hardC.close()
				hardA.close()
				hardQ.close()

				print("You got",count,"questions right! Congrats!")

				name = input("What is your name? ")
				highScoreA = open("highScoreHard.txt","a")
				highScoreA.write(name + "," + str(count) + "\n")
				highScoreA.close()

				print("Your score has been saved!")

				time.sleep(3)

			elif choice2 == 0:
				break

			else:
				print("Invalid input.")

				time.sleep(2)

				osclear()

#viewing high scores
	elif choice1 == 2:
		while True:

			osclear()
			menu3()
			
			choice3 = int(input("Enter number: "))
			if choice3 == 1:
				osclear()

				highScoreR = open("highScoreEasy.txt","r")
				temp = {}

				for line in highScoreR:
					score = line[:-1].split(",")
					name = score[0]
					temp[name] = score[1]
				highScoreR.close()

				for k,v in temp.items():
					temp[k] = int(v)
				scores = sorted(temp.values(), reverse=True)

				print("Here are the top scorers of the Easy Category:")
				for i in scores:
					for k,v in temp.items():
						if i == v:
							print(i,k)

				time.sleep(3)

			elif choice3 == 2:
				osclear()

				highScoreR = open("highScoreMedium.txt","r")
				temp = {}

				for line in highScoreR:
					score = line[:-1].split(",")
					name = score[0]
					temp[name] = score[1]
				highScoreR.close()

				for k,v in temp.items():
					temp[k] = int(v)
				scores = sorted(temp.values(), reverse=True)

				print("Here are the top scorers of the Medium Category:")
				for i in scores:
					for k,v in temp.items():
						if i == v:
							print(i,k)
							
				time.sleep(3)

			elif choice3 == 3:
				osclear()
				highScoreR = open("highScoreHard.txt","r")
				temp = {}

				for line in highScoreR:
					score = line[:-1].split(",")
					name = score[0]
					temp[name] = score[1]
				highScoreR.close()

				for k,v in temp.items():
					temp[k] = int(v)
				scores = sorted(temp.values(), reverse=True)

				print("Here are the top scorers of the Hard Category:")
				for i in scores:
					for k,v in temp.items():
						if i == v:
							print(i,k)
							
				time.sleep(3)

			elif choice3 == 0:
				break

			else:
				print("Invalid input.")
				time.sleep(2)
				osclear()

	elif choice1 == 0:
		print("Goodbye! Play again:)")
		time.sleep(2)
		break

	else:
		print("Invalid input.")
		time.sleep(2)
		osclear()