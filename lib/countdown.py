# your code goes here!
import time

def countdown(n):
    while n:
        print(f'{n} SECOND(S)!')
        n -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(n):
    while n:
        print(f'{n} SECOND(S)!')
        n -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')