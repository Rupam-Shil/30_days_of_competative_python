'''  
5th Graders kara and Rani both have lemonade
stands. Kara sells her lemonade at 5 cents a glass
and Rani sells hers at 7 cents a glass. Kara sold K number
of glasses of lemonade today and Rani sold r number of glasses.
Who made the most money and by what amount?
k and r are user entered value..'''

k = int(input("Enter no. of glasses Kara Sold today: "))
r = int(input("Enter no. of glasses Rani Sold today: "))


def totalPrice(price, glass):
    return price * glass


kara = totalPrice(5, k)
rani = totalPrice(7, r)
if kara > rani:
    print(f"Kara earns {kara-rani} Cents more than Rani")
else:
    print(f"Rani earns {rani-kara} Cents more than Kara")
