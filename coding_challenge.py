sqaures = []
def is_odd():
    for i in range(100):
        sqaures.append(i**2)
    odd_numbers = [num for num in sqaures if num % 2 != 0]
    total_sum = sum(sqaures)
    print(total_sum)
is_odd()




