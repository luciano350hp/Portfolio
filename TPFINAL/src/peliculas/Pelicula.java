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
public class Pelicula implements ProxyPelicula {
    private ProxyPelicula pl;
    private String trailer;
    private float calificacionPromedio;
    private String comentarios;

    @Override
    public String toString() {
        return "Pelicula{" + "pl=" + pl + ", trailer=" + trailer + ", calificacionPromedio=" + calificacionPromedio + ", comentarios=" + comentarios + '}';
    }

    public Pelicula(ProxyPelicula pl, String trailer, float calificacionPromedio, String comentarios) {
        this.pl = pl;
        this.trailer = trailer;
        this.calificacionPromedio = calificacionPromedio;
        this.comentarios = comentarios;
    }
    
}
