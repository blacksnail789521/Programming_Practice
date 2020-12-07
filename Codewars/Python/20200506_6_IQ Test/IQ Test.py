def iq_test(numbers):

    numbers = [ int(number) for number in numbers.split(" ") ]
    
    if len(numbers) <= 2:
        return 1
    
    even_index_list, odd_index_list = [], []
    for index, number in enumerate(numbers):
        if number % 2 == 0:
            even_index_list.append(index + 1)
        else:
            odd_index_list.append(index + 1)
        
        if len(even_index_list) == 1 and len(odd_index_list) > 1:
            return even_index_list[0]
        elif len(odd_index_list) == 1 and len(even_index_list) > 1:
            return odd_index_list[0]


def test():
    
    # input = "2 4 7 8 10" # 3
    input = "1 2 1 1" # 2
    output = iq_test(input)
    
    return output

if __name__ == "__main__":
    
    output = test()