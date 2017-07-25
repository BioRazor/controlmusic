import functions


def numerate_list(list):
    for i in range(len(list)):
        list[i] = str(int(i+1)) + ' ' + list[i]
    return list

