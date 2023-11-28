import random
number = random.randint(1, 10)

number_of_time = 3
i = 0

while i < number_of_time:
    guess_number = int(input('Guess a number: '))
    i += 1
    if guess_number > number:
        print('your guessed number is greater than number')
    elif guess_number < number:
        print('your guessed number is less than number')
    elif guess_number == number:
        print('You won!')
        break
    else:
        print('invalid number')
else:
    print('you loss!')