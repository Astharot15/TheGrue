from hashlib import *

def calcular_hash(data):            #Función hash sha-256 de haslib
    sha256 = hashlib.sha256()     
    sha256.update(data)     
    return sha256.hexdigest()


def concatenar_strings(array):      #Función concatenar de dos en dos las posiciones de un array
    half_array = []
    for i in range(0, len(array), 2):
        half_array.append(array[i] + array[i + 1])

    return half_array


def sustituir_con_hash(array):      #Función que sustituye las entradas de un array por el resultado de pasarlas por una función externa
    hash_array = [calcular_hash(string) for string in array]
    return hash_array



targetHash = "30c085686aa4b1d76ac1c72dfefab6f4a02f5e3865acd76f868b6d5781d2efc8"
mensaje = ["The","password","that","I","use","is","the","same","as","in","the","Google","account","it","is"]

wordlist = []
with open("/usr/share/wordlists/rockyou.txt", "r", encoding='latin1') as file:
        for line in file:
            wordlist.append(line.strip())

for password in wordlist:

    temp_mensaje = []
    temp_mensaje = mensaje.copy()
    temp_mensaje = temp_mensaje.append(password)

    temp_mensajemensaje = sustituir_con_hash(mensaje)

    while len(mensaje) > 1:
    
        temp_mensajemensaje = concatenar_strings(temp_mensajemensaje)
        print(mensaje)
        temp_mensajemensaje = sustituir_con_hash(temp_mensaje)
        print(mensaje)


    if temp_mensaje[0] == targetHash:
        print(password)
        break