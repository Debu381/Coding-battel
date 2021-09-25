def check(n):
    number=1    #incrementing the values consitingly
    
    for i in range (1,n+1):     #loop for printing the values
        for j in range (1,i+1):
            
            print(number,end=" ")
            number=number+1
        print(end="\n")
if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        check(number)                                           # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")        