import socket

texto = input("Ingrese el mensaje que desea enviar al cliente: ")

sockete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
puerto = 5066 
sockete.bind(('localhost', puerto)) 

print ("Esperando conexión con el cliente", puerto)

sockete.listen(1)
conexion, direccion =  sockete.accept()
conexion.send(texto.encode()) 

print("Se ha enviado el mensaje: " + texto + "\n Se guardará este mensaje en mensaje.txt - Cierre de transmisión")

conexion.close()
sockete.close()
