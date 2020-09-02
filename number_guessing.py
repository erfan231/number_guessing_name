import random
"""
show points

import rand number

ask

right -- give point

ask want to guess another game

ask = yes -
ask = no - finish 

wrong -- give another hint - take point

"""


class Game:
	
	def make_num(n):
		n = random.randint(1,200)
		print("Hint 1 is Number - 1 =", n - 1)
		return n

	def ask(n):
		ask = int(input("What is the number? " ))
		return ask

	def clues(self):
		clue = input("Would you like another CLue? ")
		return clue

	def more_clues(c):
		clue_1 = "clue 1"
		clue_2 = "clue 2"
		return clue_1 or clue_2


point = 0
def main():
	global point

	while True:
		game = Game()
		print(point)
		num = game.make_num()
		ask = game.ask()
		if ask == num:
			point = point + 1
			print("Your guess is correct! ")
			
		else:
			print("Your Guess is incorrect")
			hint = game.clues()
			if hint == 'Yes' or "yes":
				if point < 1:
					print("Sorry you can't buy a hint")
				else:
					point -= 1
					game.more_clues()
		

main()





