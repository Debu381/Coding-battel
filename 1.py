def pattern(number):                                      
    for i in range(1, number+1):                                # for upper half 
        print('*'.join(str(i*(str(i)))))
    for j in range(number,0,-1):                               # for lower half
        print('*'.join(str(j*(str(j)))))

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