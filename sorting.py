def make_same_lenght(list_val):
    max = 0
    for i in list_val:
        lenght = len(str(i))
        if lenght > max:
            max = lenght
    
    for i in enumerate(list_val):
        val = str(list_val[i])
        val = '0' * (max - len(val)) + val
        list_val[i] = val
    
    return list_val
        


def regix(list_val):
    # makes counter list
    counter = {}
    for key in range(0 , 10):
        counter[key] = 0
    

    


        
    