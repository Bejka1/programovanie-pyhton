#nasa prva kalkulacka
print(" ===Vitaj v kalkulacke====")
print("Vyber si matematicku operaciu")
print("1.===nasobenie===")
print("2.===odcitanie===")
print("3.===delenie===")
print("4.===celociselne delenie")



x= int (input("Zadaj operaciu:"))
a= float(input("Zadaj prve cislo: "))
b= float (input("Zadaj druhe čislo: "))
if x == 1:
   print("nasobenie je:" , a*b)
if x == 2:
   print("odcitanie je:" , a-b)
if x == 3:
   print("delenie je:" , a/b)
if x == 4:
    print("celoceselne delenie je:" , a//b)
    


   
