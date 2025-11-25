import random
import re
from functools import reduce
import time
import json
import os
codigos_descuento = {
        "DESCUENTO10": 0.10,
        "GAMER20": 0.20,
        "SUPER30": 0.30
    } 

def cargarDatos():
    rutaUsuarios = os.path.join(os.path.dirname(__file__),"usuarios.json")#ruta de archivo de usuarios
    rutaJuegos = os.path.join(os.path.dirname(__file__),"juegos.json")#ruta de arhivo juego

    try: #json modo lectura
        with open(rutaUsuarios,"r") as archivo:
            usuariosObtenidos = json.load(archivo)

        with open(rutaJuegos,"r") as archivo:
            videojuegosObtenidos = json.load(archivo)
            return usuariosObtenidos, videojuegosObtenidos
        
    except Exception as e:
        print("ocurrio un error inesperado al cargar los datos", e) 


def guardarDatos():
    rutaUsuarios = os.path.join(os.path.dirname(__file__), "usuarios.json")#ruta de arichivo usuarios
    rutaJuegos = os.path.join(os.path.dirname(__file__), "juegos.json")#ruta archivo juegos

    try:#json escritura 
        with open(rutaUsuarios, "w", encoding="utf-8") as archivoUsuarios:
            json.dump(usuarios, archivoUsuarios, indent=4)

        with open(rutaJuegos, "w", encoding="utf-8") as archivoJuegos:
            json.dump(videojuegos, archivoJuegos, indent=4)

        print("Datos guardados correctamente")

    except Exception as e:
        print("Ocurrió un error al guardar los datos:", e)

def crearUsuario():
    try:
        if len(usuarios)==0:
            id = 0
        else:
            idMaximo = usuarios[-1]["id"]
            id = idMaximo+1

        usuario = input("nombre de usuario: ")
        nombresUsuarios = [usuarios[i]["user"] for i in range(len(usuarios))]

        while usuario in nombresUsuarios:
            print("usuario repetido")#valida que el usuario no exista, mediante la lista de comprension de la linea 53
            usuario = input("nombre de usuario: ")

    except Exception as e:
        print("Error al crear usuario:", e)
        



    password = input("cree su contraseña con 8 caracteres minimo: ")
    password2 = input("repita su contraseña por favor")

    while len(password)<8 or password2 != password:#valida requisitos de psw
        print("contraseñas no coincidentes o con cantidad de caracteres invalida")
        password = input("cree su contraseña con 8 caracteres minimo: ")
        password2 = input("repita su contraseña por favor")

    amigos = []
    juegos = []
    notificaciones = []

    nuevoUsuario ={ #apped al diccionario
        "id": id,
        "user":usuario,
        "password":password,
        "amigos":amigos,
        "juegos":juegos,
        "saldo": 0,
        "notificaciones": notificaciones,
    }

    usuarios.append(nuevoUsuario)#se agrega el diccionario a la lista

    print("usario creado con exito")

def mostrarJuegos():
    try:
        print("estos son los juegos disponibles en nuestra biblioteca, presione cualquiera para conocer su infomracion")
        for i in range(len(videojuegos)):
            print(f"{i}){videojuegos[i]['nombre']}")#printea lista de juegos
        
        try:
            juegoElegido = int(input("selecione un juego: "))
        except ValueError:
            print("Por favor ingrese un número válido")
            return False
            
        if juegoElegido < 0 or juegoElegido > len(videojuegos)-1:#valida numeros logicos
            print("ingreso invalido")
            return False
        
        datosJuego(juegoElegido)
        return juegoElegido
    except Exception as e:
        print("Error inesperado al mostrar juegos:", e)
        return False
    
def verPerfilUsuario(usuarioActivo):

    usuario = usuarios[usuarioActivo]

    print("\n===== PERFIL DEL USUARIO =====")
    print("Nombre de usuario:", usuario["user"])
    print("Saldo:", usuario["saldo"])

    print("\nAmigos:")
    if len(usuario["amigos"]) == 0:
        print("  No tenés amigos agregados.")
    else:
        for amigo in usuario["amigos"]:
            print(" -", amigo)

    # Mostrar biblioteca correcta (compartida o normal)
    print("\nJuegos disponibles:")
    if usuario["juegosBiblioteca"] is not None:
        print("  (Biblioteca compartida activa)")
        for juego in usuario["juegosBiblioteca"]:
            print(" -", juego["nombre"])
    else:
        if len(usuario["juegos"]) == 0:
            print("  No tenés juegos.")
        else:
            for juego in usuario["juegos"]:
                print(" -", juego)

    print("\nNotificaciones pendientes:", 
          sum(1 for n in usuario["notificaciones"] if not n["visto"]))
    print("==============================\n")

def datosJuego(id):
    #informacion de juegos
    print(f"Nombre: {videojuegos[id]["nombre"]}")
    print(f"Desarrollador: {videojuegos[id]["compania"]}")
    print(f"Descripcion: {videojuegos[id]["descripcion"]}")
    print(f"Precio: {videojuegos[id]["precio"]}")
    print(f"Trofeos Totales: {videojuegos[id]["trofeos_totales"]}")
    print(f"Durecion: {videojuegos[id]["duracion_horas"]}")

def cargaSaldo (usuarioActivo):
    try:

        patron = re.compile(r'^(?:\d{4}[- ]?){3}\d{4}$') #expresion regular para validar tarjeta 

        
        flag = True
        while flag :
            cuanto_saldo = float (input ("Cuanto dinero quiere ingresar? U$D: "))
            while cuanto_saldo < 0 or cuanto_saldo == 0:#valida numeros logicos
                print("No es posible ingrese una cantidad mayor a u$d 0")
                cuanto_saldo = float (input ("Cuanto dinero quiere ingresar? U$D: "))
            medio_pago = int (input("Que medio de pago desea elegir para finalizar su compra? 1-Mercado pago, 2-Tarjeta de credito, 3-tarjeta de debito: "))
            while medio_pago <1 or medio_pago > 3:#valida opciones logicas
                print("Seleccion no valida intente otra vez")
                medio_pago = int (input("Que medio de pago desea elegir para finalizar su compra? 1-Mercado Pago, 2-Tarjeta de credito, 3-tarjeta de debito: "))

            if medio_pago == 1:
                print("El alias es: insertcoin.mp")
                print(f"Se le acredito U$D {cuanto_saldo}, numero de orden {random.randint(0,100000)}")   
                usuarios[usuarioActivo]["saldo"]+=cuanto_saldo  
                flag = False

            
            elif medio_pago == 2:

                tarjetaCredito = input("Ingrese su tarjeta de credito: ")
                while bool(patron.fullmatch(tarjetaCredito)) == False: #valida la expresion regular de la linea 119
                    print("No es valido")
                    tarjetaCredito = input("Ingrese su tarjeta de credito: ")
                cvv = int(input("Ingrese el codigo de seguridad: ")) 
                while cvv < 100 or cvv >999:#valida 3 numeros de codigo de seguridad 
                    print ("No es valido")
                    cvv = int(input("Ingrese el codigo de seguridad: ")) 
                usuarios[usuarioActivo]["saldo"]+=cuanto_saldo  
                print ("Su compra ah sido exitosa")
                print(f"Se le acredito U$D {cuanto_saldo}, numero de orden {random.randint(0,100000)}")
                flag = False

            else:

                tarjetaDedito = (input("Ingrese su tarjeta de credito: "))
                while bool(patron.fullmatch(tarjetaDedito)) == False: #valida la expresion regular de la linea 119
                    print("no es valido")
                    tarjetaDedito = input("Ingrese su tarjeta de credito: ")
                cvv = int(input("Ingrese el codigo de seguridad: ")) 
                while cvv < 100 or cvv >999: #valida codigo de seguridad
                    print ("No es valido")
                    cvv = int(input("Ingrese el codigo de seguridad: ")) 
                usuarios[usuarioActivo]["saldo"]+=cuanto_saldo  
                print ("Su compra ah sido exitosa")
                print(f"Se le acredito U$D {cuanto_saldo}, numero de orden {random.randint(0,100000)}")
                flag = False
    except Exception as e:
        print("Error inesperado al cargar saldo:", e)

def iniciarSesion():
    try:
        print("inicio de Sesion: ")
        usuarioIngresado = input("ingrese su usuario: ")
        contraseñaIngresada = input("ingrese su contraseña: ")
        
        usuarioActivo= 0 
        coincidencia = False
        indice = len(usuarios)

        for i in range (indice):
            if usuarioIngresado == usuarios[i]["user"]:
                if contraseñaIngresada == usuarios[i]["password"]:
                    usuarioActivo = i
                    coincidencia = True
        
        if coincidencia == True:
            print(f"bienvenido {usuarios[usuarioActivo]["user"]} ")

        else:
            print("alguno de los datos es incorrecto")
            usuarioActivo = None
    
    except Exception as e:
        print("Error inesperado al iniciar sesión:", e)
        usuarioActivo = None
        
    return usuarioActivo

def comprarJuegos(usuarioActivo):
   
    try:
        flag = 0
        while flag != 1:
            juegoElegido = mostrarJuegos()

            confirmacion = int(input("Ingrese 1 para comprar, 2 para volver a ver la lista, 3 para salir: "))
            while confirmacion not in [1, 2, 3]:#valida el rango propuesto
                print("Seleccione una opción válida")
                confirmacion = int(input("Ingrese 1 para comprar, 2 para volver a ver la lista, 3 para salir: "))

            if confirmacion == 1:
                print("Aguarde un momento, chequeando su saldo")
                precio = videojuegos[juegoElegido]["precio"]

                usar_codigo = input("¿Tiene un código de descuento? (s/n): ").lower()
                if usar_codigo == "s":
                    codigo = input("Ingrese el código: ").upper()
                    if codigo in codigos_descuento:
                        descuento = codigos_descuento[codigo]#valida  si existe el codigo de descuento 
                        precio_final = round(precio * (1 - descuento), 2)
                        print(f"Código válido. Precio con descuento: {precio_final}")
                    else:
                        print("Código inválido. Se aplicará el precio normal")
                        precio_final = precio
                else:
                    precio_final = precio

                if usuarios[usuarioActivo]["saldo"] >= precio_final:
                    print("Felicitaciones, compraste un juego")
                    juego = videojuegos[juegoElegido].copy()
                    juego["precioPagado"] = precio_final
                    juego["fechaCompra"] = time.strftime("%Y-%m-%d")#mediante libreria time guarda el tiempo de compra 
                    usuarios[usuarioActivo]["juegos"].append(juego)
                    usuarios[usuarioActivo]["saldo"] -= precio_final #descuenta el preciodel juego
                    flag = 1
                else:
                    print("Lo sentimos, su saldo no es suficiente")

            elif confirmacion == 2:
                print("Volviendo a la lista de juegos")

            else:
                print("Saliendo")
                flag = 1
    except Exception as e:
        print("Error inesperado al comprar juegos:", e)


def crearNotificacion(activo,destino,tipo):
    
    if tipo == "amistad":
        mensaje =f"{usuarios[activo]["user"]} te ha enviado una solicitud de amistad"
    elif tipo == "biblioteca":
        mensaje = f"{usuarios[activo]["user"]}quiere compartir bibliotecas contigo"
    else:
        mensaje = f"{usuarios[activo["user"]]} te ha regalado un juego"

    notificacion = {
        "contenido":mensaje,
        "remitente": activo,
        "visto" : False,
        "tipo": tipo
    }
    usuarios[destino]["notificaciones"].append(notificacion)

def verNotificaciones(usuarioActivo):
    notificacionesNoVistas = list(filter(lambda x: x["visto"] == False, usuarios[usuarioActivo]["notificaciones"]))

    for notificacion in notificacionesNoVistas:
        indiceRemitente = notificacion["remitente"]
        if notificacion["tipo"] == "amistad":
            print(notificacion["contenido"])
            eleccion = input("Escribi Y para aceptar o N para rechazar: ")
            if eleccion.lower() == "y":
                usuarios[usuarioActivo]["amigos"].append(usuarios[indiceRemitente]["user"])
                usuarios[indiceRemitente]["amigos"].append(usuarios[usuarioActivo]["user"])
                print("Ahora", usuarios[usuarioActivo]['user'], "y", usuarios[indiceRemitente]['user'], "son amigos.")

        elif notificacion["tipo"] == "biblioteca":
            print(notificacion["contenido"])
            eleccion = input("Escribi Y para aceptar o N para rechazar: ")
            if eleccion.lower() == "y":
                juegosFusionados = usuarios[usuarioActivo]["juegos"] + usuarios[indiceRemitente]["juegos"]
                juegosFusionadosClear = []
                for juego in juegosFusionados:
                    if juego not in juegosFusionadosClear:
                        juegosFusionadosClear.append(juego)
                usuarios[usuarioActivo]["juegosBiblioteca"] = juegosFusionadosClear
                usuarios[indiceRemitente]["juegosBiblioteca"] = juegosFusionadosClear
                print("Bibliotecas de", usuarios[usuarioActivo]['user'], "y", usuarios[indiceRemitente]['user'], "fusionadas.")
        else:
            
            notificacion["visto"] = True



def enviarNotificacion(activo,tipo):
    busqueda = input("a que usuario desea enviar la notificacion?")
    usuarioRemitente = list(filter(lambda x : x["user"]== busqueda,usuarios))
    
    if len(usuarioRemitente) != 0:
        crearNotificacion(activo,usuarioRemitente[0]["id"],tipo)
    else:
        print("usuario no encontrado")

def reembolsarJuego(usuarioActivo):
    try:
        if not usuarios[usuarioActivo]["juegos"]:
            print("No tenés juegos comprados para reembolsar.")

        else:   

            print("Tus juegos comprados:")
            for i in range(len(usuarios[usuarioActivo]["juegos"])):
                juego = usuarios[usuarioActivo]["juegos"][i]
                print(f"{i}) {juego['nombre']} (Comprado el {juego['fechaCompra']})")

            indice = int(input("Seleccioná el número del juego que querés reembolsar o -1 para salir: "))
            while indice not in range(-1,len(usuarios[usuarioActivo]["juegos"])):
                print("Selección inválida")
                indice = int(input("Seleccioná el número del juego que querés reembolsar o -1 para salir: "))

            if indice== -1:
                print("saliendo...")
            else:
                juego = usuarios[usuarioActivo]["juegos"][indice]
                fecha_actual = time.strptime(time.strftime("%Y-%m-%d"), "%Y-%m-%d")
                fecha_compra = time.strptime(juego["fechaCompra"], "%Y-%m-%d")
                segundos_actual = time.mktime(fecha_actual)
                segundos_compra = time.mktime(fecha_compra)
                diferencia = abs(segundos_actual - segundos_compra)

                if diferencia <= 3 * 24 * 3600:
                    usuarios[usuarioActivo]["saldo"] += juego["precioPagado"]
                    usuarios[usuarioActivo]["juegos"].pop(indice)
                    print(f"Se reembolsó el juego '{juego['nombre']}'. Se acreditaron U$D {juego['precioPagado']} en tu cuenta.")
                else:
                    print(f"No se puede reembolsar '{juego['nombre']}' porque ya pasaron más de 3 días desde la compra.")
    except Exception as e:
        print("Error inesperado al reembolsar juego:", e)

#funciones para usuario admin
def buscarUsuario():
    try:
        ingreso=int(input("ingrese 1 para continuar, o -1 para salir:) "))
        while ingreso !=-1:
            usuarioABuscar=input("ingrese el nombre del usuario a buscar:")
            coincidencia=False
            indice=None
            

            for i in range(len(usuarios)):
                if usuarioABuscar==usuarios[i]["user"]:
                    coincidencia= True
                    indice=i
                    usuario=usuarios[i]["user"]

                    if coincidencia==True:
                        print(usuarios[indice])#consultar como hacer para poder usar el indice para printear la info 
                        
                else:
                    print("usuario no encontrado")
    except Exception as e:
        print("Error inesperado al buscar usuario:", e)
    
    return usuario


def eliminarUsuarios():
    try:
        usuarioABuscar=input("ingrese el nombre del usuario a buscar:")
        coincidencia=False
        indice=None

        for i in range(len(usuarios)):
            if usuarioABuscar==usuarios[i]["user"]:
                coincidencia= True
                indice=i
            
        if coincidencia==True:
            print("desea eliminar el usuario?")
            confirmacion=int(input("ingrese 1 para confirmar, 2 para volver atras: "))
            if confirmacion==1:
                usuarios.pop(indice)
        else:
            print("usuario no encontrado")
    except Exception as e:
        print("Error inesperado al eliminar usuario:", e)

def agregarJuegosAbiblioteca():
    try:
        juego=input("ingrese el nombre del juego que desea agregar a la biblioteca: ")
        for i in range(len(videojuegos)):
            if juego == videojuegos[i]["nombre"]:
                coincidenciaJuego= True
                indice=i
        if coincidenciaJuego==False:
            juegoAAgegar={
                "id": len(videojuegos),
                "nombre": juego,
                "comania": input("ingrese la compañia del juego: "),
                "precio": float(input("ingrese el precio del juego: ")),
                "trofeos_totales": int(input("ingrese la cantidad de trofeos totales del juego: ")),
                "descripcion": input("ingrese la descripcion del juego: "),
                "duracion_horas": int(input("ingrese la duracion en horas del juego: "))
                
            }
            videojuegos.append(juegoAAgegar)
            
        else:
            print("ese juego ya se encuentra en la biblioteca")
    except Exception as e:
        print("Error inesperado al agregar juego a biblioteca:", e)

def agregarJuegoAUsuario():
    try:
        usuarioABuscar=input("ingrese el nombre del usuario a buscar:")
        coincidenciaUsuario=False
        indice=None

        for i in range(len(usuarios)):
            if usuarioABuscar==usuarios[i]["user"]:
                coincidenciaUsuario= True
                indice=i
                usuario=usuarios[i]["user"]

        juegoABuscar=input("ingrese el nombre del juego que desea agregarle a este usuario: ")
        for i in range(len(videojuegos)):
            if juegoABuscar == videojuegos[i]["nombre"]:
                coincidenciaJuego= True
                indice=i

        if coincidenciaJuego==True and juegoABuscar not in usuario["juegos"]:
            usuarios.append(juegoABuscar["juegos"])

        else:
            print("ese juego no puede ser regalado a ese usuario :(")

    except Exception as e:
        print("Error inesperado al agregar juego a usuario:", e)

def cambiarPassword(usuarioActivo):
    try:
        nueva = input("Nueva contraseña (mínimo 8): ")
        repetir = input("Repetir contraseña: ")

        if len(nueva) < 8 or nueva != repetir:
            nueva = input("Inválida o no coincide. Nueva contraseña (mínimo 8): ")
        else:
            usuarios[usuarioActivo]["password"] = nueva
    except Exception as e:
        print("Error al cambiar contraseña:", e)

def cambiarNombreUsuario(usuarioActivo):
    try:
        usuario = input("nombre de usuario: ")
        if usuario == "":#validacion basica
            print("El nombre de usuario no puede estar vacío")
            
            
        nombresUsuarios = [usuarios[i]["user"] for i in range(len(usuarios))]

        if usuario in nombresUsuarios:
            print("usuario repetido")#valida que no exista el nuevo nombre
            return False
        else:   
            usuarios[usuarioActivo]["user"] = usuario
            print("Nombre de usuario actualizado exitosamente")
            return True
    except Exception as e:
        print("Error al cambiar nombre de usuario:", e)

def menu_usuario(usuarioActivo):#menu visual 
    global usuarios
    flag = True
    while flag:
        try:
            print("1-Cargar Saldo\n2-Comprar juegos\n3-Rembolso\n4-Enviar solicitud de amistad\n5-Solicitud de biblioteca compartida\n6-Ver notificaciones\n7-Cambiar Nombre De Usuario\n8-Cambiar password\n9-Ver Datos\n10- Cerrar Cesion")
            try:
                opcion = int(input("¿Qué desea seleccionar?: "))
            except ValueError:
                print("Por favor ingrese un número válido")
            while opcion not in [1,2,3,4,5,6,7,8,9,10]:
                print("No es válido, intente otra vez")
                opcion = int(input("¿Qué desea seleccionar?: "))
            if opcion == 1:
                usuarios = list(usuarios)
                cargaSaldo(usuarioActivo)
                usuarios = tuple(usuarios)
            elif opcion == 2:
                usuarios = list(usuarios)
                comprarJuegos(usuarioActivo)
                usuarios = tuple(usuarios)
            elif opcion == 3:
                usuarios = list(usuarios)
                reembolsarJuego(usuarioActivo)
                usuarios = tuple(usuarios)
            elif opcion == 4:
                usuarios = list(usuarios)
                enviarNotificacion(usuarioActivo, "amistad")
                usuarios = tuple(usuarios)
            elif opcion == 5:
                usuarios = list(usuarios)
                enviarNotificacion(usuarioActivo, "biblioteca")
                usuarios = tuple(usuarios)
            elif opcion == 6:
                usuarios = list(usuarios)
                verNotificaciones(usuarioActivo)
                tuple(usuarios)
            elif opcion == 7:
                usuarios = list(usuarios)
                cambiarNombreUsuario(usuarioActivo)
                usuarios = tuple(usuarios)
            elif opcion == 8:
                usuarios = list(usuarios)
                cambiarPassword(usuarioActivo)
                usuarios = tuple(usuarios)
            elif opcion == 9:
                verPerfilUsuario(usuarioActivo)
            else:
                print("Usted cerró sesión")
                flag = False
            print("--------------------------")
        except Exception as e:
            print("Error en el menú:", e)
    

def menu_principal():#menu visual 
    global usuarios
    print("Bienvenid@ a InsertCoin")
    flag = True
    while flag:
        print("--------------------------")
        print("1-Crear un nuevo usuario\n2-Iniciar sesión\n3-Administrador\n4-Salir")
        opcion = int(input("¿Qué desea seleccionar?: "))
        while opcion not in [1,2,3,4]:
            print("Opción no válida, intente otra vez")
            opcion = int(input("¿Qué desea seleccionar?: "))
        if opcion == 1:
            usuarios = list(usuarios)
            crearUsuario()
            usuarios = tuple(usuarios)
            usuarioActivo = iniciarSesion()
            if usuarioActivo is not None:
                menu_usuario(usuarioActivo)
            
        elif opcion == 2:
            usuarioActivo = iniciarSesion()
            if usuarioActivo is not None:
                menu_usuario(usuarioActivo)
        elif opcion ==3:
            clave = input("Ingrese la clave de administrador: ")
            if clave == "adminadmin":
                administrador()
            else:
                print("Contraseña incorrecta.")
        else:
            print("¡Gracias por usar InsertCoin!")
            guardarDatos()
            flag = False

def administrador():#menu visual 
    global usuarios
    flag = True
    while flag:
        print("--------------------------")
        try:
            print("1-Buscar usuarios\n2-Eliminar usuario\n3-Cerrar sesion")
            opcion = int(input ("¿Qué desea seleccionar?:"))
        except ValueError:
            print("ValueError, valor no valido")
        while opcion not in [1,2,3]:
            print("No es válido, intente otra vez")
            opcion = int(input("¿Qué desea seleccionar?: "))
        if opcion ==1:
            buscarUsuario()
        elif opcion ==2:
            usuarios = list(usuarios)
            eliminarUsuarios()
            usuarios = tuple(usuarios)
        else:
            print ("Cerraste sesion")
            flag = False
        


def main():
    global usuarios,videojuegos
    usuarios,videojuegos = cargarDatos()
    usuarios = tuple(usuarios)
    videojuegos = tuple(videojuegos)
    menu_principal()

main()

