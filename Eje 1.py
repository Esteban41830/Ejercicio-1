import csv
class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __Clave = 0
    
    def __init__(self,idCuenta,dominio,tipoDominio,Clave):
      self.__idCuenta = idCuenta
      self.__dominio = dominio
      self.__tipoDominio = tipoDominio
      self.__Clave = Clave
    
    def retornaEmail(self):
      return "{}@{}{}".format(self.__idCuenta,self.__dominio,self.__tipoDominio)

    def getIDcuenta(self):
      return self.__idCuenta

    def cambiarClave(self):
      i = 0
      while i == 0:
         clave_actual = int(input('Ingrese clave: '))
         if self.__Clave == clave_actual:
            self.__Clave = int(input('Ingrese nueva clave: '))
            i = 1
         else:
            print("No hay coincidencia")

if __name__ == '__main__':
    
   Nombre = (input('Ingrese su nombre: '))
   idcuenta = (input('Ingrese ID: '))
   dominio = (input('Ingrese dominio: '))
   tipodominio = (input('Tipo dominio: '))
   clave = int(input('Ingrese clave: '))
   Cuenta = Email(idcuenta,dominio,tipodominio,clave)
   print("\nEstimado {} te enviaremos los mensajes a la direccion: {}".format(Nombre,Cuenta.retornaEmail()))
   
   Cuenta.cambiarClave()
   
   archivo = open("Cuentas.csv")
   reader = csv.reader(archivo,delimiter=",")
   lista = []
   for fila in reader:
       cuenta = Email(fila[0],fila[1],fila[2],fila[3])
       lista.append(cuenta)
      
   archivo.close()
   
   identificador = input("Ingrese el indentificador: ")
   repite = 0
   for i in range(5):
       if lista[i].getIDcuenta() == identificador:
           repite = repite+1
       
   if repite >= 2:
       print ("\nEl identificador se repite")
   else:
       print("\nEl identificador no se repite")
