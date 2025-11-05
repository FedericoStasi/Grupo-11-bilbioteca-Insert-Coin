import random
import re
from functools import reduce
import time
usuarios = [
    {
        "id": 0,
        "user": "juan123",
        "password": "contraseñajuan",
        "amigos": [],
        "juegos": [],
        "saldo": 1000,
        "notificaciones": []
    },
    {
        "id": 1,
        "user": "maria_gamer",
        "password": "passmaria88",
        "amigos": [],
        "juegos": [],
        "saldo": 0,
        "notificaciones": []
    },
    {
        "id": 2,
        "user": "lucho_ok",
        "password": "lucho2024",
        "amigos": [],
        "juegos": [],
        "saldo": 0,
        "notificaciones": []
    }
]
# usuarios = [

# ]
videojuegos = [
    {
        "id": 0,
        "nombre": "The Legend of Zelda: Breath of the Wild",
        "compania": "Nintendo",
        "precio": 59.99,
        "trofeos_totales": 120,
        "descripcion": "Un juego de mundo abierto donde Link explora Hyrule para derrotar a Ganon.",
        "duracion_horas": 100
    },
    {
        "id": 1,
        "nombre": "God of War Ragnarök",
        "compania": "Santa Monica Studio",
        "precio": 69.99,
        "trofeos_totales": 70,
        "descripcion": "Kratos y Atreus enfrentan a dioses nórdicos en una épica aventura.",
        "duracion_horas": 60
    },
    {
        "id": 2,
        "nombre": "Elden Ring",
        "compania": "FromSoftware",
        "precio": 59.99,
        "trofeos_totales": 120,
        "descripcion": "Un RPG de mundo abierto creado por Hidetaka Miyazaki y George R. R. Martin.",
        "duracion_horas": 120
    },
    {
        "id": 3,
        "nombre": "Minecraft",
        "compania": "Mojang",
        "precio": 29.99,
        "trofeos_totales": 114,
        "descripcion": "Juego de construcción y supervivencia en un mundo de bloques.",
        "duracion_horas": 999
    },
    {
        "id": 4,
        "nombre": "Hollow Knight",
        "compania": "Team Cherry",
        "precio": 14.99,
        "trofeos_totales": 63,
        "descripcion": "Un metroidvania desafiante ambientado en el reino de Hallownest.",
        "duracion_horas": 40
    },
    {
        "id": 5,
        "nombre": "Red Dead Redemption 2",
        "compania": "Rockstar Games",
        "precio": 59.99,
        "trofeos_totales": 51,
        "descripcion": "Una historia épica en el Salvaje Oeste con Arthur Morgan y la banda Van der Linde.",
        "duracion_horas": 90
    },
    {
        "id": 6,
        "nombre": "The Witcher 3: Wild Hunt",
        "compania": "CD Projekt Red",
        "precio": 39.99,
        "trofeos_totales": 78,
        "descripcion": "Geralt de Rivia busca a Ciri en un vasto mundo lleno de monstruos y política.",
        "duracion_horas": 120
    },
    {
        "id": 7,
        "nombre": "Dark Souls III",
        "compania": "FromSoftware",
        "precio": 49.99,
        "trofeos_totales": 43,
        "descripcion": "Acción RPG desafiante en un mundo oscuro y decadente.",
        "duracion_horas": 80
    },
    {
        "id": 8,
        "nombre": "Final Fantasy VII Remake",
        "compania": "Square Enix",
        "precio": 59.99,
        "trofeos_totales": 54,
        "descripcion": "Remake del clásico JRPG con gráficos modernos y combates en tiempo real.",
        "duracion_horas": 50
    },
    {
        "id": 9,
        "nombre": "Persona 5 Royal",
        "compania": "Atlus",
        "precio": 59.99,
        "trofeos_totales": 53,
        "descripcion": "Los Ladrones Fantasma de Corazones luchan contra la corrupción en Tokio.",
        "duracion_horas": 100
    },
    {
        "id": 10,
        "nombre": "Sekiro: Shadows Die Twice",
        "compania": "FromSoftware",
        "precio": 59.99,
        "trofeos_totales": 34,
        "descripcion": "Un shinobi en busca de venganza en un Japón feudal ficticio.",
        "duracion_horas": 50
    },
    {
        "id": 11,
        "nombre": "Cyberpunk 2077",
        "compania": "CD Projekt Red",
        "precio": 59.99,
        "trofeos_totales": 45,
        "descripcion": "Un RPG futurista en Night City lleno de decisiones y acción.",
        "duracion_horas": 70
    },
    {
        "id": 12,
        "nombre": "Super Mario Odyssey",
        "compania": "Nintendo",
        "precio": 59.99,
        "trofeos_totales": 999,
        "descripcion": "Mario viaja por mundos creativos con la ayuda de su gorra Cappy.",
        "duracion_horas": 50
    },
    {
        "id": 13,
        "nombre": "Overwatch 2",
        "compania": "Blizzard Entertainment",
        "precio": 0.00,
        "trofeos_totales": 60,
        "descripcion": "Shooter en equipos de héroes con habilidades únicas.",
        "duracion_horas": 200
    },
    {
        "id": 14,
        "nombre": "Bloodborne",
        "compania": "FromSoftware",
        "precio": 19.99,
        "trofeos_totales": 40,
        "descripcion": "Un RPG de acción gótica ambientado en la ciudad maldita de Yharnam.",
        "duracion_horas": 75
    }
]

codigos_descuento = {
        "DESCUENTO10": 0.10,
        "GAMER20": 0.20,
        "SUPER30": 0.30
    } 

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
        usuarios.append(juego["juegos"])#modificar este append pq esta mal
        
    else:
        print("ese juego no puede ser regalado a ese usuario :(")

#termino de funciones de usuario admin #

def cambiarPassword(usuarioActivo):
    try:
        nueva = input("Nueva contraseña (mínimo 8): ")
        repetir = input("Repetir contraseña: ")

        if len(nueva) < 8 or nueva != repetir:
            nueva = input("Inválida o no coincide. Nueva contraseña (mínimo 8): ")
        else:
            usuarios[usuarioActivo]["password"] = nueva
    except

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


