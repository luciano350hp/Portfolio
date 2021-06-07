/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Luciano
 */
package peliculas;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("BIENVENIDOS AL INCAA \n");
        Peliculas peliculas = new Peliculas();
        peliculas.lista();
        System.out.print("BIENVENIDOS AL TOP 10 \n LAS 10 PELICULAS MEJOR CALIFICADAS SON: \n");
        peliculas.top10();
        System.out.print(" \n \n EL LISTADO DE TODAS LAS PELICULAS ORDENADAS POR GENERO ES: \n");
        peliculas.ordenPorGenero();
        System.out.print(" \n \n AQUI PODRA VISUALIZAR LAS PELICULAS POR TITULO, AUTOR O PALABRAS CLAVE \n");
        Scanner dato = new Scanner(System.in);
        int d;
        System.out.print("INGRESE: \n 1 para buscar por titulo:\n 2 para buscar por director:\n 3 para palabras clave: \n 0 para salir ");
        d = dato.nextInt();
        while(d != 0){
            switch (d){
                case (1):
                    System.out.print(" \n \n BIENVENIDOS AL SECTOR CALIFICACIONES Y COMENTARIOS \n");
                    System.out.print(" \n \n A CONTINUACION USTED DEBERA SELECCIONAR UNA PELICULA Y COLOCAR LA CALIFICACION \n (QUE SE PROMEDIARA CON LAS ANTERIORES) Y SUS COMENTARIOS  \n");
                    Scanner sc = new Scanner(System.in);
                    String s;
                    System.out.print("Introduzca TITULO de la pelicula:(s para salir): \n");
                    s = sc.nextLine();
                    while (!s.equals("s")){
                        if (peliculas.imprimirPelicula(s)){
                            Scanner calif = new Scanner(System.in);
                            Double cali;
                            System.out.print("Introduzca la CALIFICACION !CON COMA! (5,6 por ejemplo):(0,0 para salir): \n");
                            cali = calif.nextDouble();
                            if (!cali.equals(0.0)){
                                peliculas.CalificarPelicula(s, cali);
                                System.out.print("Se ha calificado la pelicula \n");
                                peliculas.imprimirPelicula(s);
                            }
                            Scanner comen = new Scanner(System.in);
                            String coment;
                            System.out.print("Introduzca los COMENTARIOS:(s para salir): \n");
                            coment = comen.nextLine();
                            if (!coment.equals("s")){
                                peliculas.AgregarComentario(s, coment);
                                System.out.print("Se ha añadido el comentario \n");
                                peliculas.imprimirPelicula(s);
                            }
                            System.out.print("Introduzca TITULO de la pelicula:(s para salir): \n");
                            s = sc.nextLine();
                            }
                        else{
                            System.out.print("Introduzca TITULO de la pelicula:(s para salir): \n");
                            s = sc.nextLine();
                        }
                    }
                    break;
                case (2):
                    Scanner comen = new Scanner(System.in);
                    String coment;
                    System.out.print(" Introduzca el director: \n");
                    coment = comen.nextLine();
                    peliculas.filtradoDirector(coment);
                    break;
                case (3):
                    Scanner pal = new Scanner(System.in);
                    String palab;
                    System.out.print(" Introduzca palabras clave: \n");
                    palab = pal.nextLine();
                    peliculas.filtradoPalabrasClave(palab);
                    break;
            }
            System.out.print("INGRESE: \n 1 para buscar por titulo:\n 2 para buscar por director:\n 3 para palabras clave: \n 0 para salir ");
            d = dato.nextInt();
        }
           
        }    
}
