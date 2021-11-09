import socket
import asyncio
import os


async def seleccionFichero():

    os.chdir(r"C:\Users\Manuel\Documents")

    with os.scandir(os.getcwd()) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
    num = 1
    for i in ficheros:
        print(str(num) + ") " + i)
        num += 1
    entrada = int(input("Seleccione el fichero que desea descargar: "))
    return ficheros[entrada - 1]


async def enviar_informacion(direccion):
    socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    puerto = 123
    socketCliente.connect(('localhost', puerto))

    try:
        socketCliente.send(direccion.encode())
    finally:
        socketCliente.close()


async def recibir_fichero():
    socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 123
    socketCliente.connect(('localhost', port))

    try:
        data = socketCliente.recv(8192)
        print(data.decode())
    finally:
        socketCliente.close()




async def main():


    direccion = await seleccionFichero()
    await enviar_informacion(direccion)
    await asyncio.sleep(2)
    await recibir_fichero()

asyncio.run(main())
