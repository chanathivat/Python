class shop:
    A = []
    B = []
    def __init__(self,name,item,price,amount):
        self.name = name
        self.item = item
        shop.A.append(item)
        self.price = price
        shop.B.append(price)
        self.amount = amount

    def choice(self):
        global choice
        print('*'*10,'YuRINN','*'*10)
        #choice = input('\tแสดงรายการสินค้า [a]\n\tเพิ่มรายการสินค้า [s]\n\tออกจากระบบ [x]\n\nกรุณาเลือกคำสั่งสินค้า : ')


print shop.A