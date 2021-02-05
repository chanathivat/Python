import os
import datetime
name =[]
score = []
time2 = []
hit = []

def time():
    x = datetime.datetime.now().replace(microsecond=0)
    print(x)

num = int(input('กรุณากรอกจำนวนผู้เข้ารวม : '))
for i in range(num):
    print(i+1,end='.) ')
    name2 = input('ชื่อผู้เข้าซ้อม : ')
    score2 = float(input('คะแนน : '))
    time3 = float(input('ระยะเวลาที่ใช้ : '))
    name.append(name2)
    score.append(score2)
    time2.append(time3)
    hit.append(score2/time3)

for i in range(num):
    j=i
    for j in range(num):
        if hit[i]>hit[j]:
            a,b,c,d = hit[i],name[i],score[i],time2[i]
            hit[i],name[i],score[i],time2[i] = hit[j],name[j],score[j],time2[j]
            hit[j],name[j],score[j],time2[j] = a,b,c,d

os.system('cls')
x = datetime.datetime.now()
print('Shotgun',x.strftime('%A'),'Training',x.year)
print('Condtion : 1')
time()
print('-'*78)
print('{0:-<5}{1:-<7}{2:-<8}{3:-<17}{4:-<13}{5:-<15}{6}'.format('No.','PTS','TIME','COMPETITOR#Name','HIT FACTOR','STATE POINTS','STATE PERCENT'))
print('-'*78)
for i in range(num):
    points = (hit[i]/hit[0])*50
    percent = (points/(hit[0]/hit[0]*50))*100
    print('{0:<5}{1:<7}{2:<8}{3:<17}{4:<13}{5:<15}{6}'.format(i+1,int(score[i]),'%.2f'%time2[i],name[i],'%.4f'%hit[i],'%.4f'%points,'%.2f'%percent))