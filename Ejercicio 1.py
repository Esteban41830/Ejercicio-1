import csv 
class Email:
	__idCuenta = ''
	__dominio = ''
	__tipoDominio = ''
	__clave = 0

	def __init__(self,idcuenta,dominio,tipo,clave):
		self.__idCuenta = idcuenta
		self.__dominio = dominio
		self.__tipoDominio = tipo
		self.__clave = clave 

	def retornaEmail(self):
		return "{}@{}.{}" .format(self.__idCuenta,self.__dominio,self.__tipoDominio)

	def getDominio(self):
		return self.__dominio

	def crearCuenta(self):
		self.__idCuenta = input('Ingrese id: ')
		self.__dominio = input('Ingrese dominio: ')
		self.__tipoDominio = input('Ingrese tipo de dominio: ')
		self.__clave = input('Ingrese clave: ')

	def cambiarClave(self):
		i = 0
		while i == 0:
			clave_actual = input('Ingrese clave actual: ')
			if self.__clave == clave_actual:
				self.__clave = input('Ingrese nueva clave: ')
				i = 1

			else:
				print('No hay coincidencia')



if __name__ == '__main__':

   Nombre = (input('Ingrese su nombre: '))
   idcuenta = (input('Ingrese id: '))
   dominio = (input('Ingrese dominio:  '))
   tipodominio = (input('Ingrese tipo de dominio: '))
   clave = (input('Ingrese calve:  '))

   unaCuenta = Email(idcuenta,dominio,tipodominio,clave)
   print("\nEstimado {} te enviaremos los mensajes a la direccion: {}\n\n".format(Nombre,unaCuenta.retornaEmail()))

   unaCuenta.cambiarClave()

   i = 'no'
   while i == 'no':
   	i = input('¿desea ingresar una cuenta? si o no: ')
   	if i == 'si':
   		nuevaCuenta = Email()
   		nuevaCuenta.crearCuenta()
   		print('Nueva cuenta {}, se registró'.format(nuevaCuenta.retornaEmail()))


   cuentas = []
   archivo = open("Cuentas.csv")
   reader = csv.reader(archivo,delimiter=";")
   for fila in reader:
   	unaCuenta = Email(fila[0],fila[1],fila[2],fila[3])
   	cuentas.append(unaCuenta)
      
   archivo.close()
   
   dom = input("\n\nIngrese el dominio: ")
   repite = 0
   for i in range(10):
       if cuentas[i].getDominio() == dom:
           repite = repite+1


   print("Se repite {} veces".format(repite))


       

