#touch typing exercise
import random

#exercise 1
def exercise_1():
    print('repeat the following letters (don\'t add space after the last letter)')
    ans = input('a s d f j k l ; \n').lower()
    if ans == 'a s d f j k l ;':
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
        print('oops!! wrong answer!!')
        quit = input('do you want to quit? (y/n)').lower()
        if quit == 'y':
            main_menu()
        elif quit == 'n':
            exercise_1()
        else:
            print("wrong ans, try 'y' or 'n': ")

#exercise 2
def exercise_2():
    print('repeat the following letters (don\'t add space after the last letter)')
    ans = input('a d s f j l k ; \n').lower()
    if ans == 'a d s f j l k ;':
        print('well done!!')
        while True:
            action = input('try again(a)/ quit(j): ')
            if action == 'a':
                exercise_2()
            elif action == 'j':
                main_menu()
            else:
                print('invalid options')
                continue
    else:
        print('oops!! wrong answer!!')
        quit = input('do you want to quit? (y/n)').lower()
        if quit == 'y':
            main_menu()
        elif quit == 'n':
            exercise_2()
        else:
            print("wrong ans, try 'y' or 'n': ")

#exercise 3
def exercise_3():
    print('repeat the following letters (don\'t add space after the last letter)')
    ans = input('a f s d j ; k l \n').lower()
    if ans == 'a f s d j ; k l':
        print('well done!!')
        while True:
            action = input('try again(a)/ quit(j): ')
            if action == 'a':
                exercise_3()
            elif action == 'j':
                main_menu()
            else:
                print('invalid options')
                continue
    else:
        print('oops!! wrong answer!!')
        quit = input('do you want to quit? (y/n)').lower()
        if quit == 'y':
            main_menu()
        elif quit == 'n':
            exercise_3()
        else:
            print("wrong ans, try 'y' or 'n': ")
        
#exercise 4
def exercise_4():
    tries = 0
    while True:
        rand = random.randint(0, 5)
        if tries < 4:
            if rand == 0:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('sad\n')
                if ans == 'sad':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 1:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('dad\n')
                if ans == 'dad':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 2:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('fad\n')
                if ans == 'fad':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 3:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('dsf\n')
                if ans == 'dsf':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
        else:
            action = input('try again(a)/ quit(j): ')
            if action == 'a':
                exercise_4()
            elif action == 'j':
                main_menu()
            else:
                print('invalid options')
                continue


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
    elif mode == '3':
        exercise_3()
    elif mode == '4':
        exercise_4()
    else:
        print('invalid !!')


#game launches
main_menu()
