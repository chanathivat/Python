# n1 =input('Input First Number : ')
# n2 =input('Input Second Number : ')
# print('%s'%n1,'=','%s'%n2, ':' ,n1 == n2)
# print('%s'%n1,'>','%s'%n2, ':' ,n1 > n2)
# print('%s'%n1,'<','%s'%n2, ':' ,n1 < n2)
# a = 60
# b = 13
# c = 0
# c = a & b
# print(c)
# c = a | b
# print(c)
# c = a ^ b
# print(c)
# c = ~a
# print(c)
# c = a << 2
# print(c)
# c = a >> 2
# print(c)
# print('Day Converter Program')
# day = input('Input number of Days --> ')
# print('%s'%day,'Days --> Hour',int(day)*24,'Hour')
# print('%s'%day,'Days --> Minutes',int(day)*24*60,'Minutes')
# print('%s'%day,'Days --> Seconds',int(day)*24*60*60,'Seconds')
# animal={'cat','dog','rat','pig','ant'}
# animal.add('monkey')
# animal.update(['python','cipibara','spider','wombat','penguin','crocodile','zicoloc'])
# print(animal)
# print('++++++++++++++++++++++++++++++++++++++')
# print('\tโปรแกรมหยิบสินค้าใส่ตระกร้า')
# print('++++++++++++++++++++++++++++++++++++++')
# สินค้า=[]
# สินค้า.append(input('หยิบสินค้าชิ้นที่ 1 '))
# สินค้า.append(input('หยิบสินค้าชิ้นที่ 2 '))
# สินค้า.append(input('หยิบสินค้าชิ้นที่ 3 '))
# สินค้า.append(input('หยิบสินค้าชิ้นที่ 4 '))
# สินค้า.append(input('หยิบสินค้าชิ้นที่ 5 '))
# print('สินค้าที่หยิบใส่ตะกร้ามีดังนี้')
# for x in สินค้า:
#     print(x)
# print('1.',สินค้า[0])
# print('2.',สินค้า[1])
# print('3.',สินค้า[2])
# print('4.',สินค้า[3])
# print('5.',สินค้า[4])
thisdict1 = {
    'ลาดกระบัง-บางบ่อ' : '25 บาท',
    'ลาดกระบัง-บางประกง' : '30 บาท',
    'ลาดกระบัง-พนัสนิคม' : '45 บาท',
    'ลาดกระบัง-บ้านบึง' : '55 บาท',
    'ลาดกระบัง-บางพระ' : '60 บาท',
}
thisdict2 = {
    'ลาดกระบัง-บางบ่อ' : '45 บาท',
    'ลาดกระบัง-บางประกง' : '45 บาท',
    'ลาดกระบัง-พนัสนิคม' : '75 บาท',
    'ลาดกระบัง-บ้านบึง' : '90 บาท',
    'ลาดกระบัง-บางพระ' : '100 บาท',
}
thisdict3 = {
    'ลาดกระบัง-->บางบ่อ' : '60 บาท',
    'ลาดกระบัง-->บางประกง' : '70 บาท',
    'ลาดกระบัง-->พนัสนิคม' : '110 บาท',
    'ลาดกระบัง-->บ้านบึง' : '130 บาท',
    'ลาดกระบัง-->บางพระ' : '140 บาท',
}
print('\tโปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์')
print('----------------------------------------------')
print('\tรถยนต์ 4 ล้อ\t\tกด 1')
print('\tรถยนต์ 6 ล้อ\t\tกด 2')
print('\tรถยนต์มากกว่า 6 ล้อ\t กด 3')
car=int(input('\tเลือกประเภทยานพาหนะ : '))
if car==1:
    print('ค่าบริการรถยนต์ 4 ล้อ\n')
    print(*thisdict1.items(), sep = '\n')
if car==2:
    print('ค่าบริการรถยนต์ 6 ล้อ\n')
    print(*thisdict2.items(), sep = '\n')
if car==3:
    print('ค่าบริการรถยนต์มากกว่า 6 ล้อ\n')
    print(*thisdict3.items(), sep = '\n')