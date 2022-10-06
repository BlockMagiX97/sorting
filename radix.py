def _make_same_lenght(list_val):
    max = 0
    for i in list_val:
        lenght = len(str(i))
        if lenght > max:
            max = lenght
    
    for i in range(len(list_val)):
        val = str(list_val[i])
        val = '0' * (max - len(val)) + val
        list_val[i] = val
    
    return (list_val, max)

def _make_prefix_sum(list_val):
    for i in range(len(list_val)):
        val = list_val[i]
        if i != len(list_val) - 1:
            list_val[i + 1] += val
    
    return list_val


def _radix(counter1, list_val, index):
    out = []
    for val in list_val:
        out.append(None)
        counter1[int(val[index])] += 1
    print(f"before counter: {counter1}, index: {index}")
    counter1 = _make_prefix_sum(counter1)
    print(f"afrer counter: {counter1},  index: {index}")
    count = -1
    while (len(list_val) + count) > -1:
        counter1[int(list_val[count][index])] -= 1
        out[counter1[int(list_val[count][index])]] = list_val[count]
        count -= 1
    
    return out

def ragix(list_val):
    # makes counter list
    counter = []
    for i in range(0, 10):
        counter.append(0)
    
    # getting ready
    value_touple = _make_same_lenght(list_val)
    list_val = value_touple[0]
    max = value_touple[1]
    

    for i in range(1, max + 1):
        i = max - i
        print(f"original: {list_val}")
        list_val = _radix(counter.copy(), list_val, i)
        print(f"unoriginal: {list_val}")
    
    for i in range(len(list_val)):
        list_val[i] = int(list_val[i])
    
    return list_val 
