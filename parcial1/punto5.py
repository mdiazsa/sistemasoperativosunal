import hashlib
from os import listdir
from os.path import isdir, islink


for direccion in listdir("."):
    if not isdir(direccion) and not islink(direccion):
        try:
            archivo = open(direccion, "rb")
        except IOError as e:
            print(e)
        else:
            data = archivo.read()
            archivo.close()
            print(direccion + ": ")
            h = hashlib.sha1()
            h.update(data)
            try:
                hexdigest = h.hexdigest()
            except TypeError:
                hexdigest = h.hexdigest()

            print("Hash Sha1: " + hexdigest)
