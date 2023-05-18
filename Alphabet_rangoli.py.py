def print_rangoli(size):
    # your code goes here
    alphbets = "abcdefghijklmnopqrstuvwxyz"
    # get char from alphabets, "-char-", next this in center and fill
    total_size = ((4*size)-3)
    for i in range(1, size+1):
        # Form alphabets
        alpha_string = ""
        for j in range(i):
            letter = alphbets[size-i+j]
            alpha_string = alpha_string.center((2*j+1), letter)
        alpha_string_hiphen = "-".join(alpha_string)
        print(alpha_string_hiphen.center(total_size, "-"))                 
    for i in range(size-1, 0, -1):        
        alpha_string = ""
        for j in range(i):                
            letter = alphbets[size-i+j]
            alpha_string = alpha_string.center((2*j+1), letter)
        alpha_string_hiphen = "-".join(alpha_string)
        print(alpha_string_hiphen.center(total_size, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)