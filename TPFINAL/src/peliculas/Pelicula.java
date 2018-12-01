/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package peliculas;

import java.util.ArrayList;

/**
 *
 * @author Luciano
 */
 

public class Pelicula implements ProxyPelicula{


    private ProxyPelicula pl;
    ArrayList<Double> listaCalificaciones = new ArrayList<Double>();
    private String trailer;
    private double calificacionPromedio;
    private String comentarios;

    @Override
    public String toString() {
        return "Pelicula{" + "pl=" + pl + ", trailer=" + trailer + ", calificacionPromedio=" + calificacionPromedio + ", comentarios=" + comentarios + '}';
    }
    
    @Override
    public String getGenero(){
        return pl.getGenero();
    }
    @Override
    public String getTitulo(){
        return pl.getTitulo();
    }
    
    @Override
    public String getDirector() {
        return pl.getDirector();
    }
    
    @Override
    public String getPalabrasClave() {
        return pl.getPalabrasClave();
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
    
    public void AgregarComentario(String comentario){
        this.comentarios = this.comentarios + " .***. "  + comentario;
    }
    
    public double getcalificacionPromedio(){
          return this.calificacionPromedio;
          }
    
    public ProxyPelicula getPl() {
        return pl;
    }

          
    
        
    
    
}
