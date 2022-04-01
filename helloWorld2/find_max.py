def find_max(alist):
    # search for the biggest number
    big_num = alist[0]
    for i in range(0, len(alist)):
        if alist[i] > big_num:
            big_num = alist[i]

    print('the biggest number in the list is...')
    return big_num
