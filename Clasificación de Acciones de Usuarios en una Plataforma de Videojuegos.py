"""

Combate rapido (duracion < 100 seg)

Combate de larga duracion (≥ 100 seg)

Dentro de cada uno podes diferenciar por resultado: victoria o derrota.

Exploracion

Exploracion sin hallazgos

Exploracion con hallazgos breve (≤ 200 seg)

Exploracion con hallazgos prolongada (> 200 seg)

Interaccion social

Leve (duracion corta, pocos mensajes)

Moderada (duracion media)

Alta (duracion larga, muchos mensajes)"""
def clasificarAccion(accion,tiempo):
    accion=accion.capitalize()
    

    if accion=="Combate":
        if tiempo < 100:
            resultado=input("Victoria o Derrota? ")
            if resultado=="Victoria":
                return "Victoria en combate de corta duracion"
            else:
                return "Derrota en combate de corta duracion"
        else:
            resultado=input("Victoia o Derrota? ")
            resultado=resultado.capitalize()
            if resultado =="Victoria":
                return "Victoria en combate de larga duracion"
            else:
                return "Derrota en combate de larga duracion"    
    elif accion=="Exploracion":

        if tiempo < 200:
            hallazgo=input("responda si o no: descubrio algo? ")
            hallazgo=resultado.capitalize()
            if resultado=="Si":
                return "Exploracion corta con hallazgos "
            else:
                return "Exploracion corta sin hallazgos"
        else:
            resultado=input("responda si o no: tuvo suerte en la busqueda? ")
            resultado=resultado.strip().capitalize()
            if resultado=="Si":
                return "Exploracion de larga duracion con hallazgos "
            else:
                return "Exploracion de larga duracion sin hallazgos "          
    elif accion=="Interaccion social":
        if tiempo < 150:
            return "interaccion social rapida"
        else:
             return "interaccion social larga"

# Pedir datos al usuario
usuario = input("Ingrese el nombre del usuario: ")
accion = input("Ingrese la acción (Combate/Exploracion/Interaccion social): ")
tiempo = int(input("Ingrese la duracion en segundos: "))
def guardarHistorial(usuario, accion, tiempo, clasificacion):
    with open("historial.txt", "a") as archivo:
        archivo.write(f"{usuario},{accion},{tiempo},{clasificacion}\n")
clasificacion=clasificarAccion(accion,tiempo)

guardarHistorial(usuario, accion, tiempo, clasificacion)

print("Registro guardado en historial.txt")
def contarVictorias(usuario):
    victorias = 0
    with open("historial.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")  # separa por comas
            nombre, accion, tiempo, clasificacion = datos
            if nombre == usuario and "Victoria" in clasificacion:
                victorias += 1
    return victorias

# Uso:
jugador = input("Ingrese el nombre del jugador a consultar: ")
print(f"{jugador} tiene {contarVictorias(jugador)} victorias.")


