/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.ArrayList;

/**
 *
 * @author Luciano
 */
 
package peliculas;
public class Pelicula implements ProxyPelicula, Comparable<Pelicula> {
    private ProxyPelicula pl;
    ArrayList<Double> listaCalificaciones = new ArrayList<Double>();
    private String trailer;
    private double calificacionPromedio;
    private String comentarios;

    @Override
    public String toString() {
        return "Pelicula{" + "pl=" + pl + ", trailer=" + trailer + ", calificacionPromedio=" + calificacionPromedio + ", comentarios=" + comentarios + '}';
    }

    public Pelicula(ProxyPelicula pl, String trailer, double calificacionPromedio, String comentarios) {
        this.pl = pl;
        this.trailer = trailer;
        this.calificacionPromedio = calificacionPromedio;
        this.comentarios = comentarios;
    }
    
    public void AgregarCalificacion(double calificacion){
        listaCalificaciones.add(calificacion);
        double n = 0;
        for (int i = 0; i < listaCalificaciones.size(); i++) {
            n += Double.parseDouble(listaCalificaciones.get(i).toString());
        }
        double promedio = n/listaCalificaciones.size();
        this.calificacionPromedio = promedio;
    }
    
    public double getcalificacionPromedio(){
          return this.calificacionPromedio;
          }
          
    @Override
    public int compareTo(Pelicula p) {
      if (this.calificacionPromedio < p.calificacionPromedio) {
        return -1;
        }
      if (this.calificacionPromedio > this.calificacionPromedio) {
        return 1;
            }
        return 0;
        }
        
    
    
}
