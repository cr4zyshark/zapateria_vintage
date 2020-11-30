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
    print("-------------------")
    print("Ingreso De Producto")
    print("-------------------")
    cursor = conexion.cursor()
    _nombre = input("ingrese nombre del producto: ")
    _precio = int(input("ingrese precio del producto: "))
    _talla  = int(input("ingrese talla del producto: "))
    _stock = int(input("ingrese stock del producto: "))
    _categoria_id_fk = int(input("ingrese la id de la categoria: "))
    cursor.callproc("agregar_producto", [_nombre,_precio,_talla,_stock,_categoria_id_fk])
    print("--------------------------------")
    print("Producto Ingresado Correctamente")
    print("--------------------------------")
    conexion.commit()


def mostrar_producto():
    print("-------------------")
    print("Productos")
    print("-------------------")
    cursor = conexion.cursor() # establece la conexion
    cursor.execute("SELECT * from producto")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados:
        print()
        print(recorrer) 
        
   
# muestra la categoria 
def mostrar_categoria():
    print("-------------------")
    print("Categoria")
    print("-------------------")
    cursor = conexion.cursor() # establece la conexion
    cursor.execute("SELECT * from categoria")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados: # recorre los datos ordenadamente y no en una sola linea 
        print()
        print(recorrer) 

# elimina los productos 
def eliminar_producto():
    print("-------------------")
    print("Eliminar Producto")
    print("-------------------")
    cursor = conexion.cursor()
    _id_producto = int(input("Ingrese Id Del Producto: "))
    cursor.callproc("borrar_producto", [_id_producto])
    print("--------------------------------")
    print("Producto Eliminado Correctamente")
    print("--------------------------------")
    conexion.commit()


def actualizar_precio():
    print("------------------")
    print("Actualizar Precio ")
    print("------------------")

    cursor = conexion.cursor()
    precio = int(input("ingrese el precio nuevo: "))
    id_producto = int(input("ingrese id del producto: "))
    cursor.execute("update producto set precio = '{}' where id_producto = '{}' ".format(precio, id_producto))
    print("--------------------------------")
    print("Precio Actualizado Correctamente")
    print("--------------------------------")
    conexion.commit()
    

#historial de precios anteriores
def historial_precio():
    print("-------------------")
    print("Historial")
    print("-------------------")
    cursor = conexion.cursor() # establece la conexion

    cursor.execute("SELECT * from historial_precio")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados:
        print("")
        print("------------------------------")
        print(recorrer [0], end =": () - Producto: "),  print(recorrer[1], end = " () - Precio Anterior: ") ,  print(recorrer[2], end = " () - Fecha De Creacion: "), print(recorrer[3], end =" ") 
        print("")


### aca 
### problema en validacion
def agregar_cliente ():
    while(True):
        print("")
        print("verificador de rut: ")
        print("")
        cursor = conexion.cursor()
        rut_cliente = input("ingrese rut del cliente: ")
        nombre = input("ingrese nombre del cliente: ")
        cursor.execute("SELECT COUNT(*) FROM cliente  WHERE rut_cliente = '{}';".format(rut_cliente).lower().strip())
        

        rs = cursor.fetchall()
        
        ### error verificacion 
        if (rs[0][0]== 0): 
        
            print("--------------------------------")
            print("Este Rut Ya Existe")
            print("--------------------------------")
            print("--------------------------------")
            print("Intente Nuevamente              ")
            print("--------------------------------")
            
            
        
        else:

            print("")
            print("su rut es correcto")
    

### arreglar 
def agregar_factura():
    print("")
    print(" Factura ")
    print("")
    cursor = conexion.cursor()
    cliente_id_fk = int(input("ingrese id del cliente: "))
    cursor.execute("insert into factura(cliente_id_fk, fecha_venta) values ('{}', now());".format(cliente_id_fk))
    conexion.commit()



def agregar_detalle():
    print("")
    print(" Detalle De la Venta")
    print("")
    cursor = conexion.cursor()
    factura_id_fk = int(input("ingrese id de la factura: "))
    producto_id_fk = int(input("ingrese el id del producto: "))
    cantidad = int(input("ingrese cantidad del producto: "))
    cursor.execute("INSERT INTO detalle(factura_id_fk, producto_id_fk, cantidad) VALUES('{}', '{}' , '{}' , (SELECT precio FROM producto WHERE id_producto = producto_id_fk '{}' ) * cantidad '{}');".format(factura_id_fk , producto_id_fk, cantidad ))
    conexion.commit()
    

def mostrar_cliente():
    cursor = conexion.cursor() # establece la conexion
    cursor.execute("SELECT * from cliente")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados: # recorre los datos ordenadamente y no en una sola linea 
        print("")
        print(recorrer [0], end=": () - Rut: ") , print(recorrer [1],  end=" () - Nombre: " ) , print(recorrer [2], end="") 
        print("")



def mostrar_factura():
    pass


def mostrar_detalle():
    pass


## realizar este
def vender_producto():

    while(True):
        print("")
        print("1 - Ingresar cliente")
        print("2 - ingresar factura")
        print("3 - ingresar detalle")
        print("")
        print("4 - mostrar clientes")
        print("5 - mostrar facturas")
        print("6 - mostrar detalles de venta")
        cursor = conexion.cursor()
        ingreso3 = input("ingrese su opcion: ")
        ingreso3 = ingreso3.strip().lower()

        if (ingreso3 == "1"):
            agregar_cliente()

        elif(ingreso3 == "2"):
            agregar_factura()

        elif(ingreso3 == "3"):
            agregar_detalle()

        elif (ingreso3 == "4"):
            mostrar_cliente()

        elif (ingreso3 == "5"):
            mostrar_factura()
        
        elif (ingreso3 == "6"):
            mostrar_detalle()

        else:
            print("")
            print("opcion selecionada incorrecta")
            print("")
            print("intente nuevamente")
            print("")
            
    



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
                print("Opciones/Productos: ")
                print("                  ")
                print("1 - Ingresar Producto")
                print("2 - Mostrar Producto")
                print("3 - Mostrar Categoria")
                print("4 - Eliminar Producto")
                print("5 - Actualizar Precio Del Producto")
                print("6 - Historial Precio Anterior")
                print("")
                print("Opciones/Venta: ")
                print("")
                print("7 - Vender Producto")
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
                    actualizar_precio()

                elif(ingreso2 == "6"):
                    historial_precio()

                elif(ingreso2 == "7"):
                    vender_producto()
                
                elif(ingreso2 == "0"):
                     exit()

                
                elif(ingreso2 != "1" or ingreso2 != "2" or ingreso2 != "3" or ingreso2 != "4" or ingreso2 != "5" or ingreso2 != "6" or ingreso2 != "7" or ingreso2 != "0"):
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

print(inicio_sesion())













