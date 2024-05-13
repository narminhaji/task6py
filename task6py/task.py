
# class hesab():
#     def __init__(self, num, balans):
#         self.__num = num
#         self.__balans = balans

#     def balans_goster (self):
#         print(f'Balans: {self.__balans}')
    
#     def balans_i(self, pul):
#         if (pul <= 0): return
#         self.__balans += pul
#         print(f'topla{pul}')

#     def cixis (self, pul):
#         if (self.pull(pul)):
#             self.__balans -= pul
#             print(f'çıx{pul}')
#         else:
#             print('Yetərsiz balans: ')

#     def pull(self, pul):
#         return pul <= self.__balans and pul > 0


# class kredit (hesab):
#     __miqdar= 0
#     def __init__(self, num, balans, miqdar = 0):
#         super().__init__(num, balans)
#         self.kredit_al(miqdar)
    

#     def kredit_al(self, kreditin_miqdari):
#         if (kreditin_miqdari <= 0): return

#         super().balans_i(kreditin_miqdari)
#         self.__miqdar += kreditin_miqdari
#         self.ayliqodenis = round(self.__miqdar / 12, 2)
#         print(f'Sizin aylıq ödənişiniz: {self.ayliqodenis}')

    
#     def ode(self, pul):
#         if (not super().pull (pul)): 
#             print('Yetərsiz balans!!!!! ')
#             return 
        
#         if (pul > self.__miqdar):
#             pul = self.__miqdar

#         super().cixis(pul)
#         self.__miqdar -= pul
#         print(f'yekun {self.__miqdar}')


# kredit = kredit("87654321, 500)
# kredit.kredit_al(1200)
# kredit.balans_goster()
# kredit.ode(600)
# kredit.balans_goster()
# kredit.cixis(430)
# kredit.balans_i(540)








class Hesab:
    def __init__(self, num, balans):
        self.__num = num
        self.__balans = balans

    def balans_goster(self):
        print(f'Balans: {self.__balans}')

    def balans_artir(self, pul):
        if pul > 0:
            self.__balans += pul
            print(f'Topla{pul}')

    def pul_cixar(self, pul):
        if self.pul_cixar_mumkunmu(pul):
            self.__balans -= pul
            print(f'Çıx{pul}')
        else:
            print('Yetərsiz balans')

    def pul_cixar_mumkunmu(self, pul):
        return pul > 0 and pul <= self.__balans


class Kredit:
    def __init__(self, num, balans, miqdar=0):
        self.__num = num
        self.__balans = balans
        self.__miqdar = miqdar

    def kredit_al(self, miqdar):
        if miqdar > 0:
            self.__balans += miqdar
            self.__miqdar += miqdar
            self.ayliq_odenis = round(self.__miqdar / 12, 2)
            print(f'Aylıq ödəniş: {self.ayliq_odenis}')

    def kredit_ode(self, pul):
        if pul > 0:
            ode = min(pul, self.__miqdar)
            self.__balans -= ode
            self.__miqdar -= ode
            print(f'Ödənilən məbləğ: {ode}')

    def kredit_meqdari(self):
        return self.__miqdar

    def kredit_bakiyesi(self):
        return self.__balans



hesab1 = Hesab("54321", 500)
kredit1 = Kredit("54321", 500)
kredit1.kredit_al(1200)
print(f'Balans: {kredit1.kredit_bakiyesi()}')
kredit1.kredit_ode(600)
kredit1.kredit_ode(40)
print(f'Balans: {kredit1.kredit_bakiyesi()}')
kredit1.pul_cixar(430)
hesab1.balans_artir(540)
