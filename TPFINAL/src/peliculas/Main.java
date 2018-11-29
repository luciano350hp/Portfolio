/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package peliculas;

/**
 *
 * @author Luciano
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("BIENVENIDOS AL INCAA");
        Peliculas peliculas = new Peliculas();
        peliculas.lista();
        peliculas.imprimir();
        peliculas.CalificarPelicula(peliculas.titanic1, 2);
        peliculas.imprimir();
        peliculas.CalificarPelicula(peliculas.titanic1, 4);
        peliculas.CalificarPelicula(peliculas.titanic1, 10);
        peliculas.imprimir();

    }
}
