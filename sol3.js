function sol3(x,y) {
    if (x < y) {
        a = (x + y) / 2
        b = 2 * (x * y)
        return a + ' ' + b
    } else if (x > y) {
        a = 2 * (x * y)
        b = (x + y) / 2
        return a + ' ' + b
    } else {
        return x + ' ' + y
    }
}

console.log(sol3(8,8))