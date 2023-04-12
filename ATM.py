
import time
import maskpass

class ATM():
    def __init__(self, card=None, asy=None):
        self.card = card
        self.balance = 100_000
        self.asy = asy
    
    def get_card_password(self):
        return self.__password
    
    def get_card(self):
        card = int(input("Kartani kirgizing: "))
        return card
    
    def get_password(self):
        password = maskpass.askpass(prompt="Parolni kiriting: ", mask="*")
        self.asy = password
        return password
        
    
    def get_user_answer(self):
        answer = input("Davom etasizmi: Y - (ha), N - (yo'q)")
        if answer.upper() == 'Y':
            self.get_menu()
        else:
            print("Foydalanganingiz uchun raxmat! \nKartangizni oling.")
            
    
    def get_sms_serivce(self):
        tel = int(input("Raqamingizni kiriting. \n+998 "))
        print("Xizmat ulandi.")
        self.get_user_answer()
        
    def get_balance(self):
        answer = input(
            """
            Check chop etilsinmi - 1
            Ekranga chiqarish - 2
            """
        )
        if int(answer) == 1:
            print(
                f"""
                Karta raqaqmi {self.card}
                balansingiz: {self.balance} so'm
                """
            )
        else:
            print(
                f"""
                Karta raqaqmi {self.card}
                Balansingiz: {self.balance} so'm
                """
            )
        self.get_user_answer()

    def get_cash_menu(self):
        intsumma = input(
            """
            1 - 50 000      | 2 - 100 000
            3 - 200 000     | 4 - 400 000
                Boshqa summa kiritish :
            """)
        
        if int(intsumma) == 1:
             amount = 50_000
        if int(intsumma) == 2:
             amount = 100_000
        if int(intsumma) == 3:
             amount = 200_000
        if int(intsumma) == 4:
             amount = 400_000
        if int(intsumma) > 4:
             amount = int(intsumma)

        n = amount//100
        t = amount+n

        print(
                f"""
                {amount} so'm
                {n} % 
                Jami : {t} so'm
                
                """
            )
        answer = input(
            """
            Davom ettirish - 1
            Bekor qilish - 2
            """
        )
        if int(answer) == 1:
            print("Iltimos kuting : ")

            timers = 5
    

            while timers:
                mins, secs = divmod(timers, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                timers -= 1
      


        if t > self.balance:
                print(
                    f"""
                    Operatsiyani amalga oshirib bo'lmadi !
                    Hisobingizda mablag' yetarli emas.
                    """
                    )
                
        else:
                print(
                    f"""Iltimos kartangizni oling !""" )
                                                            #balansdan yechilgan summani ayirib tawidi
                self.balance=self.balance-t
                    
        timers = 3
    

        while timers:
                mins, secs = divmod(timers, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                timers -= 1
        print("Naxt pulni oling !")
        self.get_user_answer()

    def set_cash(self):

        cash_amount = 0
        cash = int(input("""Pulni kiriting... 
                            
        Bankomat faqat 5.000 , 10.000 , 100.000 kupyuralarni qabul qiladi !
                            """))
        if int(cash) >= 5_000:
            
            cash_amount=cash+cash_amount
            

            n = cash_amount//100
            t = cash_amount-n

            print( f"""Jami kiritilgan summa : 
                 
                        {cash_amount} so'm
                        {n} % 
                        Jami : {t} so'm
                        
                        """)
            self.balance=self.balance+t
            
            self.get_user_answer()

        else:
            print("iltimos qaytadan kiriting.>>>")
            self.set_cash()

    def change_pin(self):
        
        change_pin = input("Kartangizni parolini o'zgartirmoqchimisiz ? Y - (ha), N - (yo'q)") 
                                
        if change_pin == 'Y':
            a = self.asy
            print(a)
            pin = int(input("Eski parolingizni kiriting:>>>"))
            
            if pin == int(a) :
                pin2 = int(input("Marhamat yangi parolni kiritng :>>>"))

                self.asy = pin2
                self.get_menu()

            else : 
                print("Parol noto'g'ri !\n Iltimos qaytadan kiriting::::")
                self.change_pin()

        else :
            print()

        self.get_menu()

    def bekorqilish(self):
        bekorqilish = input("Kartangizni parolini o'zgartirmoqchimisiz ? Y - (ha), N - (yo'q)") 
        if bekorqilish == 'Y':

            timers = 3
            while timers:
                    mins, secs = divmod(timers, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer, end="\r")
                    time.sleep(1)
                    timers -= 1
            print("Kartangizni oling....")
                    

        else : 
            print()
        self.get_menu()  

    def Info(self):    
        print(f"""
                Karta raqami : {self.card}
                Parol : {self.password}
                Hisobraqamidagi summa : {self.balance}
                """)

    def get_menu(self):
        menu = int(input(
            """
            Xizmatni tanlang
            
            1 - SMS xizmati     | 2 - Balance
            3 - Naqd pul yecish | 4 - Pul kirim qilish
            5 - Pin o'zgartirish| 6 - Bekor qilish
                            7 - Info
            """)
        )
        match menu:
            case 1:
                self.get_sms_serivce()
            
            case 2:
                self.get_balance()
            
            case 3:
                self.get_cash_menu()
            
            case 4:
                self.set_cash()
            
            case 5:
                self.change_pin()
            case 6:
                self.bekorqilish()
            case 7:
                self.Info() 
        if menu > 5:
            pass
    
    def start(self):
        self.card = self.get_card()
        print(
            """
            1 - O'zbek
            2 - English
            3 - Русский
            """
            )
        input("Tilni tanglang: ")
        password = self.get_password()
        action = 1
        flag = True
        while True:
            if action > 2:
                print("Kartani bloklandi!!! \n tel: +9889999999999")
                flag = False
                break
            elif len(str(password)) != 4:
                print(f"Xato parol {3 - action} ta imkoniyatingiz qoldi.")
                action += 1
                self.get_password()
            else:
                self.password = password
                break
        if flag:
            self.get_menu()
        
        
        
ATM().start()