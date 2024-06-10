function smallNum(a, b, c) {
    if(a <= b && a <= c) {
        return a
    }else if(b <= a && b <= c) {
        return b
    }else {
        return c
    }
}

console.log(smallNum(7, 7, 7))