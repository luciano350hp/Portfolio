package src;
import java.util.ArrayList;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Luciano
 */
public class SistemaMM1 {
    private double TiempoGlobal;
    private Cola cola1;
    private double tiempoProximoCliente;
    private double tiempoFinServicio;
    private Servidor servidor;
    private int lambda;
    private int mu;

    public SistemaMM1(int lambda, int mu) {
        this.lambda = lambda;
        this.mu = mu;
        this.TiempoGlobal = 0;
        this.cola1 = new Cola();
        servidor = new Servidor(mu);
    }
    
    public static double exponencial(int lambdaa){
      double num = (double)(Math.random()*1);
      num = - (1/(double)lambdaa) * (Math.log(1-num));
      return num;
    }
    
    public void procesar() {
        while(true) {
            if (servidor.ocioso() || tiempoProximoCliente < tiempoFinServicio) {
              TiempoGlobal = tiempoProximoCliente;
              cola1.imprimir_cantidadClientes();
              Cliente c1 = new Cliente(TiempoGlobal);
              c1.imprimir_TiempoLlegada();
              cola1.encolar(c1);
              cola1.imprimir_cantidadClientes();
              this.tiempoProximoCliente = TiempoGlobal + exponencial(this.lambda);
              System.out.println("El proximo Cliente llegará a los: " + this.tiempoProximoCliente + " Segundos");
            } else {
              TiempoGlobal = tiempoFinServicio;
              System.out.println("El cliente " + (servidor.c.getId()) + " finalizó su atencion a los: " + this.TiempoGlobal +" Segundos");
              servidor.finalizarAtencion();
              cola1.imprimir_cantidadClientes();
            }
            if (servidor.ocioso() && !cola1.empty()) {
              System.out.println("El servidor esta ocioso");
              tiempoFinServicio = TiempoGlobal + servidor.atender(cola1.desencolar());
            }
            
        }
    }
    
    
}
