def selectionSort(nlist):
  #Vai analisar apartir de p[0] no sentido anti horário ignorando a última posição
  #[0][1][2][3][4]
  # X [0][1][2][3]
   for fillslot in range(len(nlist)-1,0,-1):
       maxpos=0 # se tornará uma referência a posição[0] futuramente
       #objetivo é pegar uma posição posterior da seguida de p[0]
       #OBS: p[0] zero não foi excluido , somente não fará parte da leitura POR ENQUANTO
       for location in range(1,fillslot+1):
          #[0] [1] [2] [3] [4]
          #     ^   ^   ^   ^
          # se as demais posições tiverem valores maiores que a posição armazenada em p[0] EM TEMPO DE EXECUÇÃO:
           if nlist[location]>nlist[maxpos]:
             #se renovará , exemplo:
             # [9] [3] [1] [0] [4]   
             #  0 > 1   2   3    4
             #     
               maxpos = location #renovando o ponteiro
       #vai ser responsável por renovar os espaços que já foram preenchidos , ou seja , o final em tempo de execução
       temp = nlist[fillslot]
       nlist[fillslot] = nlist[maxpos] # o novo final será um novo começo
       #>>>>>>ATUALIZAÇÃO<<<<<<<<
       nlist[maxpos] = temp #looping
       print(nlist)

nlist = [9,3,1,0,4]
selectionSort(nlist)
print(nlist)



#                   X(LEITURA DO PRIMEIRO FOR)
#      [0] [1] [2] [3]    
#      ______________> salva na variável "temp"
#      ^   ^   ^   ^ 
#  X   !   !   !   !
# [9] [3] [1] [0] [4]   
#  0 > 1   2   3    4 logo será trocado
#      ^   ^   ^    ^ -----> ESSES PONTEIROS SERÃO SALVOS NA VARIÁVEL maxpos
#      X(LEITURA DO SEGUNDO FOR)
