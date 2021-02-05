'''import os
anm=[]
amount=[0,0,0,0,0]
price=[15,25,75,5,2]
print('\tโปรแกรมร้านค้าออนไลน์\n','-'*36)
def menu():
    global choice
    print('1. แสดงรายการสินค้า\n2. หยิบสินค้าเข้าตะกร้า\n3. แสดงรายจำนวนและราคาที่หยิบ\n4. หยิบสินค้าออกจากตะกร้า\n5. ปิดโปรแกรม\n')
    choice = input('กรุณาเลือกทำรายการ : ')

def one():
    print('\tรายการสินค้า\n','-'*36,'\n','\t1. หมา ราคา 15 บาท\n\t2. แมว ราคา 25 บาท\n\t3. หมีแพนด้า ราคา 75 บาท\n\t4. งู ราคา 5 บาท\n\t5. หมู ราคา 2 บาท')

def two():
    animal = 0
    while(True):
        print('\t1. หมา\n\t2. แมว\n\t3. หมีแพนด้า\n\t4. งู\n\t5. หมู\n\t6. ออกจากฟังก์ชัน')
        animal = input('เลือกหยิบสินค้าหมายเลข : ')
        try:
            if int(animal)==1 or animal=='1':
                anm.append('หมา')
            elif int(animal)==2 or animal=='2':
                anm.append('แมว')
            elif int(animal)==3 or animal=='3':
                anm.append('หมีแพนด้า')
            elif int(animal)==4 or animal=='4':
                anm.append('งู')
            elif int(animal)==5 or animal=='5':
                anm.append('หมู')
            elif int(animal)==6 or animal=='6':
                break
            else:
                print('กรุณากรอกหมายเลขให้ถูกต้อง')
        except:
            print('กรุณากรอกหมายเลขให้ถูกต้อง')
            pass
def three():
    for i in anm:
        if i == 'หมา':
            amount[0]+=1
        elif i == 'แมว':
            amount[1]+=1
        elif i == 'หมีแพนด้า':
            amount[2]+=1
        elif i == 'งู':
            amount[3]+=1
        elif i == 'หมู':
            amount[4]+=1
    amounttt=amount[0]+amount[1]+amount[2]+amount[3]+amount[4]
    pricett=amount[0]*15+amount[1]*25+amount[2]*75+amount[3]*5+amount[4]*2
    print('')
    print('{0:_<10}{1}{0:_<10}'.format('','สินค้าที่คุณหยิบไปมีดังนี้'))
    print('{0:.<6}{1}{0:.<6}{2}{0:.<6}{3}{0:.<7}'.format('','สินค้า','จำนวน','ราคา'))
    print('{0:_<38}'.format(''))
    if amount[0]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:<9}{3}{0:.<10}'.format('','หมา',str(amount[0]),str(amount[0]*15)))
    if amount[1]!=0:
        print('{0:.<4}{1}{0:.<6}{2}{0:<9}{3}{0:.<10}'.format('','แมว',str(amount[1]),str(amount[1]*25)))
    if amount[2]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:<9}{3}{0:.<10}'.format('','หมีแพนด้า',str(amount[2]),str(amount[2]*75)))
    if amount[3]!=0:
        print('{0:.<6}{1}{0:.<8}{2}{0:<9}{3}{0:.<10}'.format('','งู',str(amount[3]),str(amount[3]*5)))
    if amount[4]!=0:
        print('{0:.<6}{1}{0:.<3}{2}{0:<9}{3}{0:.<10}'.format('','หมู',str(amount[4]),str(amount[4]*2)))
    print('{0:_<38}'.format(''))
    print('{0:.<6}{1}{0:.<6}{2}{0:<9}{3}{0:.<10}'.format('','รวม',str(amounttt),str(pricett)))
    print('')

def four():
    n=0
    while(True):
        print('\tสินค้าในตะกร้ามีดังนี้')
        for i in anm:
            n+=1
            print('\t'+str(n)+'.'+i)
        n=0
        animal2=int(input('เลือกลำดับสินค้าาที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก:'))
        try:
            if animal2<=len(anm) and animal2!=-1:
                anm.pop(animal2-1)
            elif animal2==0 and animal2<=len(anm) and animal2!=-1:
                anm.pop(animal2)
            elif animal2==-1:
                break
        except:
            print('กรุณากรอกลำดับสินค้าให้ถูกต้อง')
            pass

def clear():
    os.system('cls')

while True:
    menu()
    if choice == '1':
        clear()
        one()
    elif choice == '2':
        clear()
        two()
    elif choice == '3':
        clear()
        three()
    elif choice == '4':
        clear()
        four()
    else:
        yesno=input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ')
        if yesno == 'y':
            break
        elif yesno == 'n':
            continue'''
'''def Introduce(arg1, arg2 = 'com', arg3 = 'ed', arg4='kku'):
    print('Hello, I am '+arg1+','+arg2+' '+arg3+' '+arg4)
Introduce('Python')
Introduce(arg1 = 'Python')
Introduce(arg1 = 'Python' , arg3 = 'Sci')
Introduce('Python', arg4 = 'CMU')'''
