#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(arg1, arg2, nrange):
    count = 0
    for i in range(nrange):
        if (i % arg1) == 0  or ( i % arg2) == 0:
            count = count + i
    return(count)
    


multi1 = int(3)
multi2 = 5
numberrange = 1000

summ = multiples(multi1, multi2, numberrange)

print("The sum is: ", summ)



