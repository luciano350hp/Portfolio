/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Luciano
 */

import java.lang.Math.*;    
public class Exponencial{
    
    private double lambda;
    
    public Exponencial(double lambdaa){
      this.lambda = lambdaa;
     }
     
    public static double calcular(double lambdaa)
    {
      double num = (double)(Math.random()*1);
      num = - (1/lambdaa) * (Math.log(1-num));
      return num;
    }
  } 

