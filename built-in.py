def odd(numbers):
    if numbers==101:
        return "done"
    else:
        print(numbers)
        return odd(numbers+1)
    




print(odd(1))