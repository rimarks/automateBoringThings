def collatz(number):
    if number % 2== 0: #tests whether the number is even or not.
        
        print(str(number //2 )) #Divides the even number by 2, output is an integer.
        return (number//2) #outputs number to fun
    elif number % 2 == 1: #else if the number is odd then:
        print(str(3*number+1)) # 3xnumber + 1
        return (3*number+1)

print('Enter number (that is not 1):')
temp = input() #prompts user for input
fun = int(temp) #converts input into integer

while fun != 1: #runs a while loop fun is not equal to 1
    fun = collatz(fun) # keeps running collatz function until it works
