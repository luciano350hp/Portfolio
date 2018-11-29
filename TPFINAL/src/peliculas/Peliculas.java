/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package peliculas;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Luciano
 */
public class Peliculas {
    ArrayList<ProxyPelicula> listaPeliculas = new ArrayList<ProxyPelicula>();
    ProxyPelicula titanic = new ProxyPeliculaImpl("Titanic", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Drama", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    Pelicula titanic1 = new Pelicula(titanic,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    
    public void lista() {
        listaPeliculas.add(titanic);
        listaPeliculas.add(titanic1);
    }
    
    public void imprimir(){
        for(ProxyPelicula obj:listaPeliculas)
            System.out.println(obj.toString());  
    }
    
    public void CalificarPelicula(Pelicula pelicula, double calificacion){
        pelicula.AgregarCalificacion(calificacion);
    }
    
}
