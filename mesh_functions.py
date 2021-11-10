from random import randint


def create_new_mesh():

    temp = {}
    for i in range(0, 16):
        temp[i] = 0

    temp[0] = 2
    temp[4] = 2
    return temp

def render(input):
    
    k = 0
    while k < 16:
        n = 0
        while n < 4:
            print(f"|%d|" %(input[n + k]), end = '  ')
            n += 1
        print('')
        k += 4


def zeroes_locator(input):
    
    n = 0
    list = []
    while n <= 15:

        if input[n] == 0:
            list.append(n)

        n += 1
    return list

def random_place_gen(input):
    if len(input) > 0:
        place_gen = randint(0, len(input) - 1)
        return input[place_gen]

    else:
        return -1

def score(input):
    i = 0
    temp_score = 0

    while i < 16:
        temp_score += input[i]
        i += 1
    return temp_score

def refresh(input):

    txt = open('high_score.txt', 'r')
    high_score = txt.read()

    list = zeroes_locator(input)
    random_loc = random_place_gen(list)
    current_score = score(input)
    
    if random_loc != -1:
        input[random_place_gen(list)] = 2

    if current_score > float(high_score):
        txt.close()
        txt = open('high_score.txt', 'w')
        txt.write(str(current_score))
        txt.close()
        txt = open('high_score.txt', 'r')
        high_score = txt.read()
    print(f'\n___________________________________________________ Current Score : %d |||| High Score : %s' %(current_score, high_score))
    render(input)
    txt.close()
