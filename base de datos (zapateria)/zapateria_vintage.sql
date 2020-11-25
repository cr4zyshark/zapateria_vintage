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
    contraseña VARCHAR(64), --editar shar

    PRIMARY KEY(id_trabajador)


);
-----------------------------------------------------------------------

---- crear datos 

INSERT INTO trabajador VALUES(null, "jose pino", "123");
INSERT INTO trabajador VALUES(null, "daniela perez", "234");





-----------------------------------------------------------------------



-- cliente
CREATE TABLE cliente(
    id_cliente INT AUTO_INCREMENT,
    rut_cliente VARCHAR(30),
    nombre VARCHAR(30),


    PRIMARY KEY(id_cliente)


);

-----------------------------------------------------------------------

-- crear datos 

INSERT INTO cliente VALUES(null,"20234173-2", "carlos");




-----------------------------------------------------------------------




-- categoria
CREATE TABLE categoria(
    id_categoria INT AUTO_INCREMENT,
    nombre_categoria VARCHAR(30),
  


    PRIMARY KEY(id_categoria)


);


-----------------------------------------------------------------------

-- crear datos 

INSERT INTO categoria VALUES(null, "zapatos");
INSERT INTO categoria VALUES(null, "zapatillas");




-----------------------------------------------------------------------






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


-----------------------------------------------------------------------

-- crear datos      
                                                          -- categoria
INSERT INTO producto VALUES(null, "adidas revolt", 5000, 39,        2);



-----------------------------------------------------------------------



-- factura 
CREATE TABLE factura(
    id_factura INT AUTO_INCREMENT,
    
    -- fk

    cliente_id_fk INT,
    trabajador_id_fk INT,

    -- datos

    fecha_venta DATETIME,  -- e

    PRIMARY KEY(id_factura),


    FOREIGN KEY(cliente_id_fk) REFERENCES cliente(id_cliente),
    FOREIGN KEY(trabajador_id_fk) REFERENCES trabajador(id_trabajador)


);

-----------------------------------------------------------------------

-- crear datos 
                           -- id_factura(1)   --id_cliente  -- id_trabajador   -- fecha_venta (ahora)
INSERT INTO factura VALUES(null          ,  1         1  ,           1        , NOW());




-----------------------------------------------------------------------




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

-----------------------------------------------------------------------

-- crear datos: 
                         -- id_detalle   -- id_factura   -- id_producto    -- cantidad    -- precio del producto segun la cantidad     -- mismo id_producto       -- misma cantidad
INSERT INTO detalle VALUES(null        ,       1       ,       1         ,    3        , (SELECT precio FROM producto WHERE id_producto =    1)                  *  3);




-----------------------------------------------------------------------





-----------------------------------------------------------------------
----- procedimiento 

--- ingresar producto


DELIMITER //

CREATE PROCEDURE agregar_producto(IN _nombre VARCHAR(30), IN _precio INT, IN _talla INT, IN _categoria_id_fk INT)

BEGIN

    DECLARE condicion INT;

    SET condicion = (SELECT COUNT(*)
    FROM producto
    WHERE nombre_producto = _nombre);

        IF condicion = 0 THEN
        
        INSERT INTO producto VALUES(null,_nombre,_precio,_talla, _categoria_id_fk);
        SELECT'Producto ingresado' AS "mensaje";

        ELSE
            SELECT 'no se puede agregar este producto' AS "mensaje";
            END IF;

    END //

 DELIMITER;


-- agrega productos

call agregar_producto("court", 3000,41,2);


-----------------------------------------------------------------------

-- borrar producto

DELIMITER $$
CREATE PROCEDURE borrar_producto(IN _id_producto INT)

BEGIN

    DECLARE condicion INT;


    SET condicion = (SELECT COUNT(*) FROM producto where id_producto = _id_producto);

        -- error: sigue id automatico
        IF condicion = 1 THEN 
        DELETE FROM producto WHERE id_producto = _id_producto;
        SELECT 'se ha borrado el producto correctamente' AS "mensaje";

        ELSE
        SELECT 'producto no encontrado';
        END IF;

    END $$



DELIMITER ;

-- borrar id 

call borrar_producto(2);



---------------------------------------------------------------------
------- Trigger









-----------------------------------------------------------------------



