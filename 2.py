def pattern(number):
    li = list()                                     # to store of lists
    num=1                                           # to initiate
    for i in range(1, number+1):                    
        x = list()                                  # to create a temporary list
        for j in range(1 , i+1):
            x.append(str(num))                      # append string form of number in list for join function
            num += 1                                # number increment
        li.append(x)                                # append temporary lists in main list
    for i in li:
        print('*'.join(i))                          # for upper half
    for i in reversed(li):
        print('*'.join(i))                          # for lower half

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