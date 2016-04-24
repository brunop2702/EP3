class jogo:
    jogadas=[]
    matriz=[[1,2,3],[4,5,6],[7,8,9]] 
    def ___init___(self,matriz):
        self.matriz=matriz
        
    def recebe_jogada(self,linha,coluna):  
        if len(jogadas) % 2 == 0:
            self.matriz[linha][coluna]='X'
            jogadas.append(1)  
            return 'X' 
        else:
            self.matriz[linha][coluna]='O'
            jogadas.append(1)  
            return 'O' 
            
        
    def verifica_ganhador(self):
        if len(jogadas)>4: 
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
        if len(jogadas)==9:
            return 0
        else:
            return -1
            
jogo=jogo()

for i in range(0,3):
    for j in range(0,3):
        print(jogo.recebe_jogada(i,j)) 
        print(jogo.verifica_ganhador()) 
jogadas=[]