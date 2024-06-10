function kabisa_or_no(year) {
    if (year % 4 === 0 && year % 100 !== 0 || year % 400 === 0) {
        return 366
    }else {
        return 365
    }
}

console.log(kabisa_or_no(2020))

