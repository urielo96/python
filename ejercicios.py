# Haciendo el codigo de la libreria en python

nLibrosComprados = 0

nLibrosComprados = int(input(" Cuantos libros comprara el cliente? "))

total_compra = 0

for i in range(nLibrosComprados):
    
    precio_libro = 0

    precio_libro = float(input("Ingrese el precio del libro: "))

    

    total_compra += precio_libro

    

if total_compra > 1000:
    descuento = (20 * total_compra) / 100
    total_compra -= descuento
    print("Por comprar mas de 1000 pesos el cliente tiene un descuento de: ", descuento)

print("El total de la compra es de : ", total_compra)



print("Gracias por su compra!")