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

public class ProxyPeliculaImpl implements ProxyPelicula{
    private String titulo;
    private String imagen;
    private String director;
    private String actores;
    private String genero;
    private String sinopsis;
    private String palabrasClave;
    private String fechaLazamiento;
    private String duracion;

    public ProxyPeliculaImpl(String titulo, String imagen, String director, String actores, String genero, String sinopsis, String palabrasClave, String fechaLazamiento, String duracion){
        this.titulo = titulo;
        this.imagen = imagen;
        this.director = director;
        this.actores = actores;
        this.genero = genero;
        this.sinopsis = sinopsis;
        this.palabrasClave = palabrasClave;
        this.fechaLazamiento = fechaLazamiento;
        this.duracion = duracion;
    }

    @Override
    public String toString() {
        return "ProxyPelicula{" + "titulo=" + titulo + ", director=" + director + ", actores=" + actores + ", genero=" + genero + ", sinopsis=" + sinopsis + ", palabrasClave=" + palabrasClave + ", fechaLazamiento=" + fechaLazamiento + ", duracion=" + duracion + '}';
    }    
}
