def remove_right(input_list, element):
    try:
        index_element = input_list.index(element)
    except:
        print("element not found in list")
        return input_list
    if index_element != len(input_list) - 1:
        input_list.pop(index_element + 1)
    else:
        print("ELement is the last on in the list")
    return input_list


list_popped = remove_right([1, 2, 3, 4], 2)
print(list_popped)