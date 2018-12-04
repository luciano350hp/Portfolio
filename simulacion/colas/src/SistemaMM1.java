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
    
    public void SistemaMM1() {
        cola = new Cola();
        
    }
    
    public void procesar() {
        while(true) {
            if (tiempoProximoCliente < tiempoFinServicio) {
              TiempoGlobal = tiempoProximoCliente;
              Cliente c = new Cliente(TiempoGlobal);
              cola.encolar(c);
            } else {
              TiempoGlobal = tiempoFinServicio;
              Cliente c = servidor.finalizarAtencion();
              c.setearTiempoSalida(TiempoGlobal);
            }
            
            if (servidor.ocioso() && !cola.empty()) {
                Cliente c = cola.desencolar();
                tiempoFinServicio = TiempoGlobal + servidor.atender(c);
            }
        }
    }
    
    
}
