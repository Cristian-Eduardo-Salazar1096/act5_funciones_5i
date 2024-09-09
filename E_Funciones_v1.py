print("Manejo de funciones V!")
def hola_mundo():
    print("hola aqui estoy adentro de la funcion")
    
#llamando a la funcion
hola_mundo()

def Mensa(msg):
    print(msg)

def EscribeNC(Nombre,Apellido):
    print(Nombre,Apellido)
    print(f"Tu Nombre completo es: {Nombre} {Apellido}")
def suma2numeros(n1,n2):
    s=n1+n2
    return f"La suma de {n1} y de {n2} es de:", s
Mensa("Hola Whatsapp") # llama a mensa con 1 parametro
Mensa("El profe mas sorprendido enviando mensajes")# llama a mensa con 1 parametro
EscribeNC("Cristian","Salazar")
print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))

