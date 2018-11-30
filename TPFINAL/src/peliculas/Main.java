/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Luciano
 */
package peliculas;

public class Main {
    public static void main(String[] args) {
        System.out.println("BIENVENIDOS AL INCAA");
        Peliculas peliculas = new Peliculas();
        peliculas.lista();
        peliculas.CalificarPelicula(peliculas.titanic1, 2);
        peliculas.CalificarPelicula(peliculas.titanic1, 10);
        peliculas.CalificarPelicula(peliculas.titanic1, 10);
        peliculas.CalificarPelicula(peliculas.jurasic1, 8);
        peliculas.CalificarPelicula(peliculas.museo1, 7);
        peliculas.CalificarPelicula(peliculas.misterio1, 6);
        peliculas.CalificarPelicula(peliculas.cars1, 5.5);
        peliculas.CalificarPelicula(peliculas.godzilla1, 4);
        peliculas.CalificarPelicula(peliculas.secreto1, 3);
        peliculas.CalificarPelicula(peliculas.anillo1, 1);
        peliculas.CalificarPelicula(peliculas.perro1, 6);
        peliculas.CalificarPelicula(peliculas.gato1, 10);
        peliculas.imprimir();

    }
}
