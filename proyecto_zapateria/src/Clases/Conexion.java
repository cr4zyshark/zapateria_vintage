/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Clases;


import java.sql. *; // importar conexion manual
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Jose
 */
public class Conexion {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String usuario = "root";
        String clave = "123";
        String url = "jdbc:mysql://localhost:3306/zapateria";

        Connection con; 
        Statement stmt;
        ResultSet rs;
        
        
        // en caso existan errores en la conexion 
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(Conexion.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        // genere mensajes si hay error en la conexion 
        try {
            con = DriverManager.getConnection(url,usuario,clave);
            stmt = con.createStatement();
            // insert en trabajador 
            stmt.executeUpdate("insert into trabajador values (null,'jose pino', '123' )");
        } catch (SQLException ex) {
            Logger.getLogger(Conexion.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
    }
    
}
