cliente=input("Ingrese nombre del cliente: ").strip()

while cliente== "" or not cliente.isalpha():
    cliente=input("Ingrese el nombre correctamente: ").strip()

cantidadstr= input("Ingrese cantidad de productos a comprar: ").strip()

while not cantidadstr.isdigit() or int(cantidadstr) == 0:
    cantidadstr=input("Ingrese cantidad, SOLO NUMEROS enteros positivos (sin espacios ni letras)").strip()

cantidadint= int(cantidadstr)
totalcondescuento=0
totalsindescuento=0


for i in range(1,cantidadint+1):
    preciostr= input(f"Producto {i} - Precio:  ").strip()

    

    while not preciostr.isdigit() or int(preciostr) == 0:
        preciostr= input("Ingrese el precio SIN ESPACIOS ni LETRAS y deberia ser MAYOR a 0: ")
    
    precioint=int(preciostr)

    descuento= input("Ingrese si tiene o no descuento (Ss/Nn)").lower().strip()
    
    while descuento != 's' and descuento != 'n':
        descuento= input("Insgrese S o N")
    
    totalsindescuento += precioint

    if descuento == 's':
        preciofinal=precioint * 0.9
    else:
        preciofinal=precioint
    
    totalcondescuento += preciofinal

ahorro = totalsindescuento - totalcondescuento
promedio = totalcondescuento / cantidadint
print(f"Cliente: {cliente}")

print(f"El precio total sin descuentos es: $ {totalsindescuento:.2f} ")
print(f"El precio total con descuentos es: $ {totalcondescuento:.2f} ")
print(f"El ahorro total fue de: $ {ahorro:.2f}")
print(f"Promedio por producto:  $ {promedio:.2f}")


    