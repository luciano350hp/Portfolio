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
    private final double mu;
    Cliente[ ] servidor1 = new Cliente[1];

    public Servidor(double mu) {
        this.mu = SistemaMM1.exponencial(mu);
    }

    public double atender(Cliente cliente1){
        servidor1[0] = cliente1;
        System.out.println("El servidor atendera al Cliente en: " + this.mu + " ¡Segundos");
        return (this.mu);
    }

    public void finalizarAtencion(){
        servidor1[0] = null;
        System.out.println("Se finalizo la atencion del cliente");
    }
    
    public boolean ocioso(){
        System.out.println("El servidor esta ocioso");
        return servidor1[0]== null;
    }
}
