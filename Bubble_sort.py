def bubblesort(array):
  #Tamanho vetor padrão
  for i in range(len(array)):
    #Leitura sequencial começando pela última posição do meu vetor
      for j in range(0,len(array)-1):
        #Leitura de "trás para frente"
        #Se a posição do meu último valor for menor que a penúltima então:
        if array[j]>array[j+1]:
          #aux será responsável por salvar as últimas posições em tempo de execução
          aux = array[j]
          #atualizando as novas posições em tempo real
          array[j] = array[j+1]
          #renovando as próximas "últimas posições"(valores maiores são alocados para as últimas posições)
          array[j+1] = aux #looping
          
data=[]
for i in range(5):
  num=int(input('-->'))
  data.append(num)
bubblesort(data)
print(data)