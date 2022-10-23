import random


class Figure():
    def __init__(self, name: str) -> None:

        self.base = f"""
        ---------------
        |      | 
        |      
        |
        |
        |
        ^^^^^^^^^^^^^^^
\"{name} isn't present yet. Try to get all guesses correctly to not hurt {name} at all!\"
        """

        self.hang1 = f"""
        ---------------
        |      | 
        |      O
        |
        |
        |
        ^^^^^^^^^^^^^^^
\"OOF! {name}'s head is here , that oughta hurt\"
        """

        self.hang2 = f"""
        ---------------
        |      | 
        |      O
        |      |
        |
        |
        ^^^^^^^^^^^^^^^
\"If you bring your head closer to the screen , you can hear {name}'s screams\"
        """

        self.hang3 = f"""
        ---------------
        |      | 
        |      O
        |      |\\
        |
        |
        ^^^^^^^^^^^^^^^
\"NOOOO! not {name}'s right hand , he needed it for a lot of stuff. lot of stuff.....\"
        """

        self.hang4 = f"""
        ---------------
        |      | 
        |      O
        |     /|\\
        |
        |
        ^^^^^^^^^^^^^^^
\"Welp , you can still try to save {name}'s legs.... walking is kind of a important thing you know\"
        """

        self.hang5 = f"""
        ---------------
        |      | 
        |      O
        |     /|\\
        |     /
        |
        ^^^^^^^^^^^^^^^
\"You might as well let {name} die at this point....\"
        """

        self.hang6 = f"""
        ---------------
        |      | 
        |      O
        |     /|\\
        |     / \\
        |
        ^^^^^^^^^^^^^^^
\"Remember, {name}'s blood is on YOUR HANDS!\"
        """
        self.win = f"""
        ---------------
        |      
        |
        |      O
        |     \\|/
        |     / \\
        ^^^^^^^^^^^^^^^
\"{name} IS ALIVE , HOOOORAAAYYYYYYY!!!!!!!!!!!\"
        """

        self.hanglist = [self.base, self.hang1, self.hang2,
                         self.hang3, self.hang4, self.hang5]

    def __iter__(self):
        self.currenthang = 0
        return self

    def __next__(self):

        if self.currenthang < len(self.hanglist):
            x = self.hanglist[self.currenthang]
            self.currenthang += 1
            return x

        raise StopIteration

    def __str__(self) -> str:
        return self.hanglist[self.currenthang]


class Word():

    def __init__(self) -> None:
        self.word_list = ["absence", "abuse", "account", "accident", "beneath", "bend", "benefit", "biology", "bitter", "candidate", "campaign", "camera", "capacity", "capture", "deaf", "daughter", "deal", "decorate", "dialogue", "economy", "finance", "educate", "efficient",
                          "supportive", "elderly", "flight", "folk", "flame", "frustration", "garbage", "gather", "gentle", "global", "hilarious", "intelligence", "jazz", "knife", "longevity", "momument", "nonsense", "nobody", "turmeric", "utilize", "sashimi", "reconfigure", "wheat", "yellowish", "zone"]

    def random_word(self):
        return random.choice(self.word_list)

    def add_word(self, name):
        if name not in self.word_list:
            self.word_list.append(name)

    def show_words(self):
        print("\n---------------")
        for i, j in enumerate(self.word_list):
            print("{:>3}  |  {:<3}".format(i+1, j))
        print("---------------\n")


if __name__ == "__main__":
    game_on = True

    print("\n"*100)

    print("""
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝""")

    print("""\nWelcome to Hangman. A simple game for kids that teaches children that saying the wrong word can lead to someone's DEATH.
          
The rules for playing this game are pretty much non existent.
You will be given a word at random and only shown the number of letters it consists,
you need to guess all the letters in the word in 7 or less number of tries.
          """)

    hangname = input(
        "\nLet's start by entering a name for our hangman , to add a bit of \"emotional value\" : ").capitalize()

    while game_on:
        hangman = Figure(hangname)
        hangiter = iter(hangman)

        wordz = Word()
        chosen = wordz.random_word()

        blank = ["_"]*len(chosen)
        correct_messages = iter(["First correct guess!\n", "Second correct guess! ,keep going man\n", "Third correct guess! , you are killing it man\n",
                                 "Fourth correct guess! go go go\n", "Fift correct guess! , you are on fire\n", "Sixth correct guess! damn\n", "Seventh correct guess! when will this end?\n", "Eight correct guess! bruh how long is this word\n"])

        print(hangman.__next__())

        while "".join(blank) != chosen:

            print(
                f"Number of letters left to guessed = { blank.count('_') }")
            print("".join(blank))

            player_guess = input("\nPlayer enter your guess : ")

            if player_guess in chosen and player_guess != "":
                index_pos = [i for i, j in enumerate(
                    chosen) if player_guess == j]
                for i in index_pos:
                    blank[i] = list(chosen)[i]

                print(next(correct_messages))

            else:
                try:
                    print(hangiter.__next__())

                except StopIteration:
                    print(hangman.hang6)
                    print("-----GAME OVER-----")
                    print("The word was :", chosen)
                    break

        if "".join(blank) == chosen:

            print(hangman.win)

            print(
                f"You got the correct answer {chosen} in {hangiter.currenthang-1} wrong guesse(s).")

        cont = input("\nDo you want to play one more round? (y/n) : ")
        if cont != "y":
            break
        print("\n"*100)
