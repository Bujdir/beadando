def convertToNewBase(sum,targetBase):
    num=''
    powers=[]
    for x in reversed(range(targetBase)):
        powers.append(2**x)
    for i,x in enumerate(powers):
        if sum-x>=0:
            num+='1'
            sum-=x
        else:
            num+='0'
    print(''.join(num))

num1=int(input("Add meg az első számot: "))
num2=int(input("Add meg a második számot: "))
sumofnums=num1+num2
tbase=int(input("Add meg a bázist: "))

print(convertToNewBase(sumofnums,tbase))