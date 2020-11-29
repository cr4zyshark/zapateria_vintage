# libreria 
import mysql.connector

# conexion a base de datos
conexion = mysql.connector.connect(    
    
    host="localhost",    
    user="root",    
    password="123", 
    database="zapateria")




# se registra a los trabajadores nuevos al sistema 



def agregar_producto():
    print("")
    cursor = conexion.cursor()
    _nombre = input("ingrese nombre del producto: ")
    _precio = int(input("ingrese precio del producto: "))
    _talla  = int(input("ingrese talla del producto: "))
    _categoria_id_fk = int(input("ingrese la id de la categoria: "))
    cursor.callproc("agregar_producto", [_nombre,_precio,_talla,_categoria_id_fk])
    print("--------------------------------")
    print("Producto Ingresado Correctamente")
    print("--------------------------------")
    conexion.commit()


def mostrar_producto():
    cursor = conexion.cursor() # establece la conexion
    cursor.execute("SELECT * from producto")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados:
        print()
        print(recorrer) 
        
   
# muestra la categoria 
def mostrar_categoria():
    cursor = conexion.cursor() # establece la conexion
    cursor.execute("SELECT * from categoria")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados:
        print()
        print(recorrer) 

# elimina los productos 
def eliminar_producto():
    print("")
    cursor = conexion.cursor()
    _id_producto = int(input("Ingrese Id Del Producto: "))
    cursor.callproc("borrar_producto", [_id_producto])
    print("--------------------------------")
    print("Producto Eliminado Correctamente")
    print("--------------------------------")
    conexion.commit()

def vender_producto():
    pass



def registrar_trabajador():
    print("-----------------------")
    print("Registro de trabajador")
    print("-----------------------")
    cursor = conexion.cursor()
    nombre = input("Ingrese su nombre: ")
    contraseña = input("Ingrese su contraseña: ") 
    cursor.execute("INSERT INTO trabajador(nombre,contraseña) VALUES ('{}',SHA2('{}',0));".format(nombre,contraseña))
    print("-----------------------------")
    print("Usuario Creado Correctamente")
    print("-----------------------------")
    conexion.commit()
   


# inician sesion los trabajadores 
def ingresar():
    print("-----------------------")
    print(" Inicio De Sesion ")
    print("-----------------------")

    while(True):
        nombre = input("ingrese nombre: ")
        contraseña = input("ingrese contraseña: ")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM trabajador WHERE nombre = '{}' AND contraseña = SHA2('{}',0)".format(nombre,contraseña).lower().strip()) #lower : minuscula y mayuscula, .strip: sirve para los espacios

        rs = cursor.fetchall()

        if (rs[0][0] == 0): #verifica el usuario y la contraseña 
        
            print("--------------------------------")
            print("Usuario o Contraseña Incorrectas")
            print("--------------------------------")
            print("--------------------------------")
            print("Intente Nuevamente              ")
            print("--------------------------------")
         ## ingresar()
            


        else:
            while(True):
                print("                  ")
                print("Bienvenido al menu")
                print("                  ")
                print("1 - Ingresar Producto")
                print("2 - Mostrar Producto")
                print("3 - Mostrar Categoria")
                print("4 - Eliminar Producto")
                print("5 - Vender Producto")
                print("")
                print("0 - Salir")
                print("")

                ingreso2 = input("ingrese su opcion: ")
                ingreso2 = ingreso2.strip().lower()
                
                if (ingreso2 == "1"):
                    agregar_producto()
                    
                elif(ingreso2 == "2"):
                    mostrar_producto()
                
                elif (ingreso2 == "3"):
                    mostrar_categoria()
                
                elif(ingreso2 == "4"):
                    eliminar_producto()
                   
                elif(ingreso2 == "5"):
                    vender_producto()
                
                elif(ingreso2 == "0"):
                     exit()

                
                elif(ingreso2 != "1" or ingreso2 != "2" or ingreso2 != "3" or ingreso2 != "4" or ingreso2 != "5" or ingreso2 != "0"):
                    print("")






                



def inicio_sesion():

    while(True):
        print("-----------------")
        print("Zapateria Vintage")
        print("-----------------")
        print("1- Iniciar Sesion")
        print("2- Registrarse ")
        print("3- Salir ")
        ingreso1 = input("ingrese su opcion: ")
        ingreso1 = ingreso1.strip().lower() # toma datos en mayuscula y minuscula 

        if (ingreso1 == "3"):
            exit()

        elif (ingreso1 == "2"):
            registrar_trabajador()
        
        elif (ingreso1 == "1"):
            ingresar()

        elif(ingreso1 != "1" or ingreso1 != "2" or ingreso1 != "3"):
            print("")

           
inicio_sesion()














