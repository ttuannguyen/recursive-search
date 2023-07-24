def search(input_list, target):
    # print(input_list[1::-1])

    # base case: 
    if not input_list:
        return False
    elif input_list[0] == target:
        return True
    
    # recursive case:
    search(input_list[1::-1], target)


# currently getting stackoverflow
print(search([1, 2, 3], 2))