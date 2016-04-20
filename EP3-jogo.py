import numpy as np
class jogo:
    jogadas=[]
    matriz=np.array([[1,2,3],[4,5,6],[7,8,9]]) 
    def ___init___(self,jogadas,matriz):
        self.matriz=matriz
        self.jogadas=jogadas
        
    def recebe_jogada(self,linha,coluna):  
        if len(self.jogadas) % 2 == 0:
            self.matriz[linha][coluna]=='X'
            return 'X' 
        else:
            self.matriz[linha][coluna]=='O'
            return 'O'
        self.jogadas.append(1) 
            
        
    def verifica_ganhador(self):
        if self.jogadas>4: 
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
        if self.jogadas==9:
            return 0
            

jogo=jogo()

for i in range(0,3):
    for j in range(0,3):
        print(jogo.recebe_jogada(i,j))