import math
print('calculator scientific')

pilihan=input('masukan pilihan penggunaan angka = ')

if pilihan=='1':
    angka=float(input('masukan angka dalam (untuk trigonometri dalam derajat) = '))
elif pilihan=='2':
    angka1=float(input('masukan angka pertama = '))
    angka2=float(input('masukan angka kedua = '))
operator=input('masukan operator = ')

hasil=0

while True:
    if operator=='+':
        hasil=angka1+angka2
        print(f'{angka1} + {angka2} = {hasil}')
    elif operator=='-':
        hasil=angka1-angka2
        print(f'{angka1} - {angka2} = {hasil}')
    elif operator=='x':
        hasil=angka1*angka2
        print(f'{angka1} x {angka2} = {hasil}')
    elif operator=='/':
        if angka1==0 and angka2==0:
            print(f'{angka1} / {angka2} = tidak tentu')
        elif angka2==0:
            print(f'{angka1} / {angka2} = tidak terdefinisi')
        else:
            hasil=angka1/angka2
            print(f'{angka1} / {angka2} = {hasil}')
    elif operator=='^':
        hasil=angka1**angka2
        print(f'{angka1} ^ {angka2} = {hasil}')
    elif operator=='akar':
        hasil=math.sqrt(angka)
        print(f'akar {angka} = {hasil}')
    elif operator=='log':
        basis=int(input('masukan basis log = '))
        hasil=math.log(angka, basis)
        print(f'log({basis},{angka}) = {hasil}')
    elif operator=='trigono':
        trigono=input('masukan jenis trigonometri = ')
        if trigono=='sin':
            hasil=math.sin(math.radians(angka))
            print(f'sin({angka}) = {hasil}')
        elif trigono=='cos':
            hasil=math.cos(math.radians(angka))
            print(f'cos({angka}) = {hasil}')
        elif trigono=='tan':
            hasil=math.tan(math.radians(angka))
            print(f'tan({angka}) = {hasil}')
        else:
            print('jenis trigonometri tidak valid')
    
    elif operator=='arctrigono':
        trigono=input('masukan jenis trigonometri = ')
        if trigono=='sin':
            hasil=math.asin(angka)
            print(f'arcsin({angka}) = {hasil}')
        elif trigono=='cos':
            hasil=math.acos(angka)
            print(f'arccos({angka}) = {hasil}')
        elif trigono=='tan':
            hasil=math.atan(angka)
            print(f'arctan({angka}) = {hasil}')
        else:
            print('jenis arctrigonometri tidak valid')
    
    
    elif operator=='faktorial':
        hasil=math.factorial(int(angka))
        print(f'{int(angka)}! = {hasil}')
    
    
    
    
    