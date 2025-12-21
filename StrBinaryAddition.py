def addBinary(self, a: str, b: str) -> str:
    
    revnum_a = a[::-1]
    a_int = 0
    for i in range(0, len(revnum_a)):
        if revnum_a[i] == '1':
            a_int += 2**(i)
    revnum_b = b[::-1]

    b_int = 0
    for i in range(0, len(revnum_b)):
        if revnum_b[i] == '1':
            b_int += 2**(i)
    res_dec_int = a_int + b_int

    if res_dec_int == 0:
        return "0"
    
    res_bin = ""
    while res_dec_int > 0:
        res = int(res_dec_int % 2)
        res_bin += str(res)
        res_dec_int //= 2
    return res_bin[::-1]