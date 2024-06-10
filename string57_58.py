def fun(satr):

    l = satr.split(' ')
    new_l = []
    ans = ''
    for i in l:
        if i != '':
            ans += i
            ans += ' '

    return ans    

print(fun("Assalomu        alaykum        bo'lajak dasturchilar"))