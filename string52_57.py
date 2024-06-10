def funk(satr):
    l = satr.split(' ')

    l_list = []
    ans = ''
    for i in l:
        l_list.append(i.capitalize())

    for i in l_list:
        ans += i
        ans += ' '

    return ans
    
print(funk("Assalomu alaykum bo'lajak dasturchilar!"))