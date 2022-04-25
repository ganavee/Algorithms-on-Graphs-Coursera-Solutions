def max_pairwise_product(numbers):
    max_prod = 0
    for i in range(len(numbers)-1):
        for j in range(1, len(numbers)):
            prod = numbers[i]*numbers[j]
            if(prod > max_prod):
                max_prod = prod
    return max_prod


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
