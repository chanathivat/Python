'''print('\tเลือกเมนูเพื่อทำรายการ','####################################')
print('####################################')
x=int(input('\tกด 1 เลือกเหมาจ่าย\n\tกด 2 เลือกจ่ายเพิ่ม\n'))
if x==1:
    a=int(input('กรุณากรอกระยะทาง\n'))
    if a<25:
        print('ค่าใช้จ่าย รวมทั้งหมด 25 บาท')
    else :
        print('ค่าใช้จ่าย รวมทั้งหมด 55 บาท')
elif x==2:
    b=int(input('กรุณากรอกระยะทาง\n'))
    if b<25:
        print('ค่าใช้จ่าย รวมทั้งหมด 25 บาท')
    else:
        print('ค่าใช้จ่าย รวมทั้งหมด',int(25+55),'บาท')'''
'''i=0
b=0
Sum=0
a=int(input('กรุณากรอกจำนวนครั้งการรับค่า\n'))
while(i<a):
    b=int(input('กรอกตัวเลข\t'))
    Sum=Sum+b
    i+=1
print('ผลรวมค่าที่รับมาทั้งหมด =',Sum)'''
'''list=[]
i=1
s=0
print('ป้อนชื่ออารหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม')
while(i<999):
    อาหาร=str(input('อาหารโปรดอันดับที่ '+ str(i)+' คือ\t'))
    if อาหาร=='exit':
        break
    list.append(อาหาร)
    i+=1
print('อาหารสุดโปรดของคุณมีดังนี้',end='  ')
for i in list:
    s=s+1
    print('%s.'%s,i,end='\t')'''
a=[]
while True:
    b = input('Dome Barber\nเพิ่ม [a]\nแสดง [s]\nออกจากระบบ [x]\n')
    b = b.lower()
    if b=='a':
        c= input('ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด)')
        a.append(c)
        print('++++++ข้อมูลได้เข้าสู่ระบบ++++++\n')
    elif b=='s':  
        print('{0:-<6}{0:<10}{0:-<10}'.format(''))
        print('{0:-<8}{1:<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:<10}{0:-<10}'.format(''))
        for d in a:
            e = d.split(':')
            print('{0[0]:<6}{0[1]:<10}({0[2]:<10})'.format(e))
            continue
    elif b=='x':
        break
print('ทำคำสั่งถัดไป')
'''student = int(input('Please enter student : '))
print('-'*30)
point_grade = [0 , 0 , 0 , 0 , 0 , 0]
score_grade = ['90-100 :','80-89  :','70-79  :','60-69  :','50-59  :',' 0-49  :']
i = 1
while i <= student :
    point = int(input('Please enter Score : '))
    i+=1
    if point <= 100 and point >= 90 :
        point_grade[0] += 1 
    elif point < 90 and point >= 80 :
        point_grade[1] += 1 
    elif point < 80 and point >= 70 :
        point_grade[2] += 1
    elif point < 70 and point >= 60 :
        point_grade[3] += 1
    elif point < 60 and point >= 50 :
        point_grade[4] += 1
    elif point < 50 and point >= 0 :
        point_grade[5] += 1 
for x in range(0,6) :
    print(score_grade[x],'*'*point_grade[x])'''