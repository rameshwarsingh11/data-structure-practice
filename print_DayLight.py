# Program to print integers from 1 to 100. Print 'Day' for multiple of 3 and 'Light' for multiple of 5.
# For integers a multiple of both 3 and five, you should print 'DayLight'. In other cases, print the integer itself.

def printDayLight():
    for num in range(0, 10):
        if num % 3 == 0 and num % 5 == 0:
            print('DayLight')
        elif num % 3 == 0:
            print('Day')
        elif num % 5 == 0:
            print('Light')

if __name__ == '__main__':
    printDayLight()

