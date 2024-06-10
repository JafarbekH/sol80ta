def EngQisqa(satr):

    l = satr.split(' ')
    l_num = []
    for i in l:
        l_num.append(len(i))
    min_num = min(l_num)
    
    for i in l:
        if len(i) == min_num:

            return f'{i} {min_num}'

print(EngQisqa("Assalomu alaykum aziz do'stlar"))