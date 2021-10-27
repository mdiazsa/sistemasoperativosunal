import socket


def guardar_mensaje(texto):
    archivo = open("mensaje.txt", "a")
    archivo.write(texto)
    archivo.close()
    archivo = open("mensaje.txt", "r")
    archivo.close()


sockete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
puerto = 5066

sockete.connect(('localhost', puerto))

print("Conexión establecida")
data = sockete.recv(4096)
# data.decode()

sockete.close()
print("El mensaje recibido es: " + data.decode() + "\n Se guardará este mensaje en mensaje.txt - Cierre de transmisión")
guardar_mensaje(data.decode())
