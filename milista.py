# ejemplo de uso de listas 

misnovias=["aripina", " anastacia", "maria"]
misnumeros=[666,77,10]
# mostrando a mis novias
print(misnovias)
# mostrando mis numeros
print(misnumeros)
print("----accediendo a los elemntos de la lista----")
print(misnovias[-2])
if "ana" in misnovias :
    print(" si, ana esta en la pista de mis novias")
else:
    print("chale no es mi novia")
print("numero de movias")
novias=len(misnovias)
print(f"numero de novias{novias}")
print(" ciclo for en listas")
posicion=0
for medianaranja in misnovias :
    print(posicion, " ",medianaranja)
    posicion = posicion + 1