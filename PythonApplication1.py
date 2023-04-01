def common_elements(list1, list2):
    common = []
    for element in list1:
        if element in list2 and element not in common:
            common.append(element)
    return common
