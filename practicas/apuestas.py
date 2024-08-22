import random

while True:
    usuario = int(input("Ingresa el 1 o 2: "))
    
    if usuario > 2:
        print("Recuerda, solo tienes que elegir el 1 o 2. Por favor, inténtalo de nuevo.")
    else:
        break

cpu = random.randint(1,2)
if usuario > cpu:
        print(f"el usuario aposto :{usuario}")
        print(f"el cpu aposto :{cpu}")
        print(f"gano el usuario!!!!")
elif usuario == cpu:
        print("empateeeee!")
else:
        print(f"el usuario aposto :{usuario}")
        print(f"el cpu aposto :{cpu}")
        print(f"gano el cpu!!!!")