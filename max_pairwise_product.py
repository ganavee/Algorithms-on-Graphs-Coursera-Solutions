import random
def max_pairwise_product_fast(numbers):
    
    
    #METHOD 1
    #construct max heap
    #get first two elements
    #multiply them and return the result

    #METHOD 2
    #sort the elements
    #mutilply the first two elements and return the result

    #METHOD 3
    #maintaint the first 2 max elements
    #mutilply the result and return
    if(numbers[0] > numbers[1]):
        first_max = numbers[0]
        second_max = numbers[1]
    else:
        first_max = numbers[1]
        second_max = numbers[0]
    for i in range(2, len(numbers)):
        if(numbers[i] > first_max):
            second_max =  first_max
            first_max = numbers[i]
        elif(numbers[i] > second_max):
            second_max = numbers[i]
    #print("first_max {0} second_max {1} ".format(first_max, second_max))
    return(first_max * second_max)


def max_pairwise_product(numbers):
    #METHOD 4
    #Naive Solution
    length = len(numbers)
    max_prod = 0
    for i in range(0, length-1):
        for j in range(i+1, length):
            if(numbers[i]*numbers[j] > max_prod):
                max_prod = numbers[i]*numbers[j]
    return max_prod


if __name__ == '__main__':
    while(True):
        input_n = random.random()
        input_n = int(input_n * 10) + 2
        input_numbers = [random.randint(2, 10000) for i in range(input_n)]
        print("n = {0} input_numbers {1}".format(input_n, input_numbers))
        #input_numbers = [int(x) for x in input().split()]
        fast = max_pairwise_product_fast(input_numbers)
        slow = max_pairwise_product(input_numbers)
        if(fast != slow):
            print("Fast {0} Slow {1}".format(fast, slow))
            break
        print()
        
