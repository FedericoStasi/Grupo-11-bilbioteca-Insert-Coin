import random
usuarios =[

]
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
 
def crearUsuario():
    

    id = random.randint(1000,9999)

    usuario = input("nombre de usuario: ")
    nombresUsuarios = [usuarios[i]["user"] for i in range(len(usuarios))]

    while usuario in nombresUsuarios:
        print("usuario repetido")
        usuario = input("nombre de usuario: ")



    password = input("cree su contraseña con 8 caracteres minimo: ")
    password2 = input("repita su contraseña por favor")

    while len(password)<8 or password2 != password:
        print("contraseñas no coincidentes o con cantidad de caracteres invalida")
        password = input("cree su contraseña con 8 caracteres minimo: ")
        password2 = input("repita su contraseña por favor")

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
        juegoElegido = int(input("selecione un juego: "))
    
    datosJuego(juegoElegido)
    
    return juegoElegido

def datosJuego(id):
    
    print(f"Nombre: {videojuegos[id]["nombre"]}")
    print(f"Desarrollador: {videojuegos[id]["compania"]}")
    print(f"Descripcion: {videojuegos[id]["descripcion"]}")
    print(f"Precio: {videojuegos[id]["precio"]}")
    print(f"Trofeos Totales: {videojuegos[id]["trofeos_totales"]}")
    print(f"Durecion: {videojuegos[id]["duracion_horas"]}")


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
    flag=0
    while flag !=1:
        juegoElegido=mostrarJuegos()
        
        confirmacion=int(input("ingrese 1 si quiere comprar ese juego, 2 si quiere volver a ver la lista de juegos, 3 si desea salir:"))
        while confirmacion>3 or confirmacion<1:
            print("seleccione una opcion valida")
            confirmacion=int(input("ingrese 1 si quiere comprar ese juego, 2 si quiere volver a ver la lista de juegos:"))
        if confirmacion==1:
            print("aguarde un momento, chequeando su saldo :)")
            if usuarios[usuarioActivo]["saldo"]>= videojuegos[juegoElegido]["precio"]:
                print("felicitaciones, compraste un juego")
                usuarios[usuarioActivo]["juegos"].append(videojuegos[juegoElegido])
                usuarios[usuarioActivo]["saldo"]-= videojuegos[juegoElegido]["precio"]
                flag=1
        
            else:
                print("aguarde un momento, chequeando su saldo :)")
                print("lo sentimos, su saldo no es suficiente para comprar el juego :(")
        
        elif confirmacion==2:
            print("volviendo a la lista de juegos...")
        
        else:
            print("saliendo...")
            flag=1

