class MetodosOrdenamiento:
    def sort_Bubble(self,arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

        return arreglo
    
    def sort_seleccion(self, array):
        n = len(array)
        for i in range(n-1):
            indice = i
            for j in range(i+1,n):
                if(array[i] > array[indice]):
                    indice = j
            smallnumer = array[indice]
            array[indice] = array[i]
            array[i] = smallnumer