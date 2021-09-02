def ipadd(string):
    list1 = list(string.split("."))
    decimal = 0
    i = 3
    for num in list1:
        decimal += (int(num)*pow(256, i))
        i -= 1
    return decimal


def isogram(string):
    set1 = set(string)
    list1 = list(string)
    return "It is an isogram" if len(set1) == len(list1) else "It is not an isogram"


def mexican_wave(string):
    new = []
    for i in range(len(string)):
        new.append("{0}{1}{2}".format(
            string[:i], string[i].upper(), string[i+1:]))
    return new


def large_num(string):
    num = int(string)
    res = 0
    i = 1
    while num//i > 0:
        temp = (num // (i * 10)) * i + (num % i)
        i *= 10
        if temp > res:
            res = temp
    return res


def shuffle(string):
    list1 = list(string)
    list1.sort(reverse=True)
    return "".join(x for x in list1)


def word_freq(string):
    return string.count('a')


def rgb_hex(tup):
    R, G, B = tup
    return "0x{:02x}{:02x}{:02x}".format(R, G, B)


def accumulate(string):
    temp = ""
    for i in range(1, len(string)+1):
        temp += string[i-1]*i
        if i != len(string):
            temp += '-'
    return temp
