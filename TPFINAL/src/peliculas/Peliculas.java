/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package peliculas;

import java.util.*;
import java.lang.*;


/**
 *
 * @author Luciano
 */
public class Peliculas implements Filtrado {
    ArrayList<Pelicula> listaPeliculas = new ArrayList<Pelicula>();
    ProxyPelicula titanic = new ProxyPeliculaImpl("Titanic", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Drama", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    ProxyPelicula jurasic = new ProxyPeliculaImpl("Jurasic", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Suspenso", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    ProxyPelicula museo = new ProxyPeliculaImpl("Museo", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Comedia", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    ProxyPelicula misterio = new ProxyPeliculaImpl("Misterio", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Supenso", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    ProxyPelicula cars = new ProxyPeliculaImpl("Cars", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Infantil", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    ProxyPelicula godzilla = new ProxyPeliculaImpl("Godzilla", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Terror", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    ProxyPelicula secreto = new ProxyPeliculaImpl("Secreto", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Drama", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    ProxyPelicula anillo = new ProxyPeliculaImpl("Anillo", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Aventura", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    ProxyPelicula perro = new ProxyPeliculaImpl("Perro", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Comedia", "Se hunde un barco", "titanic, barco, mar", "1997", "195");    
    ProxyPelicula gato = new ProxyPeliculaImpl("Gato", "link a la imagen", "James Cameron", "Di caprio, Kate Winslet", "Infantil", "Se hunde un barco", "titanic, barco, mar", "1997", "195");
    Pelicula titanic1 = new Pelicula(titanic,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    Pelicula jurasic1 = new Pelicula(jurasic,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    Pelicula museo1 = new Pelicula(museo,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    Pelicula misterio1 = new Pelicula(misterio,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    Pelicula cars1 = new Pelicula(cars,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    Pelicula godzilla1 = new Pelicula(godzilla,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    Pelicula secreto1 = new Pelicula(secreto,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    Pelicula anillo1 = new Pelicula(anillo,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    Pelicula perro1 = new Pelicula(perro,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    Pelicula gato1 = new Pelicula(gato,"link al trailer",0,"Excelente, llore todo el dia. La mejor peli nacional");
    public void lista() {
        listaPeliculas.add(titanic1);
        listaPeliculas.add(jurasic1);
        listaPeliculas.add(museo1);
        listaPeliculas.add(misterio1);
        listaPeliculas.add(cars1);
        listaPeliculas.add(godzilla1);
        listaPeliculas.add(secreto1);
        listaPeliculas.add(anillo1);
        listaPeliculas.add(perro1);
        listaPeliculas.add(gato1);
    }

    public void imprimir(){
        for(ProxyPelicula obj:listaPeliculas)
            System.out.println(obj.toString());  
    }
    
    public void CalificarPelicula(Pelicula pelicula, double calificacion){
        pelicula.AgregarCalificacion(calificacion);
    }
    
    public void AgregarComentario(Pelicula pelicula, String comentario){
        pelicula.AgregarComentario(comentario);
    }
    
    public void top10(){
        Collections.sort(listaPeliculas, new Comparator<Pelicula>() {
        @Override
	public int compare(Pelicula p1, Pelicula p2) {
		// Aqui esta el truco, ahora comparamos p2 con p1 y no al reves como antes
		return new Double(p2.getcalificacionPromedio()).compareTo(new Double(p1.getcalificacionPromedio()));
	}
        });
        for (int i = 0; i < 10; ++i) {
            System.out.println(listaPeliculas.get(i).getPl());
        }       
    }
    
    public void filtradoPorGenero(){
        Collections.sort(listaPeliculas, new Comparator<Pelicula>() {
        @Override
	public int compare(Pelicula p1, Pelicula p2) {
		// Aqui esta el truco, ahora comparamos p2 con p1 y no al reves como antes
		return new String(p1.getPl().getGenero()).compareTo(new String(p2.getPl().getGenero()));
	}
        });
        for (int i = 0; i < listaPeliculas.size(); ++i) {
            System.out.println(listaPeliculas.get(i).getPl());
        }       
    }
    
    
    
    
    
    
    
    
    
}

