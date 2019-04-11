import random
import time

#function that plays the game
class Hangman():
    def Playing(self):
        print("")
        listOfWords = [""] #add words to the game here
        again = True
        while again:
            guessWord = random.choice(listOfWords)
            printWord = "*" * len(guessWord)
            alreadySaid = set()
            mistakes = 7
            print(" ".join(printWord))
            guessed = False
            while not guessed and mistakes > 0:
                guessPlayer = input("Guess a letter: ")
                if guessPlayer in guessWord:
                    alreadySaid.add(guessPlayer)
                    printWord = "".join([char if char in alreadySaid else "*" for char in guessWord])
                    if printWord == guessWord:
                        guessed = True
                else:
                    mistakes -= 1
                    print("Nice try! {0} mistakes left.".format(mistakes))
                print(" ".join(printWord))
            main()

#function that displays the menu
def menu():
      print("\n\n*********MENU*********")
      print("1. Play Hangman.")
      print("2. Exit"   )
      print("*********MENU*********")
      choice=input("\nEnter choice: ")
      return choice

def main():
    choice=menu()
    while choice!=4:
            if choice=='1':
                  Hangman().Playing()
            elif choice=='2':
                  print("Good Bye")
                  break
            else:
                  print("Incorrect input, returning to menu.")
                  main()
                  
main()


