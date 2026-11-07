import math
print('calculator scientific')

angka1=float(input('masukan angka pertama = '))
angka2=float(input('masukan angka kedua = '))
operator=input('masukan operator = ')

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
    hasil=math.sqrt(angka1)
    print(f'akar {angka1} = {hasil}')
elif operator=='log':
    basis=int(input('masukan basis log = '))
    hasil=math.log(angka1, basis)
    print(f'log({basis},{angka1}) = {hasil}')



