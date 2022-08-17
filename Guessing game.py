
#Guessing game#

Secret_word = "cake"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("You are now playing a guessing game where you'll have to guess the word that has to do with a birthday party, you'll only have 3 chances to guess it ")
while guess != Secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guessing word: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOOSE!!")
else:
    print( "You got the word right, You WIN!")

