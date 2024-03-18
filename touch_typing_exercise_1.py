#touch typing exercise

#exercise 1
def exercise_1():
    print('repeat the following letters (don\'t add space after the last letter)')
    lett = input('a s d f j k l ; \n').lower()
    if lett == 'a s d f j k l ;':
        print('well done!!')
        while True:
            action = input('try again(a)/ quit(j): ')
            if action == 'a':
                exercise_1()
            elif action == 'j':
                main_menu()
            else:
                print('invalid options')
                continue
    else:
        print('try again!!')
        exercise_1()

#exercise 2
def exercise_2():
    print('repeat the following letters (don\'t add space after the last letter)')
    lett = input('a d s f j l k ; \n').lower()
    if lett == 'a d s f j l k ;':
        print('well done!!')
        while True:
            action = input('try again(a)/ quit(j): ')
            if action == 'a':
                exercise_1()
            elif action == 'j':
                main_menu()
            else:
                print('invalid options')
                continue
    else:
        print('try again!!')
        exercise_2()
    


#main menu
def main_menu():
    print('what exercise do yu want to want to practise? (q to quit)')
    mode = input('1.\n2.\n3.\n4.\n: ')
    if mode == 'q' :
        exit()
    elif mode == '1':
        exercise_1()
    elif mode == '2':
        exercise_2()
    else:
        print('invalid !!')


#game launches
main_menu()
