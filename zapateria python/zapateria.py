
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



### muestra el producto 
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
    

### actualiza el precio 

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


### agrega clientes 
def agregar_cliente ():
    while(True):
        print("")
        print("verificador de rut: ")
        print("")
        cursor = conexion.cursor()
        rut_cliente = input("ingrese rut del cliente: ")
        nombre = input("ingrese nombre del cliente: ")
        cursor.execute("SELECT COUNT(*) FROM cliente  WHERE rut_cliente = '{}';".format(rut_cliente.lower().strip()))
        

        resultado = cursor.fetchall()
        conexion.commit()
        
         
        if (resultado[0][0]== 0): 
        
            print("--------------------------------")
            print("Cliente Agregado Con Exito")
            cursor.execute("insert into cliente(rut_cliente, nombre) values ('{}', '{}');".format(rut_cliente , nombre))
            break     
            
        
        else:

            print("")
            print("Datos Ya Existentes ")
            break 
    

### agrega factura 
def agregar_factura():
    print("")
    print(" Factura ")
    print("")
    cursor = conexion.cursor()
    cliente_id_fk = int(input("ingrese id del cliente: "))
    cursor.execute("insert into factura(cliente_id_fk, fecha_venta) values ('{}', now());".format(cliente_id_fk))
    conexion.commit()

    print("-------------------------------")
    print("Factura Ingresada Correctamente")
    print("-------------------------------")

### arreglar descuento en stock
### agrega detalle  
def agregar_detalle():
    print("")
    print(" Detalle De la Venta")
    print("")



    cursor = conexion.cursor()
    factura_id_fk = int(input("ingrese id de la factura: "))
    producto_id_fk = int(input("ingrese el id del producto: "))
    cantidad = int(input("ingrese cantidad del producto: "))
    
    sql_2 = "SELECT precio FROM producto WHERE id_producto = " + str(producto_id_fk)
    cursor.execute(sql_2)
    rs = cursor.fetchall()
   
    total = int(rs[0][0]) * cantidad 
    conexion.commit()

    if(total != 0):
        sql_1 = "INSERT INTO detalle VALUES(null, "+str(factura_id_fk) +" ,"+ str(producto_id_fk) +", "+str(cantidad) +", "+ str(total) +") "
        cursor.execute(sql_1)
        

        sql_4 = "SELECT stock FROM producto WHERE id_producto = " + str(producto_id_fk)
        cursor.execute(sql_4)
        rs = cursor.fetchall()
        nuevo_stock = rs[0][0] - cantidad

        if nuevo_stock > 0:


            sql_5 = "update producto set stock = "+ str(nuevo_stock) +" where id_producto = "+ str(producto_id_fk) +""


            cursor.execute(sql_5)
            conexion.commit()

            print("--------------------------------")
            print("Detalle Ingresado Correctamente ")
            print("--------------------------------")



    else:
        print("--------------------------------")
        print(" stock insuficiente o producto no existente")
        print("--------------------------------")
            

#######################

def actualizar_pago():

    cursor = conexion.cursor()
    precio = int(input("ingrese estado de pago: "))
    id_producto = int(input("ingrese id de factura: "))
    cursor.execute("update factura set estado_pago = '{}' where id_factura = '{}' ".format(precio, id_producto))
    print("--------------------------------")
    print("producto facturado Correctamente")
    print("--------------------------------")
    conexion.commit()






### muestra cliente 
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
    print("-------------------")
    print("factura")
    print("-------------------")
    cursor = conexion.cursor() # establece la conexion

    cursor.execute("SELECT * from factura")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados:
        print("")
        print("------------------------------")
        print(recorrer [0], end =": () - id cliente: "),  print(recorrer[1], end = " () - fecha de venta: ") ,  print(recorrer[2], end = " () - Estado de pago: "), print(recorrer[3], end =" ") 
        print("")


def mostrar_detalle():
    cursor = conexion.cursor() # establece la conexion
    cursor.execute("SELECT * from detalle")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados: # recorre los datos ordenadamente y no en una sola linea 
        print("")
        print(recorrer [0], end=": () - id Factura: ") , print(recorrer [1],  end=" () - id Producto : " ) , print(recorrer [2], end="() - Cantidad: ") ,print(recorrer [3], end="() - Precio Total: ") , print(recorrer [4], end=" ") 
        print("")



def  factura_actualizada():
    
    cursor = conexion.cursor() # establece la conexion
    cursor.execute("SELECT * from factura_pagada")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados: # recorre los datos ordenadamente y no en una sola linea 
        print("")
        print(recorrer [0], end=": () - id Factura: ") , print(recorrer [1], end=" () - fecha_venta: ") ,print(recorrer [2], end=" ") 
        print("")
    

def total_venta():

    cursor = conexion.cursor() # establece la conexion
    cursor.execute("select SUM(precio_total)FROM detalle")
    resultados = cursor.fetchall()
    conexion.commit()
    for recorrer in resultados: # recorre los datos ordenadamente y no en una sola linea 
        print("------------")
        print("Precio Total")
        print("------------")
        print(recorrer [0])
        
    


def mostrar_stock():
    print("")
    print("------------------")
    print("stock Del Producto")
    print("------------------")
    print("")

    cursor = conexion.cursor()
    _id_producto = int(input("Ingrese Id Del Producto: "))
    cursor.execute("select stock_disponiblee({})".format(str(_id_producto)))
    rs = cursor.fetchone() # entrega tupla 
    print(rs[0])
    print("--------------------------------")
    print(" stock Correctamente")
    print("--------------------------------")
    conexion.commit()


 
    


def vender_producto():

    while(True):
        print("")
        print("1 - Ingresar cliente")
        print("2 - ingresar factura")
        print("3 - ingresar detalle")
        print("4 - Actualizar pago del cliente")
        print("")
        print("5 - mostrar clientes")
        print("6 - mostrar facturas")
        print("7 - mostrar detalles de venta")
        print("8 - Mostrar facturas Pagadas")
        print("")
        print("9 - Total Ventas")
        print("10 - Stock Disponible")
        print("")
        print("0 - Salir")

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
            actualizar_pago()

        elif (ingreso3 == "5"):
            mostrar_cliente()
           
        
        elif (ingreso3 == "6"):
            mostrar_factura()

        elif (ingreso3 == "7"): 
            mostrar_detalle()
            

        elif (ingreso3 == "8"):
            factura_actualizada()
            
        
        elif (ingreso3 == "9"):
            total_venta()
        
        elif (ingreso3 == "10"):
            mostrar_stock()

        elif (ingreso3 == "0"):
            exit()

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

        resultado = cursor.fetchall()

        if (resultado[0][0] == 0): #verifica el usuario y la contraseña 
        
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













