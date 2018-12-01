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
public interface Filtrado {
    public void top10();
    public boolean imprimirPelicula(String titulo);
    public void ordenPorGenero();
    public void filtradoDirector(String director);
    public void filtradoPalabrasClave(String palabras);
}
