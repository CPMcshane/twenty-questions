"""
20 questions game. The user chooses a Super Smash Bros. Ultimate Character and
the computer program has 20 questions to guess what it is.
"""
import pandas as pd
import numpy as np
import math

class Interrogator:

	def __init__(self):

		# List to hold the questions to be asked
		# The idex lines up with the index of the array
		self.question_list = ["Does your character use a sword? ",
				      "Does your character use a gun? ",
				      "Is your character in a mario game? ",
				      "Is you character in a zelda game? ",
				      "Is your character in a fire emblem game? ",
				      "Is your character evil? ",
				      "Does your character have human features? ",
				      "Does your character have animal resemblance? ",
				      "Does your character have a projectile attack? ",
				      "Does your character have a counter? ",
				      "Does your character wear a hat? ",
				      "Is your character an echo character? ",
				      "Is your character male with any skins? ",
				      "Is your character in pokemon games? ",
					  "Does your character wear a crown? ",
					  "Does your character wear a helmet? ",
					  "Is your character from street fighter? ",
					  "Does your character have a golden sword? ",
					  "Does your character wear any sort of band around their head? ",
					  "Does your character have feathers? ",
					  "Does your character have fire in any attacks? ",
					  "Does your character have any move to reflect projectiles? ",
					  "Does your character have brown on their tail? "]
		
		# A 1D array to hold the yes/no info gathered from the questions
		self.character_info = [None, None, None, None, None, None, None, None, None,
							None, None, None, None, None, None, None, None, None, None,
							None, None, None, None]


	def ask_question(self, index):
		""" Asks the yes/no questions """
		
		# Loop to keep the player typing unless a yes
		# or no answer is given
		answer = ''
		while True:
			
			# User input, should be a yes or a no
			# The quesion asked is based on the index passed in
			answer = input(self.question_list[index])

			# Set the value in the character info list
			# to yes or no at the correct index
			if answer == "yes":
				self.set_info("yes", index)
				self.update_guess_array(answer, index + 1)
				break
			elif answer == "no":
				self.set_info("no", index)
				self.update_guess_array(answer, index + 1)
				break
			else:
				print("\nmust type either yes or no\n")


	def make_guess(self, character):
		""" Guess a specific character """

		while answer != 'yes' or 'no':

			# Ask the user
			answer = input(f"Is your character {character}? ")

			# Returns True if yes, False if no
			if answer == 'yes':
				return True
			elif answer == 'no':
				return False
			else:
				# Print error message if not yes or no
				print("\nAnswer must be either yes or no\n")
				

	def get_character_info(self):
		""" returns the character info list """
		return self.character_info


	def get_characters_left(self):
		""" returns a list of characters left """
		characters_left = []
		for i in range(0,75):

			character = guess_array[i,0]

			if character != None:

				characters_left.append(character)

		return characters_left


	def set_info(self, answer, index):
		""" adds a yes or no to the character list """
		self.character_info[index] = answer


	def find_question(self):

		# Empty list to eventually hold the percent of yes per question
		# Each question has it's own index spot
		checker = [None, None, None, None, None, None, None, None, None, None,
				   None, None, None, None, None, None, None, None, None, None,
				   None, None, None]

		# Iterrate through each question
		for i in range(1,24):

			# Change the index value from nonetype to integer
			checker[i-1] = 0
			# Create a 1D array of the specific question column
			specific_column = guess_array[:,i]

			# Iterrate through each value in the column
			for j in range(0,75):

				# Find the specific yes/no value in the row
				specific_value = specific_column[j]

				# If the value is yes, add one to the checker at 
				# the question's index on the checker list
				if specific_value == "yes":
					checker[i-1] = checker[i-1] + 1

			# After the iterration, find how close the value
			# is to 50%. 0 means 50% exactly
			checker[i-1] = abs(((checker[i-1] / len(self.get_characters_left())) - 0.5))

		# Create variables to find the lowest value
		lowest = 10
		index = -1
		
		# Iterrate through the checker list
		for item in checker:

			# Keep track of the index for the current
			# item being checked
			index += 1
			# If the item is lower than previous items,
			# it is now the lowest
			if item < lowest:
				lowest = item
				lowest_index = index

		# Ask what has been determined to be the
		# most effective question
		interrogator.ask_question(lowest_index)


	def update_guess_array(self, answer, index):
		""" 
		Update guess array to remove characters
		who no longer meet the criteria
		"""
		# Iterrate through the characters
		for i in range(0,75):

			# Find the character's value for
			# the question asked
			value = guess_array[i,index]

			# If the value is different from
			# the answer given, set all values
			# of that character to 0
			if answer != value:
				for j in range(0,24):
					guess_array[i,j] = None

		guess_array[:, index] = None

		

interrogator = Interrogator()



def main():

	interrogator = Interrogator()
	guess = 0
	while True:

		# Keep track of guesses
		guess += 1
		print(f"\nguess number {guess}")

		# Find the best question
		interrogator.find_question()

		# If there is only one possible character left, guess it
		characters_left = interrogator.get_characters_left()
		if len(characters_left) == 1:
			guess += 1
			print(f"\nguess number{guess}")
			answer = input(f"Is your character {characters_left[0]}? ")
			if answer == 'yes':
				
				print("I won!")
				break

		if guess == 20:

				print("I lost!")
				break



if __name__ == "__main__":

	df = pd.read_csv("smash bros info.csv", delimiter=',')

	info_array = df.values
	guess_array = df.values

	main()
