#touch typing exercise
import random

#checking the user input type 1
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
        

#checking the user inpout type 2
def check_ans2(ques, ans, tries):
    if ans == ques:
        print('well done')
        tries += 1
        return True, tries
    else:
        print('wrong ans')
        return False, tries


#exercise 4
def exercise_4():
    tries = 0
    while tries < 4:
        rand = random.randint(0, 4)
        if rand == 0:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'sad'
        elif rand == 1:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'dad'
        elif rand == 2:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'fad'
        elif rand == 3:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'dsf'
        print(ques)
        ans = input('').lower()
        correct, tries = check_ans2(ques, ans, tries)
    else:
        action = input('try again(a)/ quit(j): ').lower()
        if action == 'a':
            exercise_4()
        elif action == 'j':
            main_menu()
        else:
            print('invalid options')



#exercise 5
def exercise_5():
    tries = 0
    while tries < 4:
        rand = random.randint(0, 4)
        if rand == 0:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'jlk'
        elif rand == 1:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'l;k'
        elif rand == 2:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'k;j'
        elif rand == 3:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'j;l'
        print(ques)
        ans = input('').lower()
        correct, tries = check_ans2(ques, ans, tries)
    else:
        action = input('try again(a)/ quit(j): ').lower()
        if action == 'a':
            exercise_5()
        elif action == 'j':
            main_menu()
        else:
            print('invalid options')


#exercise 6
def exercise_6():
    tries = 0
    while tries < 4:
        rand = random.randint(0, 4)
        if rand == 0:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'ajskdlf;'
        elif rand == 1:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'jaksld;f'
        elif rand == 2:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'a;sldkfj'
        elif rand == 3:
            print('repeat the following letters (don\'t add space after the last letter)')
            ques = 'afj;sdkl'
        print(ques)
        ans = input('').lower()
        correct, tries = check_ans2(ques, ans, tries)
    else:
        action = input('try again(a)/ quit(j): ').lower()
        if action == 'a':
            exercise_6()
        elif action == 'j':
            main_menu()
        else:
            print('invalid options')

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
