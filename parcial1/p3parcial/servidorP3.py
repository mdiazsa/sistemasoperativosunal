import socket
import asyncio

ejecucion = True


async def parar():
    entrada = input("Oprima enter para detener el servidor")
    if entrada == "stop":
        return True
    else:
        return False


async def enviar_pagina(contenido):
    socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    puerto = 443
    socketServidor.bind(('localhost', puerto))

    print("Esperando conexión con el cliente... \n")

    socketServidor.listen(1)
    conexion, direccion = socketServidor.accept()
    conexion.send(contenido.encode())

    print("Se ha enviado la página web al cliente")

    conexion.close()
    socketServidor.close()


async def main():
    archivo = open("servidor.html", "r")
    contenido = archivo.read()
    print("El contenido de la pagina es: ")
    print(contenido)

    task = asyncio.create_task(enviar_pagina(contenido))
    stop = asyncio.create_task(parar())
    await stop


asyncio.run(main())
