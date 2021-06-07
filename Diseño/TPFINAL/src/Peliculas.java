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
    ProxyPelicula jurasic = new ProxyPeliculaImpl("Jurasic", "link a la imagen", " Adam Samler", "Yoko, Paul", "Suspenso", "Dinosarios reviven", "Adam, Yoko, Paul", "2018", "170");
    ProxyPelicula museo = new ProxyPeliculaImpl("Museo", "link a la imagen", "Pepe biondi", "Linda, John", "Comedia", "Museo cobra vida", "Linda, John, Museo", "1995", "192");
    ProxyPelicula misterio = new ProxyPeliculaImpl("Misterio", "link a la imagen", "Mirtha Legrand", "Susana, Sandro", "Suspenso", "Historia de una casa embrujada", "Mirtha, Susana, Sandro", "2005", "150");
    ProxyPelicula cars = new ProxyPeliculaImpl("Cars", "link a la imagen", "Johny Deep", "Karina, Sebastian", "Infantil", "Auto rojo corre carreras", "Sebastian, Karina, Auto", "2010", "200");
    ProxyPelicula godzilla = new ProxyPeliculaImpl("Godzilla", "link a la imagen", "Tevez", "Paco, Scarlet", "Terror", "Dinosaurio se come gente", "Paco, Tevez, Bombonera", "1997", "205");
    ProxyPelicula secreto = new ProxyPeliculaImpl("Secreto", "link a la imagen", "Benedetto", "Stalone, Sarah connor", "Drama", "Asesinato y obsesion", "Terminator, Stalone, Tomi Serra", "2016", "140");
    ProxyPelicula anillo = new ProxyPeliculaImpl("Anillo", "link a la imagen", "Maradona", "Gaston, Graciana", "Aventura", "Un señor tiene anillos y lucha", "Graciana, Gaston, mar", "2015", "194");
    ProxyPelicula perro = new ProxyPeliculaImpl("Perro", "link a la imagen", "Moria Casan", "Robin, Batman", "Comedia", "Perro superheroe", "Robin, Batman, ,Moria", "2001", "203");    
    ProxyPelicula gato = new ProxyPeliculaImpl("Gato", "link a la imagen", "Emilio Dissi", "John Tittor, Alfred", "Infantil", "Gato villano se enfrenta a ratas voladoras", "Ratas, Gato, Alfred", "1999", "160");
    ProxyPelicula rana = new ProxyPeliculaImpl("Rana", "link a la imagen", "Bruce Wane", "Pikachu, Sabrina", "Infantil", "Rana aprende karate y vence a los malos", "Ranas, Sabrina, Pikachu", "2004", "132");
    ProxyPelicula foca = new ProxyPeliculaImpl("Foca", "link a la imagen", "Guillermo Schelotto", "Baraka, Scorpion", "Infantil", "Foca tiene que salvar el mundo", "Baraka, Scorpion, Foca", "2007", "126");
    Pelicula titanic1 = new Pelicula(titanic,"link al trailer",10," ");
    Pelicula jurasic1 = new Pelicula(jurasic,"link al trailer",9," ");
    Pelicula museo1 = new Pelicula(museo,"link al trailer",7.7," ");
    Pelicula misterio1 = new Pelicula(misterio,"link al trailer",5.6," ");
    Pelicula cars1 = new Pelicula(cars,"link al trailer",2," ");
    Pelicula godzilla1 = new Pelicula(godzilla,"link al trailer",1," ");
    Pelicula secreto1 = new Pelicula(secreto,"link al trailer",6," ");
    Pelicula anillo1 = new Pelicula(anillo,"link al trailer",2," ");
    Pelicula perro1 = new Pelicula(perro,"link al trailer",3," ");
    Pelicula gato1 = new Pelicula(gato,"link al trailer",8," ");
    Pelicula rana1 = new Pelicula(rana,"link al trailer",4," ");
    Pelicula foca1 = new Pelicula(foca,"link al trailer",1," ");

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
        listaPeliculas.add(rana1);
        listaPeliculas.add(foca1);
    }

    public boolean imprimirPelicula(String titulo){
        boolean flag = false;
        for(Pelicula obj:listaPeliculas){
            if (titulo.equals(obj.getPl().getTitulo().toString())){
                System.out.println(obj.toString());
                flag = true;
            }
        }
        if (flag == false){
            System.out.println("NO SE ENCUENTRA EL TITULO");
        }
        return flag;
    }
    
    public void filtradoDirector(String director){
        for(Pelicula obj:listaPeliculas){
            if (director.equals(obj.getPl().getDirector().toString())){
                System.out.println(obj.toString());
            }
        }
    }
    
    public void filtradoPalabrasClave(String palabras){
        for(Pelicula obj:listaPeliculas){
            if ((obj.getPl().getPalabrasClave().toString()).contains(palabras)){
                System.out.println(obj.toString());
            }
        }
    }

    
    public void CalificarPelicula(String titulo, double calificacion){
        for(Pelicula obj:listaPeliculas){
            if (titulo.equals(obj.getPl().getTitulo().toString())){
                obj.AgregarCalificacion(calificacion);
            }
        }
    }
    
    
    public void AgregarComentario(String titulo, String comentario){
        for(Pelicula obj:listaPeliculas){
            if (titulo.equals(obj.getPl().getTitulo().toString())){
                obj.AgregarComentario(comentario);
            }
        }
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
    
    public void ordenPorGenero(){
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

