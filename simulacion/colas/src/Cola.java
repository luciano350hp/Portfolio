
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
public class Cola {
    ArrayList<Cliente> cola1 = new ArrayList<Cliente>();
    
    public void  encolar(Cliente c){
      cola1.add(c);
      System.out.println("Se encolo un cliente");
    }
    
    public void desencolar(){
      cola1.remove(0);
      System.out.println("Se desencolo un cliente");
      }
    
    public boolean empty(){
        System.out.println("La cola esta vacia");
        return (cola1.isEmpty());
    }
}
