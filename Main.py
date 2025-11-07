import random
import re
from functools import reduce
import time
import os
import json
global usuarios,videojuegos

videojuegos = []
codigos_descuento = {
        "DESCUENTO10": 0.10,
        "GAMER20": 0.20,
        "SUPER30": 0.30
    } 

gift_card = {
    "g0t_50": 50,
    "g1t_5": 5,
    "g0t_100":100 ,
    "g1t_10": 10
}

def aplicarGiftCard(usuarioActivo):#to do,
    usarGiftCard = input("¿desea usar una gift card? (s/n): ").lower()
    if usarGiftCard == "s":
        giftCard = input("Ingrese el codigo de la giftcard:  ").upper()
        if giftCard in gift_card:
            valor = gift_card[gift_card]
            usuarios[usuarioActivo]["saldo"]+=valor
        else:
            print("gift card inexistente.")
            


def cargarDatos():
    rutaUsuarios = os.path.join(os.path.dirname(__file__),"usuarios.json")
    rutaJuegos = os.path.join(os.path.dirname(__file__),"juegos.json")

    try:
        with open(rutaUsuarios,"r") as archivo:
            usuariosObtenidos = json.load(archivo)

        with open(rutaJuegos,"r") as archivo:
            videojuegosObtenidos = json.load(archivo)
            return usuariosObtenidos, videojuegosObtenidos
        
    except Exception as e:
        print("error", e)

def guardarDatos():
    rutaUsuarios = os.path.join(os.path.dirname(__file__), "usuarios.json")
    rutaJuegos = os.path.join(os.path.dirname(__file__), "juegos.json")

    try:
        with open(rutaUsuarios, "w", encoding="utf-8") as archivoUsuarios:
            json.dump(usuarios, archivoUsuarios, indent=4)

        with open(rutaJuegos, "w", encoding="utf-8") as archivoJuegos:
            json.dump(videojuegos, archivoJuegos, indent=4)

        print("Datos guardados correctamente")

    except Exception as e:
        print("Ocurrió un error al guardar los datos:", e)

def crearUsuario():
    if len(usuarios)==0:
        id = 0
    else:
        idMaximo = usuarios[-1]["id"]
        id = idMaximo+1

    usuario = input("nombre de usuario: ")
    nombresUsuarios = [usuarios[i]["user"] for i in range(len(usuarios))]

    if usuario in nombresUsuarios:
        print("usuario repetido")
        return False



    password = input("cree su contraseña con 8 caracteres minimo: ")
    password2 = input("repita su contraseña por favor")

    if len(password)<8 or password2 != password:
        print("contraseñas no coincidentes o con cantidad de caracteres invalida")
        return False

    amigos = []
    juegos = []
    notificaciones = []

    nuevoUsuario ={
        "id": id,
        "user":usuario,
        "password":password,
        "amigos":amigos,
        "juegos":juegos,
        "saldo": 0,
        "notificaciones": notificaciones,
    }

    usuarios.append(nuevoUsuario)

    print("usario creado con exito")

def mostrarJuegos():
    print("estos son los juegos disponibles en nuestra biblioteca, presione cualquiera para conocer su infomracion")
    for i in range(len(videojuegos)):
        print(f"{i}){videojuegos[i]["nombre"]}")
    
    juegoElegido = int(input("selecione un juego: "))
    while juegoElegido <1 or juegoElegido >len(videojuegos)-1:
        print("ingreso invalido")
        return False
    
    datosJuego(juegoElegido)
    
    return juegoElegido

def datosJuego(id):
    
    print(f"Nombre: {videojuegos[id]["nombre"]}")
    print(f"Desarrollador: {videojuegos[id]["compania"]}")
    print(f"Descripcion: {videojuegos[id]["descripcion"]}")
    print(f"Precio: {videojuegos[id]["precio"]}")
    print(f"Trofeos Totales: {videojuegos[id]["trofeos_totales"]}")
    print(f"Durecion: {videojuegos[id]["duracion_horas"]}")

def cargaSaldo (usuarioActivo):
    patron = re.compile(r'^(?:\d{4}[- ]?){3}\d{4}$')

    
    flag = True
    while flag :
        cuanto_saldo = float (input ("Cuanto dinero quiere ingresar? U$D: "))
        if cuanto_saldo < 0 or cuanto_saldo == 0:
            print("No es posible ingrese una cantidad mayor a u$d 0")
            return False
        
        medio_pago = int (input("Que medio de pago desea elegir para finalizar su compra? 1-Mercado pago, 2-Tarjeta de credito, 3-tarjeta de debito: "))
        if medio_pago <1 or medio_pago > 3:
            print("Seleccion no valida intente otra vez")
            return False

        if medio_pago == 1:
            print("El alias es: insertcoin.mp")
            print(f"Se le acredito U$D {cuanto_saldo}, numero de orden {random.randint(0,100000)}")   
            usuarios[usuarioActivo]["saldo"]+=cuanto_saldo  
            flag = False

        
        elif medio_pago == 2:

            tarjetaCredito = input("Ingrese su tarjeta de credito: ")
            if bool(patron.fullmatch(tarjetaCredito)) == False:
                print("No es valido")
                return False
            cvv = int(input("Ingrese el codigo de seguridad: ")) 
            if cvv < 100 or cvv >999:
                print ("No es valido")
                return False
            usuarios[usuarioActivo]["saldo"]+=cuanto_saldo  
            print ("Su compra ah sido exitosa")
            print(f"Se le acredito U$D {cuanto_saldo}, numero de orden {random.randint(0,100000)}")
            flag = False

        else:

            tarjetaDedito = (input("Ingrese su tarjeta de credito: "))
            if bool(patron.fullmatch(tarjetaDedito)) == False:
                print("no es valido")
                return False
            cvv = int(input("Ingrese el codigo de seguridad: ")) 
            if cvv < 100 or cvv >999:
                print ("No es valido")
                return False
            usuarios[usuarioActivo]["saldo"]+=cuanto_saldo  
            print ("Su compra ah sido exitosa")
            print(f"Se le acredito U$D {cuanto_saldo}, numero de orden {random.randint(0,100000)}")
            flag = False

def iniciarSesion():

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
    
    return usuarioActivo

def comprarJuegos(usuarioActivo):
   

    flag = 0
    while flag != 1:
        juegoElegido = mostrarJuegos()

        confirmacion = int(input("Ingrese 1 para comprar, 2 para volver a ver la lista, 3 para salir: "))
        if confirmacion not in [1, 2, 3]:
            print("Seleccione una opción válida")
            return False

        if confirmacion == 1:
            print("Aguarde un momento, chequeando su saldo")
            precio = videojuegos[juegoElegido]["precio"]

            usar_codigo = input("¿Tiene un código de descuento? (s/n): ").lower()
            if usar_codigo == "s":
                codigo = input("Ingrese el código: ").upper()
                if codigo in codigos_descuento:
                    descuento = codigos_descuento[codigo]
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
                juego["fechaCompra"] = time.strftime("%Y-%m-%d")
                usuarios[usuarioActivo]["juegos"].append(juego)
                usuarios[usuarioActivo]["saldo"] -= precio_final
                flag = 1
            else:
                print("Lo sentimos, su saldo no es suficiente")

        elif confirmacion == 2:
            print("Volviendo a la lista de juegos")

        else:
            print("Saliendo")
            flag = 1

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
    if not usuarios[usuarioActivo]["juegos"]:
        print("No tenés juegos comprados para reembolsar.")

    else:   

        print("Tus juegos comprados:")
        for i in range(len(usuarios[usuarioActivo]["juegos"])):
            juego = usuarios[usuarioActivo]["juegos"][i]
            print(f"{i}) {juego['nombre']} (Comprado el {juego['fechaCompra']})")

        indice = int(input("Seleccioná el número del juego que querés reembolsar o -1 para salir: "))
        if indice not in range(-1,len(usuarios[usuarioActivo]["juegos"])):
            print("Selección inválida")
            return False
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

#funciones para usuario admin #
def buscarUsuario():
    ingreso=int(input("ingrese 1 para continuar, o -1 para salir:) "))
    while ingreso !=-1:
        usuarioABuscar=input("ingrese el nombre del producto a buscar:")
        coincidencia=False
        usuarioEncontrado=None
        
        for i in range(len(usuarios)):
            if usuarioABuscar==usuarios[i]["user"]:
                coincidencia= True
                usuarioEncontrado=i
                print(usuarios[usuarioEncontrado])
                accionARealizar=int(input("ingrese: 1 para eliminar usuario, 2 para agregar un juego a un usuario."))
                if accionARealizar == 1:
                    eliminarUsuario=eliminarUsuarios(usuarioEncontrado)
                if accionARealizar ==2:
                    agregarJuegoAlUsuario=agregarJuegoAUsuario(usuarioEncontrado)
            else:
                print("usuario no encontrado")
            
    return usuarioEncontrado #retorna para poder usar el indice en el resto de funciones de amdin

def eliminarUsuarios(usuarioEncontrado):#el parametro es el return de buscar usuario
    print("desea eliminar el usuario?")
    confirmacion=int(input("ingrese 1 para confirmar, 2 para volver atras: "))
    if confirmacion==1:
        usuarios.pop(usuarioEncontrado)
    
def agregarJuegoAUsuario(usuarioEncontrado):#el parametro es el return de buscar usuario
    juego=mostrarJuegos()
    if juego in videojuegos and juego not in usuarios[usuarioEncontrado]["juegos"]:
        usuarios.append(juego["juegos"])
        
    else:
        print("ese juego no puede ser regalado a ese usuario :(")

#termino de funciones de usuario admin #

def cambiarPassword(usuarioActivo):
    nueva = input("Nueva contraseña (mínimo 8): ")
    repetir = input("Repetir contraseña: ")

    if len(nueva) < 8 or nueva != repetir:
        nueva = input("Inválida o no coincide. Nueva contraseña (mínimo 8): ")
    else:
        usuarios[usuarioActivo]["password"] = nueva

def cambiarNombreUsuario(usuarioActivo):
    usuario = input("nombre de usuario: ")
    nombresUsuarios = [usuarios[i]["user"] for i in range(len(usuarios))]

    if usuario in nombresUsuarios:
        print("usuario repetido")
    else:   
        usuarios[usuarioActivo]["user"] = usuario

def menu_usuario(usuarioActivo):
    flag = True
    while flag:
        print("1-Cargar Saldo\n2-Comprar juegos\n3-Rembolso\n4-Enviar solicitud de amistad\n5-Solicitud de biblioteca compartida\n6-Ver notificaciones\n7-Cerrar sesion")
        opcion = int(input("¿Qué desea seleccionar?: "))
        while opcion not in [1,2,3,4,5,6,7]:
            print("No es válido, intente otra vez")
            opcion = int(input("¿Qué desea seleccionar?: "))
        if opcion == 1:
            cargaSaldo(usuarioActivo)
        elif opcion == 2:
            comprarJuegos(usuarioActivo)
        elif opcion == 3:
            reembolsarJuego(usuarioActivo)
        elif opcion == 4:
            enviarNotificacion(usuarioActivo, "amistad")
        elif opcion == 5:
            enviarNotificacion(usuarioActivo, "biblioteca")
        elif opcion == 6:
            verNotificaciones(usuarioActivo)
        else:
            print("Usted cerró sesión")
            flag = False
        print("--------------------------")

def menu_principal():
    print("Bienvenid@ a InsertCoin")
    flag = True
    while flag:
        print("--------------------------")
        print("1-Crear un nuevo usuario\n2-Iniciar sesión\n3-Salir")
        opcion = int(input("¿Qué desea seleccionar?: "))
        while opcion not in [1,2,3]:
            print("Opción no válida, intente otra vez")
            opcion = int(input("¿Qué desea seleccionar?: "))
        if opcion == 1:
            crearUsuario()
            usuarioActivo = iniciarSesion()
            if usuarioActivo is not None:
                menu_usuario(usuarioActivo)
        elif opcion == 2:
            usuarioActivo = iniciarSesion()
            if usuarioActivo is not None:
                menu_usuario(usuarioActivo)
        else:
            print("¡Gracias por usar InsertCoin!")
            flag = False

menu_principal()



