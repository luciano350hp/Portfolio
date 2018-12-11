package src;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Luciano
 */
 
public class Cliente{
  
    private double TiempoLlegada;
    private double TiempoSalida;

    public double getTiempoLlegada() {
        return TiempoLlegada;
    }

    public void imprimir_TiempoLlegada() {
        System.out.println("El cliente llego al sistema a los: " + this.TiempoLlegada + " Segundos");
    }

    public double getTiempoSalida() {
        return TiempoSalida;
    }

    public void setTiempoSalida(double TiempoSalida) {
        this.TiempoSalida = TiempoSalida;
    }
    public Cliente() {
    }

    public Cliente(double TiempoLlegada) {
        this.TiempoLlegada = TiempoLlegada;
    }


  } 

