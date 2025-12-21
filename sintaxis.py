"""
if 5>3:
    print("es mayor que 3")
#este codigo vale pura monda

x = "Esta es una x" 
print(x)

x,y,z = "manzana", "naranja", "banano"
print (x,y,z)

a = b = c = "Mandarina"
print(a,b,c)

print("Mi fruta favorita es " + z)
print(a+z)



 # ordenada y mutable, sus elementos pueden cambiar
lista = [0, 1, 2, 3, 4, 5]     

# tupla ordenada e inmutable, sus elementos no se pueden modificar
tupla = ('A', 'B', 'C')

# Diccionario, Un diccionario es una colección ordenada de pares clave:valor y es mutable

diccionario = {

    "mombre" : "Sebasitan",
    "Edad" : 30,
    "Ciudad" : "Pereira"
}

#Conjuntos (sets), Un conjunto (set) es una colección desordenada, mutable y de elementos únicos. 
# No admite repetidos.

conjunto = {1,1,2,3,3,4} # Output = {1,2,3}

#Booleanos, Un booleano puede ser **verdadero** o **falso**. Se escribe con T y F mayúsculas
    
booleano_verdadero = True
booleano_falso = False

# Tipos numéricos y verificación
x = 1          # entero
y = 2.5        # flotante
z = 5 + 1j     # complejo (parte real 5, parte imaginaria 1j)

print(type(x))  
print(type(y))  
print(type(z))  

# Entero a flotante: agrega .0
x = 1
xf = float(x)
print(type(xf))  # float
print(xf)        # 1.0

# Flotante a entero: trunca
y = 2.5
ye = int(y)
print(type(ye))  # int
print(ye)        # 2  # cuidado: se pierde la parte decimal

entero = 5
flotante = 5.5

entero_complejo = complex(entero)
flotante_complejo = complex(flotante)

print(entero_complejo, type(entero_complejo))     # (5+0j) 
print(flotante_complejo, type(flotante_complejo)) # (5.5+0j) 


import random

print(random.randrange(1, 10))  # entero aleatorio entre 1 y 9


"""

father = "padre en ingles"
mother = 'Madre en ingles'
son = 'Father and mother "project" '
daugther = " father's and mother's creation "
palabra_larga = "esternocleidomastoideo"
triple_frase = """sexo
drogas
y mucho alchol
"""
print(triple_frase)

#Indica la cantidad de caracteres
print(len(palabra_larga))

#Busca la palabra en el texto y arroja True si esta, false si no esta
phrase = "Every day I wake up then I start to break up, lonely is a man wihtout love, but man, 2 times man"
buscador = "man" in phrase
print(buscador)

#Misma funcionalidad pero preguntando de forma negativa
buscador_negativo = "sex" not in phrase
print(buscador_negativo)

# Transformación de texto
mayuscula = phrase.upper()
minuscula = phrase.lower()
print(mayuscula)
print(minuscula)

# Limpieza de espacios
espacios = "   este es el texto   "
sin_espacios = espacios.strip()
print(sin_espacios)



