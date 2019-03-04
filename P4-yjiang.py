
def compare(guess,num):
    if guess == num: 
        return 0
    elif 20 >= guess > num:
        return -1
    elif 1 <= guess < num: 
        return 1


name=input ('Hello! What is your name?')
print('Well,',name,',I am thinking of a number between 1 and 20')
import random
num = random.randint(1,20)
i=1

try:
    while True:
        guess = int(input('Take a guess:'))

        if guess<1 or guess>20:
            print('please input a number bewteen 1 and 20!')
        elif compare(guess,num)==0:
            print('Good job, ',name,'! You guessed my number in ',i,' guesses!')
            break
        elif compare(guess,num)==-1:
            print('Your guess is too high.')
        else : print('Your guess is too low.')
        i+=1
        if i==7:
           print('\nSorry you hadn’t found the number in 6 tries')
           print('The number I was thinking of was',num)
           break 
except:
    print('please input a number!')