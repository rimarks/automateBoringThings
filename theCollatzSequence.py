def collatz(number):
    if number % 2== 0:
        
        print(str(number //2 ))
        return (number//2)
    elif number % 2 == 1:
        print(str(3*number+1))
        return (3*number+1)

print('Enter number (that is not 1):')
temp = input()
fun = int(temp)

while fun != 1:
    fun = collatz(fun)
