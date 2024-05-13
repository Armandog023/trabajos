import random
peli=["masacre en texas", "Exterminio"]
peli2=["Dragon Ball Z: La Resurrección de Freezer","Los Simpson: La película","Kung Fu Panda"]

print("lista de peliculas ")

edad = int (input("telcea tu edad "))

if (edad>=18):

    print(random.choice(peli))
else:

    print(random.choice(peli2))