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

    public SistemaMM1(double TiempoGlobal, Cola cola1, double tiempoProximoCliente, double tiempoFinServicio, Servidor servidor) {
        this.TiempoGlobal = TiempoGlobal;
        this.cola1 = cola1;
        this.tiempoProximoCliente = exponencial(1);
        this.tiempoFinServicio = exponencial(1);
        this.servidor = servidor;
    }
    
    public static double exponencial(double lambdaa){
      double num = (double)(Math.random()*1);
      num = - (1/lambdaa) * (Math.log(1-num));
      return num;
    }
    
    public void procesar() {
        while(true) {
            Cliente c = new Cliente();
            if (tiempoProximoCliente < tiempoFinServicio) {
              TiempoGlobal = tiempoProximoCliente;
              Cliente c1 = new Cliente(TiempoGlobal);
              cola1.encolar(c1);
            } else {
              TiempoGlobal = tiempoFinServicio;
              servidor.finalizarAtencion();
              c.setTiempoSalida(TiempoGlobal);
            }
            if (servidor.ocioso() && !cola1.empty()) {
                cola1.desencolar();
                tiempoFinServicio = TiempoGlobal + servidor.atender(c);
            }
            this.tiempoProximoCliente = exponencial(1);
            this.tiempoFinServicio = exponencial(1);
          
        }
    }
    
    
}
