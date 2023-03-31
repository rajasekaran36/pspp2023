def fibonacci(no_of_terms):
    prev_1 = -1
    prev_2 = 1
    n = 0
    while n<=no_of_terms:
        current = prev_1 + prev_2
        print(current)
        n += 1
        prev_1 = prev_2
        prev_2 = current