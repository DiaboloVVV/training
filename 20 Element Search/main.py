def main():
    a = [1, 3, 5, 30, 42, 43, 500]
    userInput = int(input("Insert a number to check if it's in a list!\n"))
    # print(easyWay(userInput, a))
    print(find(userInput, a))


def easyWay(userInput, a):
    if userInput in a:
        return True
    else:
        return False


def find(element_to_find, ordered_list):
    start_index = 0
    end_index = len(ordered_list) - 1

    print(ordered_list, element_to_find)

    while True:
        middle_index = int((end_index + start_index) / 2) 

        # changed the following section
        if middle_index == start_index or middle_index == end_index:
            if ordered_list[middle_index] == element_to_find or ordered_list[end_index] == element_to_find:
                return True
            else:
                return False

        middle_element = ordered_list[middle_index]
        if middle_element == element_to_find:
            return True
        elif middle_element > element_to_find:
            end_index = middle_index
        else:
            start_index = middle_index


if __name__ == '__main__':
    main()
