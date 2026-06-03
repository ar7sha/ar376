import operator as o

import math
def hasher(ipath,opath,f1=4,f2=5,salt=1):
    def readbit():
        with open(ipath,"rb") as f:
            while True:
                a = f.read(106)
                if not a:
                    break
                if 106 > len(a):
                    repeat = (106 + len(a) - 1) // len(a)
                    a = (a * repeat)[:106]
                k = a[math.ceil((a.find(a[0]) + a.rfind(a[-1])) / 2)]
                for j in a:
                    yield j , a[0] , a[-1] , a[-2] , k
    line = readbit()
    fixed_size = pow(2,376)-1
    global inheritance
    inheritance = 2
    global magic_number
    magic_number = 163378
    def liner():
        for y in line:
            key = y[1] + 2
            i = o.xor(y[0], salt)
            ar_xor = o.xor(i , key)
            ar_or = o.or_(key,i)
            ar_and = o.and_(i,key)
            ar_nand = ~(o.and_(key,i)) & 0xFF
            ar_nor = ~(o.or_(key,i)) & 0xFF
            ar_xnor = ~(ar_xor) & 0xFF    
            global inheritance
            key2 = y[2] + inheritance + y[3] + 2
            fog = pow(key2,25)
            and1 = ar_and + ar_nand + ar_nor + ar_xnor
            and2 = ar_and + ar_nand + ar_xor + ar_or
            and3 = ar_and + ar_nand + ar_xor + ar_or + ~(key) & 0xFF
            and4 = ar_and + ar_or + ar_xnor
            ands = and1 + and2 + and3 + and4 
            fand = pow(ands * 7, fog, 101)
            or1 = ar_or + ar_nand + ar_nor + ar_xnor
            f_or = pow(or1*7,fog,101)
            xor1 = ar_xor + ar_nand + ar_nor + ar_xnor 
            xor2 = ar_xor + ar_xnor + ar_and + ar_or
            fxor = pow((xor1+xor2)*7, key2,101)
            nand1 = ar_nand + ar_xnor + ar_and + ar_or
            fnand = pow(nand1,key2)
            nor1 = ar_nor + ar_or + ar_xor + ar_nand
            nor2 = ar_nor + ar_or + ar_xor + ar_nand + ~(key2) & 0xFF
            nor3 = ar_nor + ar_and + ar_or + ar_xnor
            fnor = pow(nor1 + nor2 + nor3 * 7, fog , 101)
            xnor1 = ar_xnor + ar_xor + ar_nand + ar_or
            xnor2 = ar_xnor + ar_xor + ar_nand + ar_or + ~(key2) & 0xFF
            fxnor = pow(xnor1 + xnor2 * 7 , fog,101)
            key3 = y[4] + 2 
            f1 = pow(fand + fxnor, magic_number ,1000000000001)
            f2 = pow(f_or + fnor,magic_number,1000000000007)
            f3 = (((fxor + fnand)//2)*key3) + inheritance 
            res = pow(f1,f2 ,f3)
            inheritance = o.xor(ar_and,ar_or) + o.xor(ar_nor,ar_nand) + o.and_(ar_xor, ar_xnor) + inheritance
            yield res       
    def mk_hazy(res,fog,magic_number,for1,for2):
        r = None
        for i in range(for1):
            r = pow(res,fog,magic_number)
        for i in range(for2):
            r = pow(res,magic_number,fog)
        if r < 100 :
            r = (r + 2 ) * magic_number
        slipt_point = len(f'{r}') // 2
        r1 = f'{r}'[:slipt_point]
        r2 = f'{r}'[slipt_point:]
        ambiguous = pow(int(r1),int(r2))
        vague = pow(ambiguous,1,magic_number)
        return vague
    def mk376(res:int,fog:int):
        r = 0
        while True :
            if r.bit_length() == 376 :
                break
            r = pow(res,fog , fixed_size)
        return r
    def mix():
        stop = 'go'
        ihave_runoutof_names = []
        while stop != 'stop':
            if len(ihave_runoutof_names) >=2 :
                ihave_runoutof_names = [mk_hazy(ihave_runoutof_names[0]+ihave_runoutof_names[1],314159,fixed_size,f1,f2)]
            try:
                res = next(liner())
            except StopIteration :
                stop = 'stop'
                break
            value = mk_hazy(res,314159,magic_number,f1,f2)
            ihave_runoutof_names.append(value)
        return ihave_runoutof_names
    with open(opath,"ab") as rfile :
        t:int  = mix()[0]
        rr = 0
        if t.bit_length() != 376 :
            rr = mk376(t,314159)
        rfile.write(f'{hex(rr)[2:]}'.encode())
                


hasher("test.txt","ar.ar376")
