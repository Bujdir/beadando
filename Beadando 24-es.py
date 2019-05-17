def konvtizre(num,bazis):
    hossz=len(str(num))
    tsz=0
    for i in range(hossz):
        sz=str(num)
        tsz+=int(num[i])*bazis**(hossz-1)
        hossz-=1
    return tsz
def vissza(num,bazis):
    index=num**0
    hatvanye=0
    while num>=findex:
        index*=bazis
        hatvanye+=1
    index/=bazis
    megoldas=""
    for i in range(hatvanyertek):
        helyiertek=0
        while index<=num:
            num-=index
            helyiertek+=1
        megoldas+=str(helyiertek)
        index/=bazis
    return megoldas
def feladat(num1,num2,bazis):
    number1=tizesse(num1,bazis)
    number2=tizesse(num2,bazis)
    sum=tsz1+tsz2
    eredmeny=vissza(sum,bazis)
    return eredmeny
print("eredmeny:",feladat(125,149,2))
