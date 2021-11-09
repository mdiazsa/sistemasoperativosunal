import socket
import os
import asyncio

async def recibir_informacion():
    socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    puerto = 123

    socketServidor.bind(('localhost', puerto))
    socketServidor.listen(1)

    print("Esperando conexión con el cliente: ")

    while True:
        conexion, direccion = socketServidor.accept()

        try:
            data = conexion.recv(8192)
            mensaje = data.decode()

        finally:
            conexion.close()

        return mensaje

      
async def enviar_fichero(direccion):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 123

    sock.bind(('localhost', port))
    sock.listen(1)

    while True:
        conexion, dirIp = sock.accept()
        try:
            f = open(direccion, 'rb')
            contenido = f.read()
            conexion.sendall(contenido)
            f.close()
            break
        finally:
            conexion.close()




async def main():

    os.chdir(r"C:\Users\Manuel\Documents")

    nombreArchivo = await recibir_informacion()
    print("El usuario ha elegido el archivo: " + nombreArchivo)
    await enviar_fichero(nombreArchivo)


asyncio.run(main())
