import sys
import os
import textwrap
import time


# Initialize classes
class Player:
	def __init__(self, name="", username="", level=1, knowledgeStat=1, gutsStat=1):
		self.name = name
		self.username = username
		self.level = level
		self.knowledgeStat = knowledgeStat
		self.gutsStat = gutsStat


class Character:
	def __init__(self, name="", username=""):
		self.name = name
		self.username = username


# Initialize variables
textSpeed = 2
currentPlayer = Player()
schoolFriend = Character()
coproducerFriend = Character()
playerNameInput = ""
playerInterests = ["Writing", "Swimming", "Art"]
schoolFriendInterests = ["Sculpting", "Football", "Music"]
playerMajors = ["Architecture", "Business", "Psychology"]
currentChapter = 1
currentPosition = -1
currentBranch = -1
storyChoices = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
currentStoryChoice = 0
chapterText = [
	[
		# ['""', '{playerName}'],
		['Chapter One: "i guess i thought that [school] was gonna be fun"'],
		['"Dear Diary,"', '???'],
		['"It\'s {playerName}."', '{playerName}'],
		['"Remember when I said starting high school might have been pretty scary?"', '{playerName}'],
		['"Well..."', '{playerName}'],
		['A week ago. Orientation Day.'],
		['We are grateful to have you here. At this school, we value...', 'Principal'],
		['(Man, this assembly is boring. Wish there was something more fun to do.)', '{playerName}'],
		['You look over to the side to see what seems to be a fellow student from your class. They\'re wearing a bright yellow T-shirt with a black stripe running across it and a pair of black trousers.'],
		['(Should I introduce myself to her?)', '{playerName}', 1, ["Yes", "No"]],
		[
			['Hey. My name is {playerName}. What\'s your name?', '{playerName}', 11],
			['You refrained from introducing yourself to the classmate. Unfortunately, you couldn\'t make any friends in school afterwards and struggled to keep up with your academics as a result. Game over.', None, 10]
		],
		['Oh, hi! My name is... (Please enter their name. Leave empty for default name.)', '???', 2, ["Jamison"]],
		['...{schoolFriendName}. Nice to meet you. What hobbies are you into?', '{schoolFriendName}'],
		['Oh, well I\'m into...', '{playerName}'],
		['Present day.'],
		['"...maybe high school isn\'t so bad after all. I got to meet some new people and make some new friends."', '{playerName}'],
		['"Classes aren\'t too bad. They\'re kinda hard, but I\'m sure I\'ll get the hang of it sooner or later."', '{playerName}'],
		['"Anyways, that\'s all from me. I\'ve got high hopes for high school! (pun intended)"', '{playerName}'],
		['"- {playerName}"', '{playerName}'],
		['Chapter One End. Level Up! +1 Knowledge.']
	],
	[
		# ['""', '{playerName}'],
		['Chapter Two: "i guess i maybe had a couple expectations"'],
		['"Dear Diary,"', '{playerName}'],
		['"It\'s me again."', '{playerName}'],
		['"Unfortunately, school isn\'t going as well as I expected."', '{playerName}'],
		['"I mean, classes aren\'t as hard as they were last year, and my grades have gotten way better."', '{playerName}'],
		['"But..."', '{playerName}'],
		['"I\'m no longer friends with {schoolFriendName} and the others."', '{playerName}'],
		['"I\'m more interested in..."', '{playerName}', 3, playerInterests],
		['"...{playerInterest}, but everyone else was more into..."', '{playerName}', 3, schoolFriendInterests],
		['"...{schoolFriendInterest}. Because of our different interests, we split apart."', '{playerName}'],
		['"And I haven\'t had any luck finding new friends."', '{playerName}'],
		['"I talk to my teachers a lot but they\'re not like the friends I could make with people my age."', '{playerName}'],
		['"Everyone seems to either already be a part of a friend group or is too shy to make friends."', '{playerName}'],
		['"The latter is kinda the same deal for me..."', '{playerName}'],
		['1 week ago. Lunch break.'],
		['You\'re walking into the eating area, holding a tray full of unremarkable school food, when you overhear some students talking nearby.'],
		['So how is it in your {playerInterest} club? From what I hear, you\'re top of the club!', '???'],
		['(They seem to be into {playerInterest} as well. Should I go introduce myself to them?)', '{playerName}', 1, ["Yes", "No"]],
		[
			['Unfortunately, you don\'t have enough Guts to introduce yourself.', None, 12],
			['You didn\'t introduce yourself to the students.', None, 11]
		],
		['Yeah, you wanna see what I got so far?', '???'],
		['Present day.'],
		['"I\'m just too scared to talk to people, and I don\'t know if I\'ll ever be able to get over this fear."', '{playerName}'],
		['"I don\'t know what I\'m going to do about this problem."', '{playerName}'],
		['"...well, that\'s all I wanted to talk about. Hope things get better from here on out."', '{playerName}'],
		['"- {playerName}"', '{playerName}'],
		['Chapter Two End. Level Up! +2 Knowledge.']
	],
	[
		# ['""', '{playerName}'],
		['Chapter Three: "all i wanna do is run"'],
		['"Dear Diary,"', '{playerName}'],
		['"It\'s {playerName} again."', '{playerName}'],
		['"So while things didn\'t exactly get better since last time, there has been a nice change."', '{playerName}'],
		['"I found something I really love: music!"', '{playerName}'],
		['"Right now, I have a sort-of double life where I secretly make music with instruments and other stuff around the house."', '{playerName}'],
		['"On the internet, I\'m known as... (Please enter your username. Leave empty for default username.)"', '{playerName}', 2, ["mxmtoon"]],
		['"...{playerUsername}. So far, I\'ve made covers for my favorites songs and even wrote some original songs to put on Boundcloud."', '{playerName}'],
		['"All my songs are getting hundreds to even thousands of likes! And some people are even leaving nice comments."', '{playerName}'],
		['"But I don\'t think my parents will be happy if they found out that I \'waste\' my time making music, so I\'m keeping it all a secret for now."', '{playerName}'],
		['"Still, even if I\'m still too nervous to meet new people in real life, at least I can confidently share my music online."', '{playerName}'],
		['"I can\'t wait to make more music in the future!"', '{playerName}'],
		['"- {playerName}"', '{playerName}'],
		['Chapter Three End. Level Up! +1 Knowledge. +2 Guts.']
	],
	[
		# ['""', '{playerName}'],
		['Chapter Four: "i\'m nearing the end of my fourth year"'],
		['"Dear Diary,"', '{playerName}'],
		['"It\'s {playerName}."', '{playerName}'],
		['"Well, I guess Mom and Dad had to find out eventually."', '{playerName}'],
		['"I was getting popular on Boundcloud, and there was no way Mom and Dad weren\'t going to hear about my little music secret."', '{playerName}'],
		['"So, I built up the courage to tell them directly..."', '{playerName}'],
		['"...and it didn\'t turn out all that bad."', '{playerName}'],
		['"Mom and Dad were pretty accepting of my music."', '{playerName}'],
		['"I guess they couldn\'t deny how many likes I was getting."', '{playerName}'],
		['"For college, I was planning to major in..."', '{playerName}', 3, playerMajors],
		['"...{playerMajor}. But now with my new and now public music hobby, I might just take a gap year to focus on making music instead."', '{playerName}'],
		['"I like writing music and interacting with my fans more."', '{playerName}'],
		['"And besides, I didn\'t get accepted by most of my schools anyways, so it\'s not really a big deal."', '{playerName}'],
		['"Outside of that, the year hasn\'t been so bad."', '{playerName}'],
		['"I participated in clubs more and I helped out the underclassmen with my teachers."', '{playerName}'],
		['"I guess I\'m more of a floater, since I\'m fine with having lots of people I kinda know."', '{playerName}'],
		['"I will admit that trying to balance school with college admissions and music was pretty tough."', '{playerName}'],
		['"But that doesn\'t matter now. I can do my college admissions again next year."', '{playerName}'],
		['"Well, here\'s to an awesome year of making music!"', '{playerName}'],
		['"- {playerName}"', '{playerName}'],
		['Chapter Four End. Level Up! +2 Guts.']
	],
	[
		# ['""', '{playerName}'],
		['Chapter Five: "i\'m sitting here, crying in my prom dress"'],
		['"Dear Diary,"', '{playerName}'],
		['"It\'s me again."', '{playerName}'],
		['"Things might have blown up a little."', '{playerName}'],
		['"And by a little, I mean a lot."', '{playerName}'],
		['"In a good way, I mean."', '{playerName}'],
		['"Getting to make more music and interact with my fans has been so fun."', '{playerName}'],
		['"And now, I\'m super popular!"', '{playerName}'],
		['"Millions of people are listening to my music on Boundcloud."', '{playerName}'],
		['"And a lot more people started to stream my music when I started uploading on Whotify as well."', '{playerName}'],
		['"I\'ve started working with this really cool person called... (Please enter their name. Leave empty for default name.)"', '{playerName}', 2, ["Robin"]],
		['"...{coproducerName}, also known as... (Please enter their username. Leave empty for default username.)"', '{playerName}', 2, ["cavetown"]],
		['"...{coproducerUsername}. We\'re currently working on making this song called \'prom dress\'."', '{playerName}'],
		['"I got the idea when I thought it was a good idea to try and wear my prom dress after eating a Double Double from Enter-N-Leave."', '{playerName}'],
		['"Turns out, it wasn\'t a good idea at all and I couldn\'t fit in my prom dress."', '{playerName}'],
		['"I did eventually put on my prom dress and I had a blast at my prom (for the half hour I stayed for)."', '{playerName}'],
		['"But with this song, I want to share a story of how you often have high expectations and those expectations not being met by reality."', '{playerName}'],
		['"A story I\'m sure you\'re very familiar with."', '{playerName}'],
		['"Anyways, that\'ll be all from me. This song is going to be awesome! I\'ll be seeing you around."', '{playerName}'],
		['"- {playerName}"', '{playerName}'],
		['The End.']
	]
]


# Clears the screen by removing all text
def clearScreen():
	if (os.name == "nt"):
		os.system("cls")
	else:
		os.system("clear")


# Prints text with a scrolling effect
# Requires a line of text (string)
def scrollingPrint(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()

		# Modifies text scrolling speed
		if (textSpeed < 3):
			time.sleep(0.01 * (2 ** (2 - textSpeed)))


# Renders a textbox
# Requires a line of text (string)
# A speaker (None or a string), type of decisions (integer), and possible decisions (array of strings) are optional
# Decision type 1 is narrative multiple choice; choices will affect the story
# Decision types 10-12 are branches from decision type 1; type 10 is the incorrect branch, type 11 is the correct branch, type 12 is an impossible branch
# Decision type 2 is input; only the first of possible decisions is used, and the first possible decision is used as a default if the input is left empty
# Decision type 3 is non-narrative multiple choice; choices will not affect the story
def renderTextbox(line, speaker=None, decisionType=0, decisions=[]):
	global textSpeed

	# Wraps text
	wrapper = textwrap.TextWrapper(width=80)
	wordList = wrapper.wrap(text=line)

	choice = -1
	while (choice == -1):
		clearScreen()

		# Displays the speaker if there is one
		if (speaker != None):
			print("    +==============+")
			print("    | " + speaker[:9] + "... |    " if len(speaker) > 12 else "    | " + speaker + " " * (12 - len(speaker)) + " |")
		else:
			print()
			print()

		# Displays the textbox
		print("    +==================================================================================+")
		for element in wordList:
			print("      ", end="")
			scrollingPrint(element + "\n")
		if (len(wordList) < 4):
			for i in range(4 - len(wordList)):
				print()
		
		# Displays additional options while in game
		if (currentPosition >= 0):
			print("      [Q] Log   [W] Character   [E] Speed (" + ">" * textSpeed + " " * (3 - textSpeed) + ")                       [ENTER] Next   v")
		else:
			print("                                                                      [ENTER] Next   v")
		print("    +==================================================================================+")

		# Displays multiple choice options if the player needs to make a choice
		if (decisionType == 1 or decisionType == 3):
			count = 1
			for i in range(len(decisions)):
				wordListChoices = wrapper.wrap(text=decisions[i])
				for element in wordListChoices:
					print("      [" + str(count) + "] ", end="")
					print(element)
				count += 1
			print("    +==================================================================================+")
		
		# Displays default choice for input if the player needs to provide an input
		elif (decisionType == 2):
			print("      12 characters max")
			print("      Default: " + str(decisions[0]))
			print("    +==================================================================================+")

		try:
			choice = input("> ")

			# If the player picks an additional option, perform that option
			if ((choice.lower() == "q" or choice.lower() == "log") and currentPosition != -1):
				renderLog()
				choice = -1
			elif ((choice.lower() == "w" or choice.lower() == "character") and currentPosition != -1):
				renderCharacterPage()
				choice = -1
			elif ((choice.lower() == "e" or choice.lower() == "speed") and currentPosition != -1):
				if (textSpeed < 3):
					textSpeed += 1
				else:
					textSpeed = 1
				choice = -1

			# Otherwise, the player is either progressing through the story, making a choice, or providing their input
			else:
				if (decisionType == 0):
					continue
				elif ((decisionType == 1 and choice.isdigit() and int(choice) >= 1 and int(choice) <= len(decisions)) or (decisionType == 3 and choice.isdigit() and int(choice) >= 1 and int(choice) <= len(decisions))):
					return choice
				elif (decisionType == 2):
					if (len(choice) > 0 and len(choice) <= 12):
						return choice
					elif (len(choice) > 12):
						choice = -1
					else:
						return decisions[0]
				else:
					choice = -1
		except:
			choice = -1


# Renders the text log (up to the past 10 lines).
def renderLog():
	clearScreen()

	# Creates the wrapper
	wrapper = textwrap.TextWrapper(width=76)

	# Displays the header
	print("    +==============+")
	print("    | Log          |")
	print("    +==================================================================================+")

	choicesCount = 0
	# For up to the last 10 lines
	for logPosition in range(max(currentPosition - 9, 0), currentPosition + 1):

		# Get the current text; get the specific branch if there is one
		if (len(chapterText[currentChapter - 1][logPosition]) == 2 and len(chapterText[currentChapter - 1][logPosition][0]) == 3 and chapterText[currentChapter - 1][logPosition][0][2] >= 10):
			currentText = chapterText[currentChapter - 1][logPosition][int(storyChoices[choicesCount - 1]) - 1]
		else:
			currentText = chapterText[currentChapter - 1][logPosition]

		# Assigns specific parts of current text to variables
		currentLine = currentText[0].replace("{playerName}", currentPlayer.name).replace("{schoolFriendName}", schoolFriend.name).replace("{playerInterest}", playerInterests[int(storyChoices[2]) - 1].lower()).replace("{schoolFriendInterest}", schoolFriendInterests[int(storyChoices[3]) - 1].lower()).replace("{playerUsername}", currentPlayer.username).replace("{playerMajor}", playerMajors[int(storyChoices[6]) - 1]).replace("{coproducerName}", coproducerFriend.name).replace("{coproducerUsername}", coproducerFriend.username)
		if (len(currentText) > 1):
			currentSpeaker = currentText[1].replace("{playerName}", currentPlayer.name).replace("{schoolFriendName}", schoolFriend.name).replace("{playerInterest}", playerInterests[int(storyChoices[2]) - 1].lower()).replace("{schoolFriendInterest}", schoolFriendInterests[int(storyChoices[3]) - 1].lower()).replace("{playerUsername}", currentPlayer.username).replace("{playerMajor}", playerMajors[int(storyChoices[6]) - 1]).replace("{coproducerName}", coproducerFriend.name).replace("{coproducerUsername}", coproducerFriend.username)
		if (len(currentText) > 2):
			currentDecisionType = currentText[2]
		if (len(currentText) > 3):
			currentDecisions = currentText[3]

		# Displays the speaker if there is one
		if (len(currentText) > 1 and currentSpeaker != None):
			print("      ", end="")
			print(currentSpeaker)

		# Wraps the line of text and displays the line
		wordList = wrapper.wrap(text=currentLine)
		for element in wordList:
			print("        ", end="")
			print(element)

		# Displays player choices
		if (len(currentText) >= 3 and currentDecisionType == 1):
			if (currentDecisionType == 1):
				decisionsCount = 1
				for i in range(len(currentDecisions)):
					if (len(storyChoices) > choicesCount and int(storyChoices[choicesCount]) == decisionsCount):
						print("       >> [", end="")
					else:
						print("          [", end="")
					print(str(decisionsCount) + "] ", end="")
					print(currentDecisions[i])
					decisionsCount += 1
			elif (currentDecisionType == 2):
				print('          "', end="")
				print(storyChoices[choicesCount], end="")
				print('"')
			choicesCount += 1

		print("\n")

	print("                                                                    [ENTER] Return   v")
	print("    +==================================================================================+")

	input("> ")


# Renders the character page, displaying the player's name, username, level, knowledge stat, and guts stat.
def renderCharacterPage():
	characterPageText = [
		"{playerName}",
		"({playerUsername})",
		"Level {playerLevel}",
		"Knowledge {playerKnowledgeStat}",
		"Guts\t  {playerGutsStat}"
	]

	clearScreen()

	# Creates the wrapper
	wrapper = textwrap.TextWrapper(width=76)

	# Displays the header
	print("    +==============+")
	print("    | Character    |")
	print("    +==================================================================================+")

	# For each line of text on the character page
	for currentText in characterPageText:

		# Replaces variables in the text with actual values
		currentText = currentText.replace("{playerName}", currentPlayer.name).replace("{playerUsername}", currentPlayer.username).replace("{playerLevel}", str(currentPlayer.level)).replace("{playerKnowledgeStat}", str(currentPlayer.knowledgeStat)).replace("{playerGutsStat}", str(currentPlayer.gutsStat))

		# Adds space before each text depending on what the text is
		if (currentText == currentPlayer.name):
			print("      ", end="")
		elif (currentText == "(" + currentPlayer.username + ")"):
			if (len(currentPlayer.username) > 0):
				print(" ", end="")
			else:
				continue
		else:
			print("        ", end="")

		# Special display for the character's name and username if they have a username
		if (currentText == currentPlayer.name and len(currentPlayer.username) > 0):
			print(currentText, end="")
		elif (currentText == "(" + currentPlayer.username + ")"):
			if (len(currentPlayer.username) > 0):
				print(currentText)

		# Special display for the character's stats
		elif (len(currentText.split()) > 1 and (currentText.split()[0] == "Knowledge" or currentText.split()[0] == "Guts")):
			print(currentText + " ", end="")
			if (currentText.split()[0] == "Knowledge"):
				statNumber = currentPlayer.knowledgeStat
			elif (currentText.split()[0] == "Guts"):
				statNumber = currentPlayer.gutsStat
			else:
				statNumber = 1
			print("◼" * statNumber, end="")
			print("◻" * (5 - statNumber))

		# Regular display for everything else
		else:
			print(currentText)

	print("                                                                    [ENTER] Return   v")
	print("    +==================================================================================+")

	input("> ")


# Initializes the game and displays the title screen.
def initializeGame():
	global currentPlayer

	choice = -1

	while (choice != 0):
		clearScreen()

		print("+==========================================================================================+")
		print("                                                      __                               v0.2 ")
		print("                                                     /  |                                   ")
		print("  ______   ______   ______  _____  ____          ____$$ | ______   ______   _______ _______ ")
		print(" /      \ /      \ /      \/     \/    \        /    $$ |/      \ /      \ /       /       |")
		print("/$$$$$$  /$$$$$$  /$$$$$$  $$$$$$ $$$$  |      /$$$$$$$ /$$$$$$  /$$$$$$  /$$$$$$$/$$$$$$$/ ")
		print("$$ |  $$ $$ |  $$/$$ |  $$ $$ | $$ | $$ |      $$ |  $$ $$ |  $$/$$    $$ $$      $$      \ ")
		print("$$ |__$$ $$ |     $$ \__$$ $$ | $$ | $$ |      $$ \__$$ $$ |     $$$$$$$$/ $$$$$$  $$$$$$  |")
		print("$$    $$/$$ |     $$    $$/$$ | $$ | $$ |      $$    $$ $$ |     $$       /     $$/     $$/ ")
		print("$$$$$$$/ $$/       $$$$$$/ $$/  $$/  $$/        $$$$$$$/$$/       $$$$$$$/$$$$$$$/$$$$$$$/  ")
		print("$$ |                                                                                        ")
		print("$$ |                                                                                        ")
		print("$$/                                                                                         ")
		print("/ a short visual novel adaptation /".center(92))
		print("/ where a high school girl has unmet expectations and finds unexpected realities /".center(92))
		print("+==========================================================================================+")
		print("[1] Start Game")
		print("[0] Exit")
		print("+==========================================================================================+")

		try:
			choice = int(input("> "))
			if (choice == 1):
				playerNameInput = renderTextbox('Please enter your name. Leave empty for default name.', None, 2, ["Maia"])
				currentPlayer = Player(str(playerNameInput))
				startGame()
			elif (choice == 0):
				sys.exit()
		except ValueError:
			choice = -1


# Resets variables to their initial values and starts the game
# Plays through each chapter of the game
# Handles leveling after each chapter
def startGame():
	global currentChapter
	global currentPosition
	global currentBranch
	global storyChoices
	global currentStoryChoice

	currentChapter = 1
	currentPosition = -1
	currentBranch = -1
	storyChoices = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
	currentStoryChoice = 0
	while (currentChapter <= len(chapterText)):
		playChapter(currentChapter)

		currentPlayer.level += 1
		if (currentChapter == 1):
			currentPlayer.knowledgeStat += 1
		elif (currentChapter == 2):
			currentPlayer.knowledgeStat += 2
		elif (currentChapter == 3):
			currentPlayer.knowledgeStat += 1
			currentPlayer.gutsStat += 2
		elif (currentChapter == 4):
			currentPlayer.gutsStat += 2
		currentChapter += 1


# Plays a specific chapter
# Requires a chapter number
def playChapter(chapter):
	global currentPlayer
	global schoolFriend
	global coproducerFriend
	global storyChoices
	global currentStoryChoice
	global currentChapter
	global currentPosition
	global currentBranch

	currentPosition = 0
	currentChapterText = chapterText[chapter - 1]

	while (currentPosition < len(currentChapterText)):

		# Get the current text; get the specific branch if there is one
		if (currentBranch == -1):
			currentText = currentChapterText[currentPosition]
		else:
			currentText = currentChapterText[currentPosition][currentBranch]

		# Assigns specific parts of current text to variables
		currentLine = currentText[0].replace("{playerName}", currentPlayer.name).replace("{schoolFriendName}", schoolFriend.name).replace("{playerInterest}", playerInterests[int(storyChoices[2]) - 1].lower()).replace("{schoolFriendInterest}", schoolFriendInterests[int(storyChoices[3]) - 1].lower()).replace("{playerUsername}", currentPlayer.username).replace("{playerMajor}", playerMajors[int(storyChoices[6]) - 1]).replace("{coproducerName}", coproducerFriend.name).replace("{coproducerUsername}", coproducerFriend.username)
		if (len(currentText) > 1 and currentText[1] != None):
			currentSpeaker = currentText[1].replace("{playerName}", currentPlayer.name).replace("{schoolFriendName}", schoolFriend.name).replace("{playerInterest}", playerInterests[int(storyChoices[2]) - 1].lower()).replace("{schoolFriendInterest}", schoolFriendInterests[int(storyChoices[3]) - 1].lower()).replace("{playerUsername}", currentPlayer.username).replace("{playerMajor}", playerMajors[int(storyChoices[6]) - 1]).replace("{coproducerName}", coproducerFriend.name).replace("{coproducerUsername}", coproducerFriend.username)
		else:
			currentSpeaker = None
		if (len(currentText) > 2 and currentText[2] != 0):
			currentDecisionType = currentText[2]
		else:
			currentDecisionType = 0
		if (len(currentText) > 3 and currentText[3] != []):
			currentDecisions = currentText[3]
		else:
			currentDecisions = []

		# Displays the textbox
		if (len(currentText) == 1):
			renderTextbox(currentLine)
		elif (len(currentText) == 2 or len(currentText) == 3 and currentDecisionType >= 10):
			renderTextbox(currentLine, currentSpeaker)
		elif (len(currentText) == 3):
			storyChoices[currentStoryChoice] = renderTextbox(currentLine, currentSpeaker, currentDecisionType)
			currentStoryChoice += 1
		elif (len(currentText) == 4):
			storyChoices[currentStoryChoice] = renderTextbox(currentLine, currentSpeaker, currentDecisionType, currentDecisions)
			if (currentDecisionType == 1):
				currentBranch = int(storyChoices[currentStoryChoice]) - 1
			currentStoryChoice += 1

		# If the player needed to make a choice
		if (len(currentText) == 3 and currentDecisionType >= 10):

			# If the player made the incorrect choice, show the retry menu
			if (currentDecisionType == 10):
				gameOverChoice = renderTextbox("Would you like to retry?", None, 1, ["Redo the last choice", "Restart the chapter", "Return to title screen"])

				# Redo the last choice
				if (int(gameOverChoice) == 1):
					currentPosition -= 2
					currentStoryChoice -= 1

				# Restart the chapter
				elif (int(gameOverChoice) == 2):
					currentPosition = -1
					if (currentChapter == 1):
						currentStoryChoice = 0
					elif (currentChapter == 2):
						currentStoryChoice = 2
					elif (currentChapter == 3):
						currentStoryChoice = 5
					elif (currentChapter == 4):
						currentStoryChoice = 6
					elif (currentChapter == 5):
						currentStoryChoice = 7

				# Return to title screen
				elif (int(gameOverChoice) == 3):
					currentPosition = len(currentChapterText)

			# If the player made an impossible choice, go back to the position where they need to make a choice
			elif (currentDecisionType == 12):
				currentPosition -= 2
				currentStoryChoice -= 1
			currentBranch = -1

		# Specific character naming events
		if (currentChapter == 1 and currentStoryChoice - 1 == 1 and int(storyChoices[0]) == 1):
			schoolFriend = Character(storyChoices[currentStoryChoice - 1])
		elif (currentChapter == 3 and currentStoryChoice - 1 == 5):
			currentPlayer.username = storyChoices[currentStoryChoice - 1]
		elif (currentChapter == 5 and currentStoryChoice - 1 == 7):
			coproducerFriend = Character(storyChoices[currentStoryChoice - 1])
		elif (currentChapter == 5 and currentStoryChoice - 1 == 8):
			coproducerFriend.username = storyChoices[currentStoryChoice - 1]

		currentPosition += 1


initializeGame()