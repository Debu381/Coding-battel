def pattern(number):
    for i in range(1,number+2):               # for upper half
        print('* ', end="")                   # first vertical line of *
        for j in range(1,i):                  # asc order of numbers
            print(j, end=' ')
        for k in range((i-2),0,-1):            # desc order of numbers
            print(k, end=' ')
        if i != 1:                             # * at end of line
            print('*', end='')                 
        print()
    for i in range(number+1, 1, -1):           # for lower half 
        print('* ', end="")                     # first vertical line of *
        for j in range(1,i-1):                 # asc order of numbers
            print(j, end=' ')
        for k in range((i-3),0,-1):             # desc order of numbers
            print(k, end=' ')
        if i != 2:
            print('*', end='')                  # * at end of line
        print()

if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        pattern(number)                                           # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")