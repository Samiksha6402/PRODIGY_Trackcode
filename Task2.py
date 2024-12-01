#Guessing number
import random
class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass
print("GUESS THE NUMBER GAME!!!")
print("Guess the number between 1 and 100")
random_num=random.randint(1,100)
attempts = 0
while True:
    try:
        num=int(input("Enter the guessing number:"))
        attempts += 1
        if num<random_num:
            raise ValueTooSmallError
        elif num>random_num:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Value is too small,try again!!")
    except ValueTooLargeError:
        print("Value is too large,try again!!")
    except ValueError:
        print("Invalid input")
print("Congratulations!You guessed it correctly.")
print("Your total number of attempts are",attempts)



