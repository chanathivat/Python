############################################################5.1####################################################################################################
class nisit:
    def __init__(self,name,province,year,department,sex):
        self.name = name
        self.province = province
        self.year = year
        self.department = department
        self.sex = sex

    def show(self):
        if self.sex == 'ชาย':
            print('สวัสดีครับ ผมชื่อ '+self.name +' มาจากจังหวัด'+self.province+' เพศ'+self.sex+ ' นักศึกษาชั้นปีที่ '+self.year + ' สาขา '+self.department)
        elif self.sex == 'หญิง':
            print('สวัสดีค่ะ ฉันชื่อ'+self.name +' มาจากจังหวัด'+self.province+' เพศ'+self.sex+ ' นักศึกษาชั้นปีที่ '+self.year + ' สาขา '+self.department)
        else:
            print('ERROR!')

    @classmethod
    def info(self):
        print('-'*15,'แนะนำตัว','-'*15)
        #print('ชื่อ-สกุล:เพศ:ชั้นปี:สาขาวิชา:')
        name = input('ชื่อ : ')
        province = input('จังหวัด : ')
        year = input('ชั้นปี : ')
        department = input('สาขา : ')
        sex = input('เพศ : ')
        return self(name,province,year,department,sex)

x = nisit.info()
x.show()

###################################################################5.2##########################################################################################
import os
name_list = ['แมว','สุนัข','หมีแพนด้า','สิงโต']
price_list = [8,6,9,8]
class market :
    def list_def(self):
        for x in range(0,len(name_list)):
            print(x+1,name_list[x],price_list[x],'บาท')
    def choose(self):
        print('*'*10,'','*'*10)
        print('\tแสดงรายการสินค้า [a]\n\tเพิ่มรายการสินค้า [s]\n\tออกจากระบบ [x]')
    def input_choise(self):
        global choise
        choise = input('กรุณาเลือกคำสั่ง: \t')
    def add_list(self):
        while True:
            print('เพิ่มรายการสินค้า หากต้องการกรอก exit')
            add_name = input('เพิ่มชื่อสินค้า: ')
            if add_name == 'exit':
                break
            else : 
                add_price = input('เพิ่มราคาสินค้า: ')
                name_list.append(add_name)
                price_list.append(add_price)
            add = input ('ต้องการเพิ่มสินค้าอีกหรือไม่ [y/n]: ')
            if add == 'n' :
                break
            elif add == 'y' :
                os.system('cls')

while True:
    x = market()
    x.choose()
    x.input_choise()
    if choise == 'a' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง:\t',choise)
        x.list_def()
    if choise == 's' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง:\t',choise)
        x.add_list()
    if choise == 'x' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง:\t',choise)
        close = input('ต้องการออกจากระบบหรือไม่ [y/n] : ')
        if close == 'n' :
            os.system('cls')
        if close == 'y' :
            os.system('cls')
            print('ออกจากระบบเรียบร้อยแล้ว')
            break