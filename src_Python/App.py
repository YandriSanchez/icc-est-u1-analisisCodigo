import matplotlib.pyplot as plt
from Benchmarking import Benchmarking
from MetodosOrdenamiento import MetodosOrdenamiento
from datetime import datetime 

if __name__ == "__main__":
    print("Funciona")
    
    # Instancias
    benchmark = Benchmarking()
    metodos = MetodosOrdenamiento()
    tamanios = [500, 1000, 2000]
    resultados = []
    fecha_hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    
    metodosDic = {
        "burbuja": metodos.sort_Bubble,
        "seleccion": metodos.sort_seleccion
    }
    
    tiempos_by_metodo = {
        "burbuja": [],
        "seleccion": []
    }

    for tam in tamanios:
        arreglo_base = benchmark.build_arreglo(tam)
        
        for nombre, metodo in metodosDic.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)
        
    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")
        tiempos_by_metodo[nombre].append(tiempo)
    
    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    
    #clasificar los tiempos segun los metodos
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker='o')
    
    plt.grid()
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Comparación de Algoritmos de Ordenamiento  "+f"\nYandri Sanchez: {fecha_hora_actual}")
    plt.get_current_fig_manager().set_window_title("Yandri Sanchez - "+fecha_hora_actual)
    plt.legend()
    plt.show()
    
    