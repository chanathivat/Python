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