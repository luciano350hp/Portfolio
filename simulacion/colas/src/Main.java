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
        Cola cola = new Cola();
        Servidor servidor = new Servidor(1);
        SistemaMM1 sistema = new SistemaMM1(0,cola,1,1,servidor);
        sistema.procesar();
    }
  }
