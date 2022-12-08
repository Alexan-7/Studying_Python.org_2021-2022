def count_list(par, par2 = False, count = 0): # параметр
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    
    else:
        for i in par:
            count += 1
        return count
        

j = [9, 8, 7, 6]

h, p = count_list(j, True) # print(count_list(j, True, -1)) # в скобках - аргумент (значение для параметра)

##h = ['a', 'b', 'g']
##
##print(count_list(h))
##
##k = [9, 8, 7, 6, 7, 8]
##
##print(count_list(k))
