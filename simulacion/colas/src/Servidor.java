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
public class Servidor {
    private final int mu;
    Cliente c ;
    
    public Servidor(int mu) {
        this.mu = mu;
    }

    public double atender(Cliente cliente1){
        c = cliente1;
        double tiempoAtencion = SistemaMM1.exponencial(this.mu);
        System.out.println("El servidor atenderá al Cliente " + c.getId());
        return  tiempoAtencion;
    }

    public void finalizarAtencion(){
        c = null;
    }
    
    public boolean ocioso(){
        return c == null;
    }
}
