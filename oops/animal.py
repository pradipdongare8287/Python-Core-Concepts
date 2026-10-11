
class Animal:
    def __init__(self,Name,Colour,Type):
        self.Animal_name = Name
        self.Animal_Colour = Colour
        self.Animal_Type = Type

    def Animal_detail(self):
        name = self.Animal_name
        colour = self.Animal_Colour
        type =  self.Animal_Type

        print(f'Animal Name is :- {name} \n Animal Colour is :- {colour} \n animal Type is {type}')

ani = Animal('Dog','Black','Domastic')
ani.Animal_detail()