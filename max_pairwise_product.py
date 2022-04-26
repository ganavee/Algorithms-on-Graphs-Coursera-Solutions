def max_pairwise_product(numbers):
    max_prod = 0
    
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


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
