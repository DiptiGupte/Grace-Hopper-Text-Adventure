start = "Hello! Welcome to the Grace Hopper adventure!"
print(start)
done = False
while not done:
	print("There is a huge bug just stole your laptop! Quick! Catch it!")
	user_input = input()
	correct_input = False
	while not correct_input:
		if user_input == "catch bug":
			print("Did you know that the terms 'bug' and 'debug' are said to have come from Grace Hopper after she found a moth inside her machine!")
			correct_input = True
		else:
			print("I don't understand that. Try again.")
			print("Hint: enter 'catch bug'")
			user_input = input()
	print("As you are running after your bug, you reach a crossroad.")
	print("To your left is Song Street and to your right is Compiler road. Which way do you go?")
	correct_input = False
	while not correct_input:
		user_input = input()
		if user_input == "left":
			print("Another fun fact! Grace Hopper was nicknamed 'Amazing Grace' because of her contributions to math and science, as well as her naval rank.")
			correct_input = True
		elif user_input == "right":
			print("Another fun fact! Grace Hopper invented the first compiler!")
			correct_input = True
		else:
			print("I don't understand that. Try again.")
			print("Hint: enter 'left' or 'right'")
			user_input = input()
	print("You're so close to getting your bug!")
	print("You reach a deadend with a door on one side and a set of stairs on the other. Which do you chose to enter?")
	correct_input = False
	user_input = input()
	while not correct_input:
		if user_input == "door":
			print("One last fun fact! Grace Hopper has a supercomputer at the National Energy Research Scientific Computing Center named after her!")
			correct_input = True
		elif user_input == "stairs":
			print("One last fun fact! Grace Hopper was a big believer in mentorship, saying training newer people was one of her most important accomplishments!")
			correct_input = True
		else:
			print("I don't understand that. Try again.")
			print("Hint: enter 'door' or 'stairs'")
			user_input = input()
	done = True
print("Thanks for playing!")
