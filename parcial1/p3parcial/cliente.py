import socket
import webbrowser


def abrir_pagina(direccion):
    webbrowser.open_new_tab(direccion)

def descargar_pagina():
    socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    puerto = 443

    socketCliente.connect(('localhost', puerto))

    print("Conexión establecida")
    data = socketCliente.recv(4096)
    data = data.decode()

    pagina = open("descarga.html", "a")
    pagina.write(data)

    socketCliente.close()
    print("El código fuente recibio es: " + data +
          "\n Se guardará este códigoen servidor.html - Cierre de transmisión")
    webbrowser.open_new_tab("descarga.html")

descargar_pagina()
