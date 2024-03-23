#touch typing exercise
import random

#checking the user input
def check_ans(ques, ans, func):
    if ans == ques:
        print('well done!!')
        while True:
            action = input('try again(a)/ quit(j): ')
            if action == 'a':
                func()
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
            func()
        else:
            print("wrong ans, try 'y' or 'n': ")


#exercise 1
def exercise_1():
    print('repeat the following letters (don\'t add space after the last letter)')
    ques = 'a s d f j k l ;'
    ans = input('a s d f j k l ; \n').lower()
    check_ans(ques, ans, exercise_1)

#exercise 2
def exercise_2():
    print('repeat the following letters (don\'t add space after the last letter)')
    ques = 'a d s f j l k ;'
    ans = input('a d s f j l k ;\n').lower()
    check_ans(ques, ans, exercise_2)

#exercise 3
def exercise_3():
    print('repeat the following letters (don\'t add space after the last letter)')
    ques = 'a f s d j ; k l'
    ans = input('a f s d j ; k l\n').lower()
    check_ans(ques, ans, exercise_3)
        
#exercise 4
def exercise_4():
    tries = 0
    while True:
        rand = random.randint(0, 5)
        if tries < 4:
            if rand == 0:
                print('repeat the following letters (don\'t add space after the last letter)')
                ques = 'sad'
                ans = input('sad\n').lower
                if ans == 'sad':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 1:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('dad\n').lower
                if ans == 'dad':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 2:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('fad\n').lower
                if ans == 'fad':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 3:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('dsf\n').lower
                if ans == 'dsf':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
        else:
            action = input('try again(a)/ quit(j): ').lower
            if action == 'a':
                exercise_4()
            elif action == 'j':
                main_menu()
            else:
                print('invalid options')
                continue


#exercise 5
def exercise_5():
    tries = 0
    while True:
        rand = random.randint(0, 5)
        if tries < 4:
            if rand == 0:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('jlk\n').lower
                if ans == 'jlk':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 1:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('l;k\n').lower
                if ans == 'l;k':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 2:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('k;j\n').lower
                if ans == 'k;j':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 3:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('j;l\n').lower
                if ans == 'j;l':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
        else:
            action = input('try again(a)/ quit(j): ').lower
            if action == 'a':
                exercise_5()
            elif action == 'j':
                main_menu()
            else:
                print('invalid options')
                continue


#exercise 6
def exercise_6():
    tries = 0
    while True:
        rand = random.randint(0, 5)
        if tries < 4:
            if rand == 0:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('ajskdlf;\n').lower
                if ans == 'ajskdlf;':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 1:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('jaksld;f\n').lower
                if ans == 'jaksld;f':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 2:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('a;sldkfj\n').lower
                if ans == 'a;sldkfj':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
            elif rand == 3:
                print('repeat the following letters (don\'t add space after the last letter)')
                ans = input('afj;sdkl\n').lower
                if ans == 'afj;sdkl':
                    print('well done')
                    tries += 1
                    continue
                else:
                    print('wrong ans')
                    continue
        else:
            action = input('try again(a)/ quit(j): ').lower
            if action == 'a':
                exercise_6()
            elif action == 'j':
                main_menu()
            else:
                print('invalid options')
                continue

#main menu
def main_menu():
    print('what exercise do yu want to want to practise? (q to quit)')
    mode = input('1.\n2.\n3.\n4.\n5.\n6.\n: ')
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
    elif mode == '5':
        exercise_5()
    elif mode == '6':
        exercise_6()
    else:
        print('invalid !!')


#game launches
main_menu()
