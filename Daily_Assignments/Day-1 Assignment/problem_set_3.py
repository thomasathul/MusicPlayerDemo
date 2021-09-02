def odd_man(list1):
    list1.sort()
    if list1[0] != list1[1]:
        return list1[0]
    return list1[-1]


def close_mean(list1):
    mean = sum(list1)//len(list1)
    list1.append(mean)
    list1.sort()
    indexnum = list1.index(mean)
    if abs(list1[indexnum]-list1[indexnum-1]) > abs(list1[indexnum]-list1[indexnum+1]):
        return list1[indexnum+1]
    return list1[indexnum-1]


def average_speed(list1, timeint):
    return sum(list1)//(len(list1)*timeint)


def missing_number(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    return set1.difference(set2)


def diff_low_num(list1):
    set1 = set(list1)
    unique_list = list(set1)
    unique_list.sort()
    diff = unique_list[1]-unique_list[0]
    return diff


def small_than_mean(list1):
    mean = sum(list1)//len(list1)
    list1.append(mean)
    list1.sort()
    index_num = list1.index(mean)
    return index_num
