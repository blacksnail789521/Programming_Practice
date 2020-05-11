import numpy as np

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return -1 if np.sqrt(sq) != int(np.sqrt(sq)) else (np.sqrt(sq) + 1) ** 2


def test():
    
    # input = 121 # 144
    # input = 625 # 676
    input = 114 # -1
    output = find_next_square(input)
    
    return output

if __name__ == "__main__":
    
    output = test()