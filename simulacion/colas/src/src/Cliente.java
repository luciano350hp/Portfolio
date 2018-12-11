package src;

import java.util.concurrent.atomic.AtomicInteger;

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
    private final int id;
    private static final AtomicInteger count = new AtomicInteger(0); 


    public double getTiempoLlegada() {
        return TiempoLlegada;
    }

    public void imprimir_TiempoLlegada() {
        System.out.println("El cliente " + this.getId() + " llegó al sistema a los: " + this.TiempoLlegada + " Segundos");
    }

    public double getTiempoSalida() {
        return TiempoSalida;
    }

    public void setTiempoSalida(double TiempoSalida) {
        this.TiempoSalida = TiempoSalida;
    }

    public int getId() {
        return id;
    }

    public Cliente(double TiempoLlegada) {
        this.TiempoLlegada = TiempoLlegada;
        this.id = count.incrementAndGet(); 
    }


  } 

