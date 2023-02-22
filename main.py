def array_sum(array):
    print(sum(array))


def array_mult(array):
    mult = 1
    y = 1
    y = len(array)
    for y in array:
        mult = mult * y
    print(mult) #ae


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lst = []
    num = int(input("How many numbers: "))
    for i in range(0, num):
        ele = int(input())

        lst.append(ele)

    array_sum(lst)

    array_mult(lst)

