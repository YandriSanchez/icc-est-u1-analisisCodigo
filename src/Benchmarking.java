import java.util.Random;
public class Benchmarking {
    private MetodosOrdenamiento metodosOrdenamiento;
    public Benchmarking() {
        //long inicioMillis = System.currentTimeMillis();//Fecha actual en milisegundos desde epoca referencial de epoch
        //long inicioNano = System.nanoTime();

        //System.out.println(inicioMillis);
        //System.out.println(inicioNano);
        metodosOrdenamiento = new MetodosOrdenamiento();
        int [] arreglo = generaArregloAleatorio(1000000000);
        Runnable tarea = () -> metodosOrdenamiento.burbujaTradicional(arreglo);
        double tiempoNano = medirConNanoTime(tarea);
        System.out.println("Tiempo: " + tiempoNano + " segundos");
        double tiempoMillis = medirConNanoTime(tarea);
        System.out.println("Tiempo: " + tiempoMillis+ " segundos");
    }

    private int[] generaArregloAleatorio(int i){
        //valores entre 0 y 99,999
        Random random = new Random();
        int [] arreglo = new int[i];
        for(int j = 0; j < i; j++){
            arreglo[j] = random.nextInt(i);
        }
        return arreglo;
    }

    //Tiempo usando nanoTime
    public double medirConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin-inicio)/1000000000.0;
    }
    //Tiempo usando currentTimeMillis
    public double medirConCurrenTime(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin-inicio)/1000.0;
    }
    
}