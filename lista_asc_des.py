def ordenar_lista(lista,orden):
   
   #ordenar lista
   contador = 0
   for x in range(len(lista)-1):
      for y in range(len(lista)-1):
         if lista[y]>lista[y+1]:
            aux = lista[y]#???
            lista[y] = lista[y+1]
            lista[y+1] = aux
            contador+=1
    
         print("contador: ",contador)
    
         return lista
      



lista_original= [2,3,56,3,2,45,56,3,2,4,34]
print("lista original: ",lista_original)

lista_ordenada= ordenar_lista(lista_original,"ASC")
print("lista ordenada", lista_ordenada)

