
class Tv:
    def __init__(self,colour,Price,Brand):
        self.Tv_colour = colour
        self.Tv_price = Price
        self.Tv_brand = Brand

    def TV_datails(self):
        Tv_colour = self.Tv_colour
        Tv_brand = self.Tv_brand
        Tv_Price = self.Tv_price

        print(f'Tv Colour :-{Tv_colour} \n Tv Brand :- {Tv_brand} \n Tv Price :- {self.Tv_price}')


tv1 = Tv('Black',20000,'Sansui')
tv1.TV_datails()
        