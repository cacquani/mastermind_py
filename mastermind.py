import random

print('Create secret code!')

colours = [ 'R', 'Y', 'G', 'B', 'K', 'W' ]

def create_code():
    return random.choices(colours, k=4)

def calculate_score(code, guess):
    correct = 0
    included = 0
    indexes = []
    for index, element in enumerate(guess):
        if code[index] == element:
            correct = correct + 1
            indexes.append(index)

    indexes.reverse()
    for index in indexes:
        code.pop(index)
        guess.pop(index)

    for element in guess:
        try:
            index = code.index(element)
            code.pop(index)
            included = included + 1
        except ValueError:
            print

    return [correct, included]



# code = ['G', 'W', 'B', 'K']
code = create_code()
print('Code:  ', code)

# guess = ['K', 'K', 'W', 'B']
# guess = create_code()
print("Enter four colours separated by spaces. Possible colours are: R, Y, G, B, K, W:")
guess_string = ''
while 1:
    guess_string = input('> ')

    if guess_string == 'exit':
        break

    guess = guess_string.split()

    print('Guess: ', guess)
    score = calculate_score(code.copy(), guess)

    if score[0] == 4:
        print('You won!')
        break
    else:
        print('Correct pegs:                 ', score[0])
        print('Right colour, wrong position: ', score[1])
        print
