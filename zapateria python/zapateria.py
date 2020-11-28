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



    ##cursor.execute("call agregar_producto('()','{}','{}','{}')").format(_nombre,_precio,_talla, _categoria_id_fk)
    

    conexion.commit()


def mostrar_producto():
    pass # deja inactiva la funcion 

def vender_producto():
    pass



def registrar_trabajador():
    print("-----------------------")
    print("Registro de trabajador")
    print("-----------------------")
    cursor = conexion.cursor()
    nombre = input("ingrese su nombre: ")
    contraseña = input("ingrese su contraseña: ") 
    cursor.execute("INSERT INTO trabajador(nombre,contraseña) VALUES ('{}',SHA2('{}',0));".format(nombre,contraseña))
    print("-----------------------------")
    print("usuario creado correctamente")
    print("-----------------------------")
    conexion.commit()
   


# inician sesion los trabajadores 
def ingresar():
    print("-----------------------")
    print("Ingreso")
    print("-----------------------")

    while(True):
        nombre = input("ingrese nombre: ")
        contraseña = input("ingrese contraseña: ")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM trabajador WHERE nombre = '{}' AND contraseña = SHA2('{}',0)".format(nombre,contraseña).lower().strip()) #lower : minuscula y mayuscula, .strip: sirve para los espacios

        rs = cursor.fetchall()

        if (rs[0][0] == 0): #verifica el usuario y la contraseña 
        
            print("                                ")
            print("Usuario o contraseña incorrectas")
            print("                                ")
           ## ingresar()
            


        else:
            while(True):
                print("                  ")
                print("Bienvenido al menu")
                print("                  ")
                print("1 - Ingresar Producto")
                print("2 - Mostrar Producto")
                print("3 - Vender Producto")
                print("0 - Salir")

                ingreso2 = input("ingrese su opcion: ")
                ingreso2 = ingreso2.strip().lower()
                
                if (ingreso2 == "1"):
                    agregar_producto()
                    
                elif(ingreso2 == "2"):
                    mostrar_producto()
                
                elif (ingreso2 == "3"):
                    vender_producto()
                
                elif(ingreso2 == "0"):
                    exit()
                
                elif(ingreso2 != "1" or ingreso2 != "2" or ingreso2 != "3" or ingreso2 != "0"):
                    print("")






                



def inicio_sesion():

    while(True):
        print("1- iniciar sesion")
        print("2- registrarse ")
        print("3- salir del programa")
        ingreso1 = input("ingrese su opcion: ")
        ingreso1 = ingreso1.strip().lower()

        if (ingreso1 == "3"):
            exit()

        elif (ingreso1 == "2"):
            registrar_trabajador()
        
        elif (ingreso1 == "1"):
            ingresar()

        elif(ingreso1 != "1" or ingreso1 != "2" or ingreso1 != "3"):
            print("")

           
inicio_sesion()














