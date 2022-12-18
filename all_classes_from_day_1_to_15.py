"""UDEMY COURSE"""

"""100 days code exercises challenge"""


# day 1 - "band name generator" project

def band_name_gen():
    # 1. Create a greeting for your program.
    print("Welcome to the band name generator")
    # 2. Ask the user for the city that they grew up in.
    city = input("wich city you grew up?\n")
    # 3. Ask the user for the name of a pet.
    pet_name = input("Whats the name of your pet?\n")
    # 4. Combine the name of their city and pet and show them their band name.

    return print("your band name could be " + city + " " + pet_name)


def BMI_calculator():  # version 2.0
    height = float(input("enter your height in cm: "))
    weight = float(input("enter your weight in kg: "))
    height /= 100
    height *= height

    bmi = round(weight / height, 2)

    if bmi < 18.5:
        print(f"you are under weight with {bmi} BMI")
    elif 18.5 <= bmi < 25:
        print(f"you have a normal weight with {bmi} BMI")
    elif 25 <= bmi < 30:
        print(f"you are slightly overweight with {bmi} BMI")
    elif 30 <= bmi < 35:
        print(f"you are obese with {bmi} BMI")
    else:
        print(f"you are clinically obese with {bmi} BMI")

    return bmi


# Day 2 - "Tip calculator" project

def tip_calculator(bill=150, ppl=5, tip_rate=0.12):
    """If the bill was $150.00, split between 5 people, with 12% tip.
    Each person should pay (150.00 / 5) * 1.12 = 33.6
    Format the result to 2 decimal places = 33.60
    Tip: There are 2 ways to round a number"""

    print("Welcome to the tip calculator\n")

    bill = float(input("whats the total bill $"))

    ppl = int(input("How many people to pay? "))

    tip_rate = float("1." + input("Whats the tip rate? 10, 12, 15? "))

    # TASK: make this program "user fail-safe"
    # while bill <= 0:
    #     print("The bill must be bigger than 0")
    #     bill = float(input("whats the total"))
    #
    # while ppl == 0:
    #     print("division by 0 not defined!\n")
    #     ppl = int(input("How many people to pay? "))
    #
    # while tip_rate <= 0 or tip_rate >= 1:
    #     abs(tip_rate)
    #
    #     if tip_rate == 0:
    #         print("you are a nasty customer")
    #
    #     if tip_rate is int:
    #         print('tip rate should be in "0.10" format, you place a integer that will be formated to float format')
    #         tip_rate /= 100
    #     else:
    #         print("invalid tip rate")
    #         input("What's the tip rate? ")

    return f"the split bill per person is {round((bill / ppl) * tip_rate, 2):.2f}"


class YearClass:
    def __init__(self, year, month):
        # def __init__(self, year=int(input("Enter a year: ")), month=int(input("Enter a month: "))):
        self.year = year
        self.month = month
        self.days = YearClass.days_in_month(self)
        # TASK: make the class print this
        print(self.days)

    def is_leap(self):
        """returns true or false"""

        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def days_in_month(self):
        """returns the amount of days of an specific month in a determined year"""
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if YearClass.is_leap(self) and self.month == 2:
            return 29
        return month_days[self.month - 1]


# Day 3 - "Treasure Island" project

def treasure_island():
    """a simple game to learn if staments"""
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    answer1 = input('at the edge of a road type "left" to go left or "rigth" to go right ').lower()

    if answer1 == "left":
        answer2 = input('you found a lake, type "wait" for waiting for a boat or "swim" to swim ').lower
        if answer2 == "wait":
            answer3 = input(
                'you found an island with a house that have trhee doors, type "red" for open the red door, '
                '"yellow" for yellow door or "blue" for the blue one').lower
            if answer3 == "yellow":
                input("you found a treasure chest and you found inside... ").lower()
                print('You found DEATH!!!!')
            else:
                print('You found DEATH!!!!')
        else:
            print('You found DEATH!!!!')
    else:
        print('You found DEATH!!!!')


# Day 4 - "Rock, Paper, Scissors" project

def who_pays():
    """a class exercises to learn import"""
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")

    import random

    ppl = len(names)
    payer = random.randint(0, ppl - 1)

    print(f"The payer is {names[payer]}")


def who_pays_2():
    """a simple game to random select from a list of names"""
    import random

    print(f"""The payer is {random.choice(input("Give me everybody's names, separated by a comma. ").split(", "))}""")


def emojis_():
    """a random choice of emojis"""
    import random
    emojis = ["💪", "😀", "🍆"]
    print(f"{random.choice(emojis)}")


def treasure_map():
    """a game to learn 2D list"""
    row1 = ["⬜️", "⬜️", "⬜️"]
    row2 = ["⬜️", "⬜️", "⬜️"]
    row3 = ["⬜️", "⬜️", "⬜️"]

    map = [row1, row2, row3]

    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")

    row = int(position[0]) - 1
    column = int(position[1]) - 1

    map[column][row] = "X"

    print(f"{row1}\n{row2}\n{row3}")


def rock_paper_scissors():  # project
    """good 'ol game of rock-paper-scissors"""

    import random

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    display = [rock, paper, scissors]

    choices = [rock, paper, scissors]
    emoji = ["✊", "✋", "✌"]

    player_choice = int(input(f"choose your hand number:\n {display}\n "
                              f"your choice is: ")) - 1

    cpu_choice = random.choice(choices)

    # logic math
    """
    0-1 = -1 loose,
    1-0 = 1 win,
    1-2 = -1 loose,
    0-2 = -2 win,
    2-0 = 2 loose,
    2-1 = 1 win"""

    cpu_num = choices.index(cpu_choice)
    player_num = player_choice

    result = player_num - cpu_num

    print("\n")
    print(f"Your choice is:\n{emoji[player_num]}\nCPU choice is:\n{emoji[cpu_num]}")

    if player_choice > 3 or player_choice <= 0:
        print("you typed an invalid number, you loose!!")
    elif result == -1 or result == 2:
        print("You loose!")
    elif result == 1 or result == -2:
        print("You win!!!")
    else:
        print("TIE!!!")


# rock_paper_scissors()


# day 5 - "Pasword generator"

# Password Generator Project
def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
    return password


# class exercise - " fizz buzz game"

def fizz_buzz_game():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(f"{num}")


# Day 6 - "Reeborg World: scape challenge"

# class exercise

"""def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if not at_goal():
        while not wall_in_front():
            move()
        turn_left()
        while not right_is_clear():
            move()
        turn_right()
        move()
        turn_right()
        while not wall_in_front():
            move()
        turn_left()

while not at_goal():
    jump()"""

"""class project (my solution)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right():
       turn_left()
    else:
       turn_right()

    loop = 0

    while not wall_in_front() and not at_goal():
        move()
        if loop == 5:
            turn_left()
        if not wall_in_front and wall_on_rigth():
            move()
        elif not wall_on_right():
            turn_right()

        loop += 1
        """

"""class project (teacher solution)
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_rigth()
        move()

    elif front_is_clear():
        move()
    else: 
        turn_left()
"""


# Day 7 - "Hangman Game"

# exercise 1


class Hangman:
    """hang a man fur fun"""

    # from replit import clear # only in repl.it

    def __init__(self):
        """you know inits"""
        self.word_list = [
            'abruptly',
            'absurd',
            'abyss',
            'affix',
            'askew',
            'avenue',
            'awkward',
            'axiom',
            'azure',
            'bagpipes',
            'bandwagon',
            'banjo',
            'bayou',
            'beekeeper',
            'bikini',
            'blitz',
            'blizzard',
            'boggle',
            'bookworm',
            'boxcar',
            'boxful',
            'buckaroo',
            'buffalo',
            'buffoon',
            'buxom',
            'buzzard',
            'buzzing',
            'buzzwords',
            'caliph',
            'cobweb',
            'cockiness',
            'croquet',
            'crypt',
            'curacao',
            'cycle',
            'daiquiri',
            'dirndl',
            'disavow',
            'dizzying',
            'duplex',
            'dwarves',
            'embezzle',
            'equip',
            'espionage',
            'euouae',
            'exodus',
            'faking',
            'fishhook',
            'fixable',
            'fjord',
            'flapjack',
            'flopping',
            'fluffiness',
            'flyby',
            'foxglove',
            'frazzled',
            'frizzled',
            'fuchsia',
            'funny',
            'gabby',
            'galaxy',
            'galvanize',
            'gazebo',
            'giaour',
            'gizmo',
            'glowworm',
            'glyph',
            'gnarly',
            'gnostic',
            'gossip',
            'grogginess',
            'haiku',
            'haphazard',
            'hyphen',
            'iatrogenic',
            'icebox',
            'injury',
            'ivory',
            'ivy',
            'jackpot',
            'jaundice',
            'jawbreaker',
            'jaywalk',
            'jazziest',
            'jazzy',
            'jelly',
            'jigsaw',
            'jinx',
            'jiujitsu',
            'jockey',
            'jogging',
            'joking',
            'jovial',
            'joyful',
            'juicy',
            'jukebox',
            'jumbo',
            'kayak',
            'kazoo',
            'keyhole',
            'khaki',
            'kilobyte',
            'kiosk',
            'kitsch',
            'kiwifruit',
            'klutz',
            'knapsack',
            'larynx',
            'lengths',
            'lucky',
            'luxury',
            'lymph',
            'marquis',
            'matrix',
            'megahertz',
            'microwave',
            'mnemonic',
            'mystify',
            'naphtha',
            'nightclub',
            'nowadays',
            'numbskull',
            'nymph',
            'onyx',
            'ovary',
            'oxidize',
            'oxygen',
            'pajama',
            'peekaboo',
            'phlegm',
            'pixel',
            'pizazz',
            'pneumonia',
            'polka',
            'pshaw',
            'psyche',
            'puppy',
            'puzzling',
            'quartz',
            'queue',
            'quips',
            'quixotic',
            'quiz',
            'quizzes',
            'quorum',
            'razzmatazz',
            'rhubarb',
            'rhythm',
            'rickshaw',
            'schnapps',
            'scratch',
            'shiv',
            'snazzy',
            'sphinx',
            'spritz',
            'squawk',
            'staff',
            'strength',
            'strengths',
            'stretch',
            'stronghold',
            'stymied',
            'subway',
            'swivel',
            'syndrome',
            'thriftless',
            'thumbscrew',
            'topaz',
            'transcript',
            'transgress',
            'transplant',
            'triphthong',
            'twelfth',
            'twelfths',
            'unknown',
            'unworthy',
            'unzip',
            'uptown',
            'vaporize',
            'vixen',
            'vodka',
            'voodoo',
            'vortex',
            'voyeurism',
            'walkway',
            'waltz',
            'wave',
            'wavy',
            'waxy',
            'wellspring',
            'wheezy',
            'whiskey',
            'whizzing',
            'whomever',
            'wimpy',
            'witchcraft',
            'wizard',
            'woozy',
            'wristwatch',
            'wyvern',
            'xylophone',
            'yachtsman',
            'yippee',
            'yoked',
            'youthful',
            'yummy',
            'zephyr',
            'zigzag',
            'zigzagging',
            'zilch',
            'zipper',
            'zodiac',
            'zombie',
        ]

        self.stages = ['''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        ''', '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''']

        self.logo = ''' 
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/    '''

    @staticmethod
    def step_1():

        # Step 1

        word_list = ["aardvark", "baboon", "camel"]

        # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
        import random

        chosen_word = random.choice(word_list)

        # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess
        #  lowercase.

        guess = input("guess a letter: ").lower()

        # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

        for letter in chosen_word:
            if guess == letter:
                print(f"right, {letter}-{guess} ")
            else:
                print(f"grong, {letter}-{guess} ")

    @staticmethod
    def step_2():
        # Step 2

        import random
        word_list = ["aardvark", "baboon", "camel"]
        chosen_word = random.choice(word_list)

        # Testing code
        print(f'Pssst, the solution is {chosen_word}.')

        # TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
        #  So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing
        #  each letter to guess.

        display = []
        for n in range(len(chosen_word)):
            display += "_"

        print(display)

        guess = input("Guess a letter: ").lower()

        # TODO-2: - Loop through each position in the chosen_word; If the letter at that position matches 'guess'
        #  then reveal that letter in the display at that position. e.g. If the user guessed "p" and the chosen word
        #  was "apple", then display should be ["_", "p", "p", "_", "_"].

        index = 0
        for letter in chosen_word:
            if letter == guess:
                display[index] = letter
                print("Right")
            else:
                print("Wrong")
            index += 1

        """teachers solution of above for loop"""

        # for position in range(len(chosen_word)):
        #     letter = chosen_word[position]  # added
        #     if letter == guess:
        #         display[position] = letter  # changed
        #         print("Right")
        #     else:
        #         print("Wrong")

        # TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other
        #  letter replace with "_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle
        #  that in step 3.

        print(display)

    @staticmethod
    def step_3():

        # Step 3

        import random
        word_list = ["aardvark", "baboon", "camel"]
        chosen_word = random.choice(word_list)
        word_length = len(chosen_word)

        # Testing code
        print(f'Pssst, the solution is {chosen_word}.')

        # Create blanks
        display = []
        for _ in range(word_length):
            display += "_"

        # TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
        #  all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user
        #  they've won.

        game_on = True

        while game_on:
            guess = input("Guess a letter: ").lower()

            # Check guessed letter
            for position in range(word_length):
                letter = chosen_word[position]
                # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                if letter == guess:
                    display[position] = letter

            # Check blank spaces left
            left_blank = word_length

            for item in display:
                if item != "_":
                    left_blank -= 1
                if left_blank == 0:
                    print("you win!")
                    game_on = False

            print(display)

    @staticmethod
    def step_3_2():  # CHANGED the while main loop condition and the teachers solution added

        # Step 3

        import random
        word_list = ["aardvark", "baboon", "camel"]
        chosen_word = random.choice(word_list)
        word_length = len(chosen_word)

        # Testing code
        print(f'Pssst, the solution is {chosen_word}.')

        # Create blanks
        display = []
        for _ in range(word_length):
            display += "_"

        # TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
        #  all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user
        #  they've won.

        while "_" in display:
            guess = input("Guess a letter: ").lower()

            # Check guessed letter
            for position in range(word_length):
                letter = chosen_word[position]
                # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                if letter == guess:
                    display[position] = letter

            print(display)

            # Check blank spaces left
            if not "_" in display:
                print("you win!")

    @staticmethod
    def step_4():

        import random

        stages = ['''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        ''', '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''']

        end_of_game = False
        word_list = ["ardvark", "baboon", "camel"]
        chosen_word = random.choice(word_list)
        word_length = len(chosen_word)

        # TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
        lives = 6

        # Testing code
        print(f'Pssst, the solution is {chosen_word}.')

        # Create blanks
        display = []
        for _ in range(word_length):
            display += "_"

        while not end_of_game:
            guess = input("Guess a letter: ").lower()

            # Check guessed letter
            for position in range(word_length):
                letter = chosen_word[position]
                # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                if letter == guess:
                    display[position] = letter

                # TODO-2: - If guess is not a letter in the chosen_word,Then reduce 'lives' by 1. If lives goes down
                #  to 0then the game should stop and it should print "You lose."

            if guess not in chosen_word:
                lives -= 1
                if lives == 0:
                    print("you loose")
                    end_of_game = True

            # Join all the elements in the list and turn it into a String.
            print(f"{' '.join(display)}")

            # Check if user has got all letters.
            if "_" not in display:
                end_of_game = True
                print("You win.")

            # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user
            #  has remaining.
            print(stages[lives])

    def step_5(self):

        import random
        # import hangman_art # from other file
        # import hangman_words # from other file

        # TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

        chosen_word = random.choice(self.word_list)
        word_length = len(chosen_word)

        end_of_game = False
        lives = 6

        # TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

        print(self.logo)

        # Testing code
        print(f'Pssst, the solution is {chosen_word}.')

        # Create blanks
        display = []
        guessed = []

        for _ in range(word_length):
            display += "_"

        while not end_of_game:
            guess = input("Guess a letter: ").lower()

            if guess not in guessed:
                guessed += guess

                # Check guessed letter
                for position in range(word_length):
                    letter = chosen_word[position]
                    # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                    if letter == guess:
                        display[position] = letter

                # Check if user is wrong.
                if guess not in chosen_word:
                    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's
                    #  not in the word.
                    print(f'letter "{guess}" is not in the word')
                    lives -= 1
                    if lives == 0:
                        end_of_game = True
                        print("You lose.")

            # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
            else:
                print(f'letter "{guess}" already entered')

            # Join all the elements in the list and turn it into a String.
            print(f"{' '.join(display)}")

            # Check if user has got all letters.
            if "_" not in display:
                end_of_game = True
                print("You win.")

            # TODO-2: - Import the stages from hangman_art.py and make this error go away.
            print(self.stages)


# Day 8 - "Cypher Encryption"

def prime_checker():  # class exercise
    tired = False
    while not tired:
        number = int(input("Check this number: "))

        if number == "exit":
            tired = True
            break

        else:
            for x in range(2, number):
                if number % x == 0:
                    print(f"{number} It's not a prime number.\n")
                    break
                else:
                    print(f"{number} Is a prime number.\n")
                    break


# "cypher encrypt" class project

def caesar():
    logo = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """

    print(logo)
    again = True

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    while again:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        alt_alphabet = []
        cipher_text = ""

        for item in alphabet:
            alt_alphabet.append(item)

        for letter_index in range(shift):
            alt_alphabet.append(alt_alphabet[0])
            alt_alphabet.remove(alt_alphabet[0])

        if direction == "encode":

            for letter in text:
                position = alphabet.index(letter)
                cipher_text += alt_alphabet[position]

        elif direction == "decode":
            for letter in text:
                position = alt_alphabet.index(letter)
                cipher_text += alphabet[position]

        print(f"The {direction}d text is {cipher_text}")

        answer = input('type "yes" to try again?')
        if answer != "yes":
            again = False
            print("Good bye!")


#  Day 9 - "Auction bids"

def auction_bid():
    logo = '''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    '''

    print(logo)

    bid_dict = {}
    more_bids = True
    while more_bids:
        name = input("whats your name:")
        bid = int(input("whats your bid:"))

        bid_dict[name] = bid

        answer = input("are more bidders? ")
        if answer != "yes":
            more_bids = False

        # clear()

    bigger_bid = 0
    winner = ""
    for name, bid in bid_dict.items():
        if bid_dict[name] > bigger_bid:
            bigger_bid = bid_dict[name]
            winner = name

    print(f"the winner is {winner}")


#  Day 10 - "good'ol calculator"

def calculator():
    """notice the usage of the dictionary to save functions, and further, the way functions are called!!!"""

    logo = """
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    print(logo)

    # TASK: create more functions square, square root, 0 div proof.
    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    def mul(n1, n2):
        return n1 * n2

    def div(n1, n2):
        if n2 > 0:
            return n1 / n2

    calc_dict = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    def calculator_inner():
        num1 = int(input("type the first number: "))

        cont = True
        while cont:

            options = ""
            for key in calc_dict:
                options += f"{key} "

            operation = input(f"type an operator ( {options}): ")

            num2 = int(input("type the next number: "))

            calculation = calc_dict[
                operation]  # this converts variable calculation in the name of the calculation function (add, sub, mul, div)!!!

            result = calculation(num1,
                                 num2)  # using the name of the variable calculation to call the name of the function !!!!!!!!!

            print(f"{num1} {operation} {num2} = {result}")

            jatka = input("type 'y' to add an operation else to quit: ")
            if jatka == "y":
                num1 = result
            else:
                cont = False
                calculator_inner()  # recursion, function calling itself
                print("\n")

    return calculator_inner()


# Day 11 - "Black Jack"
def black_jack():
    """
    - if the dealer scores less than 17 it must take a card
    """

    import random
    from functools import reduce

    dealer_hand = []
    player_hand = []
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_deck_dict = {}

    def reset_values():  # checked
        dealer_hand.clear()
        player_hand.clear()

    def print_logo():  # CHECKED
        logo = """
                .------.            _     _            _    _            _    
                |A_  _ |.          | |   | |          | |  (_)          | |   
                |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
                | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
                |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
                `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                      |  \/ K|                            _/ |                
                      `------'                           |__/           
                """
        return print(logo)

    def create_deck():  # CHECKED
        """returns a dictionary of each card in a card deck with str key ("a♥") and its int value"""
        card_symbols = ["♥", "♦", "♠", "♣"]
        card_values = ["a", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

        for symbol in card_symbols:  # create a set of cards
            for value in card_values:
                if value is int:
                    points = value
                elif value == "a":
                    points = 11
                else:
                    points = 10
                card_deck_dict[f"{value}{symbol}"] = points

        return print([key for key, value in card_deck_dict.items()]), card_deck

    def draw_a_card():  # CHECKED
        """returns a random card from the deck"""
        return random.choice(card_deck)

    def change_value(hand):  # CHECKED
        """changes the first value of 11 that finds to 1 and returns changed list"""
        for card in hand:
            if card == 11:
                hand[hand.index(card)] = 1
                return hand

    def check_hand_total(hand):  # CHECKED
        """add toguether all values and returns int total"""
        total = reduce(lambda x, y: x + y, hand)
        if total > 21 and hand.count(11) >= 1:
            doubs = True
            laps = hand.count(11)
            test_hand = hand
            while laps > 0:
                test_hand = change_value(test_hand)
                test_total = reduce(lambda x, y: x + y, test_hand)
                if test_total != total and test_total <= 21:
                    return test_total
                laps -= 1
        return total

    def dealer_move(hand_value):  # CHECKED
        """determine if dealer(CPU) draws more cards or not, calls check_hands, returns list "hand" and the total value"""
        while hand_value < 17:
            dealer_hand.append(random.choice(card_deck))
            hand_value = check_hand_total(dealer_hand)
        return dealer_hand, hand_value

    def who_wins(dealer, player):  # CHECKED
        """takes 2 int and comapares closest to 21"""

        if player < dealer <= 21:
            print("dealer wins")
        elif dealer < player <= 21:
            print("player wins")
        elif player > 21:
            print("dealer wins")
        elif dealer > 21:
            print("player wins")
        elif dealer == player and dealer <= 21 and player <= 21:
            print(" draw ")
        else:
            print("esto que pinga e?")

    def print_hands():
        print(
            f"dealer hand: {dealer_hand}, {check_hand_total(dealer_hand)}\nplayer hand: {player_hand}, {check_hand_total(player_hand)}")

    def UI_():
        answer_1 = input('would you like to play a "BLACK JACK" match? [y/n]: ')
        if answer_1 == "y":
            player_hand.append(draw_a_card())
            player_hand.append(draw_a_card())
            dealer_hand.append(draw_a_card())
            dealer_hand.append(draw_a_card())

            playing = True

            if check_hand_total(player_hand) >= 21:
                playing = False
            while playing:
                print(
                    f"dealer hand: [X,{dealer_hand[1]}] \nplayer hand: {player_hand}, {check_hand_total(player_hand)}")
                answer_2 = input('"hit me" or "stand" [y/n]:')
                if answer_2 == "y":
                    player_hand.append(draw_a_card())
                    if check_hand_total(player_hand) >= 21:
                        playing = False
                else:
                    playing = False

            dealer_move(check_hand_total(dealer_hand))
            print_hands()
            who_wins(check_hand_total(dealer_hand), check_hand_total(player_hand))
            reset_values()
            return answer_1
        else:
            return answer_1

    def main_loop():
        print_logo()
        game_on = True
        while game_on:
            one_more = UI_()
            if one_more != "y":
                game_on = False

    main_loop()


# Day 12 - "Guess my number"

def guess_my_number():
    import random

    logo = """                                                                     _               
                                                                    | |              
   __ _ _   _  ___ ___ ___   _ __ ___  _   _   _ __  _   _ _ __ ___ | |__   ___ _ __ 
  / _` | | | |/ _ / __/ __| | '_ ` _ \| | | | | '_ \| | | | '_ ` _ \| '_ \ / _ | '__|
 | (_| | |_| |  __\__ \__ \ | | | | | | |_| | | | | | |_| | | | | | | |_) |  __| |   
  \__, |\__,_|\___|___|___/ |_| |_| |_|\__, | |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
   __/ |                                __/ |                                        
  |___/                                |___/  
    """
    print(logo)

    def generate_num():
        return random.choice([num for num in range(100)])

    choice_number = generate_num()

    def set_difuiculty():
        print("the number is", choice_number)
        answer = "x"
        while answer != 1 != 2:
            answer = input("type 1 for easy game or 2 for difficult game: ")
            if answer == "1":
                return 10
            elif answer == "2":
                return 5
            else:
                print("wrong input!!")

    def restart():
        restart = input("wanna play again? [y/n]: ")
        if restart == "y":
            generate_num()
            return set_difuiculty()

        else:
            print("game terminated")
            return 0

    chances = set_difuiculty()

    while chances > 0:
        print(f"you have {chances} chances left")
        guess = int(input("guess my number: "))
        chances -= 1
        if guess == choice_number:
            print("yaaaay!!")

            chances = restart()

        elif guess < choice_number:

            print("too low")
        elif guess > choice_number:

            print("too high")

        if chances == 0:
            print("you run out of chances ")
            chances = restart()


# day 13 - "debugging"

"""try to not use global variables"""

# day 14 - "Higher-Lower game"
import random

POINTS = 0

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi b',
        'follower_count': 67,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def print_logo():
    """display logo"""
    print(logo)


def generate_data():
    """generates a random data from dict, erases the item from that list and returns it"""
    item = random.choice(data)  # ok returns dictionary
    position = data.index(item)  # ok returns int(index)
    del data[position]  # ok deletes the data from list
    return item


def compare_results(a, b):
    """compare two int "a" and "b",
     returns:
     0 if a is bigger
     1 if b is bigger
     2 if they are iquals"""

    if a > b:
        return "a"
    elif a < b:
        return "b"
    else:
        return 0


def swap_data(data_b):
    print()
    higher_lower(data_b)


def display_formated_data(dats):
    print(f"Followers: {dats['follower_count']} millions")  # secret data to guess
    return print(f"Name: {dats['name']}, a {dats['description']} from {dats['country']}")


def higher_lower(data_A=generate_data()):  # if user data is not passed in parameter then generate a new
    """main loop of the entire game, call most of the function and itself, depends of user choices, returns 0"""
    global POINTS

    print_logo()

    # data_A = generate_data()  # display data a

    print(f"You have earned {POINTS} points\n")

    display_formated_data(data_A)

    print(vs)  # display vs art

    data_B = generate_data()  # display data b
    display_formated_data(data_B)

    # ask user opinion
    answer = input("\nWhich of this ones has more instagram followers [A/B]?: ").lower()

    # compare answer
    result = compare_results(data_A['follower_count'], data_B['follower_count'])
    if result == answer:  # if right add point
        POINTS += 1
        swap_data(data_B)  # data b turns into data a and generate new data b
    elif result != answer:
        if result == "a" or result == "b":  # if wrong end game
            print("Wrong answer!!")
            input("press enter to continue...")
            POINTS = 0
            more = input("Would you like to play again? [Y/N]: ")
            if more == "y":  # restart main loop
                higher_lower()

        print("thans for playing, game terminated")
        return 0
    return 0


# Day 15 - "Coffee machine"
def coffee_machine():
    """Coffee Machine Program"""
    in_use = False

    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }

    logo = """ ______         ___   ___             
     / _____)       / __) / __)            
    | /       ___  | |__ | |__  ____  ____ 
    | |      / _ \ |  __)|  __)/ _  )/ _  )
    | \_____| |_| || |   | |  ( (/ /( (/ / 
     \______)\___/ |_|   |_|   \____)\____)"""

    print(logo)

    def make_coffee(coffee):  # working ok
        """takes a dictionary, calls the main prompt()"""

        completed_coffee = False

        for ingredient, value in MENU[coffee]["ingredients"].items():

            test = resources[ingredient] - value
            if test >= 0:
                resources[ingredient] -= value
                completed_coffee = True
            else:
                print(f'⚠ not enough resource "{ingredient}" to make your coffee')
                refound_money(MENU[coffee].get("cost"))
                prompt()

        if completed_coffee:
            resources["money"] += MENU[coffee].get("cost")
            print("here is your coffee!"),
            prompt()

    def refill():
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print("resources refilled!")

    def switch_power(turn_on=True):
        """a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        the machine. Your code should end execution when this happens."""
        if turn_on:
            prompt(False)
        elif not turn_on:
            prompt(True)

    def print_report():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    def refound_money(amount):
        print(f"Here is ${amount:.2f} dollars in change.")

    def prompt(turn_on=True):
        """a. Check the user’s input to decide what to do next.
        b. The prompt should show every time action has completed, e.g. once the drink is
        dispensed. The prompt should show again to serve the next customer."""

        menu = ""

        for item in MENU:
            menu += f"/{item}"

        while True:
            if turn_on:

                order = input(f"“What would you like? {menu}:")

                if order == "espresso" or order == "latte" or order == "cappuccino":
                    Check_transaction(order)
                elif order == "off":

                    switch_power()
                elif order == "report":

                    print_report()
            else:
                order = input("power off. Standby... ")
                if order == "on":
                    switch_power(False)
                elif order == "refill":
                    refill()

                else:
                    prompt(False)

    def coins():
        "returns variable money (total of all coins)"
        coin_dict = {"a": 0.25, "b": 0.10, "c": 0.05, "d": 0.01}
        coin_list = []
        money = 0
        cash_list = []

        print("type [a/b/c/d] to insert coins")
        print("a) quarters = $0.25, b) dimes = $0.10, c) nickles = $0.05, d) pennies = $0.01")
        cash = input("insert coins...")
        for item in cash:
            if item in coin_dict:
                money += coin_dict.get(item)
                cash_list.append(coin_dict.get(item))
            else:
                print(f"this item '{item}' is not e propper coin, returned!!")

        for coin in cash_list:
            print(f"{coin:.2f}, ", end="")

        print(f"\ntotal ${money:.2f}")
        return float(money)

    def Check_transaction(coffee, money=None):
        """takes dictionary 'coffee' as argument, Checks transaction successful, calls prompt() if false to loop or calls
        makecoffee() if true """

        if not money:
            money = coins()

        price = MENU[coffee]["cost"]

        if money >= price:
            if money > price:
                refound_money(money - price)

            make_coffee(coffee)
        else:
            print(f"Sorry that's not enough money. {money:.2f} refunded")

            prompt()

# day 16 - "Object oriented programing (OOP) the coffee machine again :)"

# CLASS NOTES:
# from turtle import Turtle, Screen
#
# timy = Turtle()
# timy.shape("turtle")
# timy.color("coral")
# timy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
