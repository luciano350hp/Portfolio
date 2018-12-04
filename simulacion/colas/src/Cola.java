
import java.util.LinkedList;
import java.util.Queue;

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
    ArrayList<Cliente> cola1 = new ArrayList<CLiente>();
    public void  encolar(Cliente c){
      cola1.add(c);
    }
    
    public void desencolar(Cliente c){
      cola1.remove(0);_
      }
    
    public static double calcular(double lambdaa)
    {
      double num = (double)(Math.random()*1);
      num = - (1/lambdaa) * (Math.log(1-num));
      return num;
    }
    
    
    

}
