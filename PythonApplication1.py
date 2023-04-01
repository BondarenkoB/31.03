def starts_with(lst, substr):
    new_lst = []
    for item in lst:
        if item.startswith(substr):
            new_lst.append(item)
    return new

