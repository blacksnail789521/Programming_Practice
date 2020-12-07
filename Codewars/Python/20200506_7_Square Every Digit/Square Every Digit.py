def square_digits(num):
    result = ""
    for digit in str(num):
        result += str(pow(int(digit), 2))
    
    return int(result)


def test():
    
    input = 9119
    output = square_digits(input)
    
    return output

if __name__ == "__main__":
    
    output = test()