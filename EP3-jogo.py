class Jogo:
     
    def __init__(self):
        self.jogadas=[]
        self.matriz=[[1,2,3],[4,5,6],[7,8,9]]
        #self.matriz=matriz
        #self.jogadas=jogadas
        
    def recebe_jogada(self,linha,coluna):  
        if len(self.jogadas) % 2 == 0:
            self.matriz[linha][coluna]='X'
            self.jogadas.append(1)  
            return 'X' 
        else:
            self.matriz[linha][coluna]='O'
            self.jogadas.append(1)  
            return 'O' 
            
        
    def verifica_ganhador(self):
        if len(self.jogadas)>4: 
            if self.matriz[0][0]=='X' and self.matriz [0][1]=='X' and self.matriz[0][2]=='X':
                return 1
            if self.matriz[1][0]=='X' and self.matriz[1][1]=='X' and self.matriz[1][2]=='X':
                return 1
            if self.matriz[2][0]=='X' and self.matriz[2][1]=='X' and self.matriz[2][2]=='X': 
                return 1
            if self.matriz[0][0]=='X' and self.matriz[1][0]=='X' and self.matriz[2][0]=='X':
                return 1
            if self.matriz[0][1]=='X' and self.matriz[1][1]=='X' and self.matriz[2][1]=='X':
                return 1 
            if self.matriz[0][2]=='X' and self.matriz[1][2]=='X' and self.matriz[2][2]=='X':
                return 1
            if self.matriz[0][0]=='X' and self.matriz[1][1]=='X' and self.matriz[2][2]=='X':
                return 1
            if self.matriz[0][2]=='X' and self.matriz[1][1]=='X' and self.matriz[2][0]=='X':
                return 1
            if self.matriz[0][0]=='O' and self.matriz [0][1]=='O' and self.matriz[0][2]=='O':
                return 2
            if self.matriz[1][0]=='O' and self.matriz[1][1]=='O' and self.matriz[1][2]=='O':
                return 2
            if self.matriz[2][0]=='O' and self.matriz[2][1]=='O' and self.matriz[2][2]=='O':
                return 2 
            if self.matriz[0][0]=='O' and self.matriz[1][0]=='O' and self.matriz[2][0]=='O':
                return 2 
            if self.matriz[0][1]=='O' and self.matriz[1][1]=='O' and self.matriz[2][1]=='O':
                return 2
            if self.matriz[0][2]=='O' and self.matriz[1][2]=='O' and self.matriz[2][2]=='O':
                return 2
            if self.matriz[0][0]=='O' and self.matriz[1][1]=='O' and self.matriz[2][2]=='O':
                return 2
            if self.matriz[0][2]=='O' and self.matriz[1][1]=='O' and self.matriz[2][0]=='O':
                return 2
        if len(self.jogadas)==9:
            return 0
        else:
            return -1
    def limpa_jogadas(self):
        if self.verifica_ganhador()==0:
            for i in range(0,3):
                for j in range(0,3):
                    self.matriz[i][j]=''
            return ('empate')
        elif self.verifica_ganhador()==1:
            for i in range(0,3):
                for j in range(0,3):
                    self.matriz[i][j]=''
            return ('Jogador X ganhou')
        elif self.verifica_ganhador()==2:
            for i in range(0,3):
                for j in range(0,3):
                    self.matriz[i][j]=''
            return ('Jogador O ganhou')
            
            
jogo=Jogo()

for i in range(0,3):
    for j in range(0,3):
        print(jogo.recebe_jogada(i,j)) 
        print(jogo.verifica_ganhador())
        print(jogo.matriz) 
        print(jogo.limpa_jogadas())
print(jogo.jogadas)
print(jogo.matriz)