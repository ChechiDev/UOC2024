#Pregunta 1
# Primero crearemos una función personalizada, para validar los parámetros y evitar duplicar código.
def param_validation(inputValue, keys, token, functionMode="encrypt"):
    # He creado un parámetro "functionMode", que me servirá de chivato para determinar que mensaje de salida debe mandarse al usuario.
   
    # Lista de los tokens válidos:
    valid_token = ["=", "*", "+", "#", "%", "/"]
    # Creamos una lista vacía para la comprobación de las Keys
    valid_keys = []
    valid_dict = {}

    # Personalizamos el mensaje de salida según queremos encriptar o desencriptar
    mensajeError = ""
    if functionMode == "encrypt":
        mensajeError = "No es posible encriptar la cadena. Verifique los parámetros de entrada"

    else:
        mensajeError = "No es posible desencriptar la cadena. Verifique los parámetros de entrada"    

    # --- VERIFICACION DE LOS PARÁMETROS:  
    # Validamos el diccionario:
    for key, value in keys.items():
        # Verificamos que las claves sean alfabéticas:
        if type(key) is not str or not key.isalpha():
            raise ValueError(f"{mensajeError}")
        # Verificamos que los valores sean números enteros:
        elif type(value) is not int:
            raise ValueError(f"{mensajeError}")
        # Verificamos si hay duplicados:
        elif key in valid_keys:
            raise ValueError(f"{mensajeError}")

        valid_keys.append(key)
        valid_dict[key] = value

    if functionMode == "encrypt" and token in inputValue:
        raise ValueError(f"{mensajeError}")
    
    # Verificamos que el Token esté dentro de la lista de Tokens válidos:
    elif not token in valid_token:
        raise ValueError (f"{mensajeError}")
    
    # Verificamos que el Token se introduzca correctamente:
    elif len(token) != 1:
        raise ValueError (f"{mensajeError}")
    
# ---------------------------------------------------------------------------------

def encrypt(inputValue, keys, token):
    #PUT YOUR CODE HERE
    try:
        param_validation(inputValue, keys, token, functionMode="encrypt")
    
    except ValueError as e:
        return f"{e}"

    # --- ENCRIPTACIÓN:
    # Creamos una variable vacía para guardar la encriptación:    
    encrypt_inputValue = ""

    # Recorremos los carácteres de inputValue con un loop FOR:
    for i in inputValue:
        #  Miramos si el carácter está en el diccionario Keys. Si está lo reemplaza y añadimos el Token a cada lado del carácter
        if i in keys:
            encrypt_inputValue += f"{token}{keys[i]}{token}"
        
        #  Si el carácter no está en el diccionario, devolvemos el carácter original
        else:
            encrypt_inputValue += i
    
    # Devolvemos la variable con el inputValue encriptado
    return encrypt_inputValue

print(encrypt("hola", {"a": 1}, "*"))
print(encrypt("Mis amigos son GENIALES.", {"i": 0, "E": 8, "a": 3, "A": 4}, "+"))
encrypt("hola 11", {"a": 1}, "#")
encrypt("16", {"A": 1}, "%")
encrypt("Hola mi celular es 09999999", {"e": 5, "H": 7}, "/")
encrypt("Opcion que permite generar una solicitud", {"O": 120, "o": 20, "e": 17, "p": 100, "u": 30}, "*")

# --- Restricciones:
print(encrypt("Hola mi celular es 09999999", {"9": 7, "H": 8}, "="))
print(encrypt("Hola mi celular es 09999999", {"e": 7, "H": 8}, "¿"))
print(encrypt("Hola ** mi celular es 09999999", {"e": 7, "H": 8}, "*"))

# ---------------------------------------------------------------------------------

#Pregunta 2:
def decrypt(inputValue, keys, token):
    #PUT YOUR CODE HERE
    
    # Validamos que los parámetros de entrada son los correctos con la función auxiliar "param_validation":
    try:
        param_validation(inputValue, keys, token, functionMode="decrypt")
    
    # Creamos las excepciones
    except ValueError as e:
        return f"{e}"


    # --- DESENCRIPTACIÓN:
    # Guardamos la cadena desencriptada:
    decrypt_inputValue = ""
    
    # Creamos un señuelo que nos indique si coincide el carácter con un token:
    temp_token = False
    
    # Creamos una variable temporal para almacenar los números que encontremos:
    temp_inputValue_parts = ""
  
    
    # Recorremos la cadena temporal dividida "temp_inputValue_parts" en busca de los números:"
    for part in inputValue:
        # Cuando part coincida con un token, entramos:
        if part == token:
            if temp_token == True:
                
                # Recorremos el diccionario Keys en busca de la clave que corresponda al número:
                for key, value in keys.items():
                    if value == int(temp_inputValue_parts):
                        decrypt_inputValue += key
                        break
                
                # Vaciamos la variable temporal dónde guardamos el número:
                temp_inputValue_parts = ""
                
                # Reiniciamos el señuelo:
                temp_token = False
                    
            else:
                temp_token = True
            
        elif temp_token:
            # Si es un número lo añadimos a una variable temporal:
            temp_inputValue_parts += part
                    
        else:
            # Si la parte de la cadena no es un número, lo añadimos a la variable de desencriptación sin reemplazarla:
            decrypt_inputValue += part        
    
    # Devolvemos el texto desencriptado:
    return decrypt_inputValue  

print(decrypt("hol*1*", {"a": 1}, "*"))
decrypt ("M+0+s +3+m+0+gos son G+8+NI+4+L+8+S.", {"i":0,"E":8,"a":3,"A":4}, "+") # devolvería “Mis amigos son GENIALES.”
decrypt("hol#1# 11", {"a": 1}, "#")
decrypt("16", {"A": 1}, "%")
decrypt("/7/ola mi c/5/lular /5/s 09999999", {"e": 5, "H": 7}, "/")
decrypt("*120**100*ci*20*n q*30**17* *100**17*rmit*17* g*17*n*17*rar *30*na s*20*licit*30*d", {"O": 120, "o": 20, "e": 17, "p": 100, "u": 30}, "*")

# --- Restricciones:
decrypt("Hola mi celular es 09999999", {"9": 7, "H": 8}, "=")
decrypt("Hola mi celular es 09999999", {"e": 7, "H": 8}, "¿")