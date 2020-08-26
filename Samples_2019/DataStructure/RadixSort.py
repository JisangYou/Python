# 기수 정렬
def radix(order):
    is_sorted = False
    position = 1

    while not is_sorted:
        is_sorted = True
        queue_list = [list() for _ in range(10)]
        # print("queue_list", queue_list)

        for num in order:
            # print("num",num)
            digit_number = (int)(num / position) % 10
            # print("digit_number", digit_number)
            queue_list[digit_number].append(num)
            print(" queue_list[digit_number]",  queue_list[digit_number])
            if is_sorted and digit_number > 0:
                is_sorted = False
        index = 0

        for numbers in queue_list:
            print(" numbers", numbers)
            for num in numbers:
                print(" num", num)
                order[index] = num
                index += 1

        position *= 10


x = [5, 2, 8, 6, 1, 9, 3, 7]
radix(x)
print(x)
