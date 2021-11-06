import socket
import ssl
import asyncio

protocolo = ssl.create_default_context() #Esto se requiere para conectarse con la API ya que usa https
url = "www.buda.com"
puerto = 443

#Ejemplos de funciones que adminte la API

funcion1 = b"GET /api/v2/markets/btc-clp/volume HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"
funcion2 = b"GET /api/v2/markets/btc-clp/ticker HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"
funcion3 = b"GET /api/v2/markets/btc-clp/order_book HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"


async def peticion(ruta):
    socketCliente = protocolo.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=url)
    socketCliente.connect((url, puerto))

    socketCliente.send(ruta)

    mensaje = socketCliente.recv(4096)


    mensaje = mensaje[mensaje.find(b"{"):]
    print("Se recibe del servidor el siguiente .JSON: " + mensaje.decode())



async def main():
    # Se crea un nuevo task por cada peticion que se le hace  la API
    task1 = asyncio.create_task(peticion(funcion1))

    task2 = asyncio.create_task(peticion(funcion2))

    task3 = asyncio.create_task(peticion(funcion3))

    await task3

    print("Fin de la conexión")


asyncio.run(main())
