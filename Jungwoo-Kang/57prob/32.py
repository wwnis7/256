# Let's play Guess the Number.
# Pick a difficulty level (1, 2, or 3): 1
# I have my number. What's your guess? 1
# Too low. Guess again: 5
# Too high. Guess again: 2
# You got it in 3 guesses!
# Play again? n
# Goodbye!

print('Let\' play Guess the Nubmer.')
diff = input('Pick a difficulty level (1, 2, or 3): ')
if diff == '1':
    n = 10
elif diff == '2':
    n = 100
elif diff == '3':
    n = 1000
else:
    print('you enter the wrong number.')
#########random으로 correct잡는법

# correct=np.random(1,n+1,1)

again='y'
correct = 3

while again == 'y':
    count=0
    guess = input('I have my number. What\'s your guess?: ')
    while True:
        count += 1
        if int(guess) < correct:
            guess = input('Too low. Guess again: ')
        elif int(guess) > correct:
            guess = input('Too high. Guess again: ')
        elif int(guess) == correct:
            print(f'You got it in {count} guesses!')
            again = input('Play again?')
            if again == 'y':
                break
            elif again == 'n':
                print('Goodbye!')
                break

