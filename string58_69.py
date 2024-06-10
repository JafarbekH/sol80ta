def ank(satr):
    
    l = satr.split("\\")

    return l[-1].split('.')[0]

print(ank("D:\java.exe"))