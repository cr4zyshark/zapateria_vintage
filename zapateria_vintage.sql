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

CREATE TABLE usuario(
    id_usuario INT AUTO_INCREMENT,
    nombre VARCHAR(30),
    contraseña VARCHAR(30), --editar 

    PRIMARY KEY(id_usuario)


);

-- cliente
CREATE TABLE cliente(
    id_cliente INT AUTO_INCREMENT,
    -- fk
    usuario_id_fk INT,
    -- datos
    rut VARCHAR(30),
    nombre VARCHAR(30),


    PRIMARY KEY(id_cliente),


    FOREIGN KEY(usuario_id_fk) REFERENCES usuario(id_cliente)

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

    -- FK

    categoria_id_fk INT,
  

    PRIMARY KEY(id_producto),

    FOREIGN KEY(categoria_id_fk) REFERENCES categoria(id_categoria)

);

-- detalle de los productos 
CREATE TABLE detalle_producto(
    id_detalle_producto INT AUTO_INCREMENT,
    color VARCHAR(30),
    stock INT,
    talla INT,

-- fk

    producto_id_fk INT,


    PRIMARY KEY(id_detalle_producto),


    FOREIGN KEY(producto_id_fk) REFERENCES producto(id_producto)


);




-- historial venta
CREATE TABLE historial(
    id_historial INT AUTO_INCREMENT,
    fecha_venta VARCHAR(30),
  
    -- fk

    cliente_id_fk INT,
--  categoria_id_fk INT,
    producto_id_fk INT,



    PRIMARY KEY(id_historial),

    FOREIGN KEY (cliente_id_fk) REFERENCES cliente (id_cliente),
--  FOREIGN KEY (categoria_id_fk) REFERENCES categoria (id_categoria),
    FOREIGN KEY (producto_id_fk) REFERENCES producto (id_producto)


);


------------------
-- creacion datos 
------------------




