class Hodim:

    def __init__(self, nomi, oylik, lavozimi):
        self.nomi = nomi
        self.oylik = oylik
        self.lavozimi = lavozimi

    def __str__(self):
        return f"Nomi: {self.nomi}\nOylik: {self.oylik}\nLavozimi: {self.lavozimi}"
    
class KorxonaHodim(Hodim):

    def __init__(self,  nomi, oylik, lavozimi, rating=0):
        super().__init__( nomi, oylik, lavozimi)
        self.rating = rating
    
    def __str__(self):
        return f"{super().__str__() }\nReyting:{self.rating}\nOshirilgan oylik: {self.oshirilgan_oylik()}" 
    
    def oshirilgan_oylik(self):
        if 60 <= self.rating < 75:
            return self.oylik * 1.2
        if 75 <= self.rating < 90:
            return self.oylik * 1.4
        if 90 <= self.rating <= 100:
            return self.oylik * 1.6                

hodim = KorxonaHodim("Otabek",1000,"Rahbar",75)
print(hodim)
