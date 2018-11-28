/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Luciano
 */
 
public class Main{
    public static void main(String args[])
    {
        Cliente cliente1 = new Cliente();
        cliente1.imprimir();
        Exponencial expo = new Exponencial(1);
        System.out.println(expo.calcular(1));
    }
  }
