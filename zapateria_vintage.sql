------------------
-- creacion base de datos 
------------------


CREATE DATABASE zapateria;
Use zapateria;



------------------
-- creacion tablas 
------------------



-- login

-- un usuario atiende al cliente 

CREATE TABLE trabajador(
    id_trabajador INT AUTO_INCREMENT,
    nombre VARCHAR(30),
    contraseña VARCHAR(64), 

    PRIMARY KEY(id_trabajador)


);

-- cliente
CREATE TABLE cliente(
    rut_cliente INT AUTO_INCREMENT,
    nombre VARCHAR(30),


    PRIMARY KEY(rut_cliente)


);



-- categoria
CREATE TABLE categoria(
    id_categoria INT AUTO_INCREMENT,
    nombre_categoria VARCHAR(30),
  


    PRIMARY KEY(id_categoria)


);


-- producto
CREATE TABLE producto(
    id_producto INT AUTO_INCREMENT,
    nombre_producto VARCHAR(30),
    precio INT,
    talla INT,

    -- FK
    categoria_id_fk INT,
  

    PRIMARY KEY(id_producto),

    FOREIGN KEY(categoria_id_fk) REFERENCES categoria(id_categoria)

);

-- factura 
CREATE TABLE factura(
    id_factura INT AUTO_INCREMENT,
    
    -- fk

    cliente_id_fk INT,
    trabajador_id_fk INT

    -- datos

    fecha_venta NOW,

    PRIMARY KEY(id_factura),


    FOREIGN KEY(cliente_id_fk) REFERENCES cliente(rut_cliente),
    FOREIGN KEY(trabajador_id_fk) REFERENCES trabajador(id_trabajador)


);


-- detalle de los producto
CREATE TABLE detalle(
    id_detalle INT AUTO_INCREMENT,

    -- fk

    factura_id_fk INT,
    producto_id_fk INT,


    -- datos

    cantidad INT,
    precio_total INT,


    PRIMARY KEY(id_detalle),


    FOREIGN KEY(factura_id_fk) REFERENCES factura(id_factura),
    FOREIGN KEY(producto_id_fk) REFERENCES producto(id_producto)



);



------------------
-- creacion datos 
------------------




