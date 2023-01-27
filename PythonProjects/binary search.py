#recursion binary search

'''def binary_search(number, counter):

    if number == 1:
        return counter + 1
    counter += 1
    return binary_search(number // 2, counter)
counter = 0
print(binary_search(int(input()), counter))'''

# binary search
def bin_sea(number, count):
    while number != 1:
        number //= 2
        count += 1
    return count + 1

count = 0
print(bin_sea(int(input()), count))