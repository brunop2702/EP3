import tkinter as tk 
import EP3jogo

class Tabuleiro:
    def __init__(self):
        self.jogo=EP3jogo.Jogo()
        self.window = tk.Tk()
        self.window.title("Jogo da Velha") 
        self.iniciar()

    def iniciar(self): 
        self.botao1= tk.Button(self.window) 
        self.botao1.configure(command=lambda:self.mudar1()) 
        self.botao1.configure(width= 15, height= 10)  
        self.botao1.grid(column= 0, row= 0) 
    
        self.botao2= tk.Button(self.window)
        self.botao2.configure(command=lambda:self.mudar2()) 
        self.botao2.configure(width= 15, height= 10)
        self.botao2.grid(column= 1, row= 0)
        
        self.botao3= tk.Button(self.window)
        self.botao3.configure(command=lambda:self.mudar3()) 
        self.botao3.configure(width= 15, height= 10) 
        self.botao3.grid(column= 2, row= 0) 
        
        self.botao4= tk.Button(self.window)
        self.botao4.configure(command=lambda:self.mudar4()) 
        self.botao4.configure(width= 15, height= 10)
        self.botao4.grid(column= 0, row= 1)
        
        self.botao5= tk.Button(self.window)
        self.botao5.configure(command=lambda:self.mudar5()) 
        self.botao5.configure(width= 15, height= 10)
        self.botao5.grid(column= 1, row= 1)
        
        self.botao6= tk.Button(self.window)
        self.botao6.configure(command=lambda:self.mudar6())
        self.botao6.configure(width= 15, height= 10)
        self.botao6.grid(column= 2, row= 1)
        
        self.botao7= tk.Button(self.window)
        self.botao7.configure(command=lambda:self.mudar7())
        self.botao7.configure(width= 15, height= 10)
        self.botao7.grid(column= 0, row= 2)
        
        self.botao8= tk.Button(self.window)
        self.botao8.configure(command=lambda:self.mudar8())
        self.botao8.configure(width= 15, height= 10)
        self.botao8.grid(column= 1, row= 2)
        
        self.botao9= tk.Button(self.window)
        self.botao9.configure(command=lambda:self.mudar9())
        self.botao9.configure(width= 15, height= 10)
        self.botao9.grid(column= 2, row= 2)
        
        self.label=tk.Label(self.window) 
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        self.label.grid(column= 0, row= 3)
        
        self.window.mainloop()

    def mudar1(self):
        self.botao1.configure(text=self.jogo.recebe_jogada(0,0))    
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        print(self.jogo.verifica_ganhador())
        if self.jogo.verifica_ganhador()!=(-1):
            self.label.configure(text=self.jogo.limpa_jogadas())
            self.botao1.configure(text=self.jogo.matriz[0][0])
            self.botao2.configure(text=self.jogo.matriz[0][0])
            self.botao3.configure(text=self.jogo.matriz[0][0])
            self.botao4.configure(text=self.jogo.matriz[0][0])
            self.botao5.configure(text=self.jogo.matriz[0][0])
            self.botao6.configure(text=self.jogo.matriz[0][0])
            self.botao7.configure(text=self.jogo.matriz[0][0])
            self.botao8.configure(text=self.jogo.matriz[0][0])
            self.botao9.configure(text=self.jogo.matriz[0][0])
            self.jogo.jogadas=[]
            print(self.jogo.matriz)
        
        
    def mudar2(self):
        self.botao2.configure(text=self.jogo.recebe_jogada(0,1))    
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        print(self.jogo.verifica_ganhador())
        if self.jogo.verifica_ganhador()!=(-1):
            self.label.configure(text=self.jogo.limpa_jogadas())
            self.botao1.configure(text=self.jogo.matriz[0][0])
            self.botao2.configure(text=self.jogo.matriz[0][0])
            self.botao3.configure(text=self.jogo.matriz[0][0])
            self.botao4.configure(text=self.jogo.matriz[0][0])
            self.botao5.configure(text=self.jogo.matriz[0][0])
            self.botao6.configure(text=self.jogo.matriz[0][0])
            self.botao7.configure(text=self.jogo.matriz[0][0])
            self.botao8.configure(text=self.jogo.matriz[0][0])
            self.botao9.configure(text=self.jogo.matriz[0][0])
            self.jogo.jogadas=[]
            print(self.jogo.matriz)
            
    def mudar3(self):
        
        self.botao3.configure(text=self.jogo.recebe_jogada(0,2))    
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        print(self.jogo.verifica_ganhador())
        if self.jogo.verifica_ganhador()!=(-1):
            self.label.configure(text=self.jogo.limpa_jogadas())
            self.botao1.configure(text=self.jogo.matriz[0][0])
            self.botao2.configure(text=self.jogo.matriz[0][0])
            self.botao3.configure(text=self.jogo.matriz[0][0])
            self.botao4.configure(text=self.jogo.matriz[0][0])
            self.botao5.configure(text=self.jogo.matriz[0][0])
            self.botao6.configure(text=self.jogo.matriz[0][0])
            self.botao7.configure(text=self.jogo.matriz[0][0])
            self.botao8.configure(text=self.jogo.matriz[0][0])
            self.botao9.configure(text=self.jogo.matriz[0][0])
            self.jogo.jogadas=[]
            print(self.jogo.matriz)
            
    def mudar4(self):
        self.botao4.configure(text=self.jogo.recebe_jogada(1,0))    
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        print(self.jogo.verifica_ganhador())
        if self.jogo.verifica_ganhador()!=(-1):
            self.label.configure(text=self.jogo.limpa_jogadas())
            self.botao1.configure(text=self.jogo.matriz[0][0])
            self.botao2.configure(text=self.jogo.matriz[0][0])
            self.botao3.configure(text=self.jogo.matriz[0][0])
            self.botao4.configure(text=self.jogo.matriz[0][0])
            self.botao5.configure(text=self.jogo.matriz[0][0])
            self.botao6.configure(text=self.jogo.matriz[0][0])
            self.botao7.configure(text=self.jogo.matriz[0][0])
            self.botao8.configure(text=self.jogo.matriz[0][0])
            self.botao9.configure(text=self.jogo.matriz[0][0])
            self.jogo.jogadas=[]
            print(self.jogo.matriz)
            
    def mudar5(self):
        self.botao5.configure(text=self.jogo.recebe_jogada(1,1))    
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        print(self.jogo.verifica_ganhador())
        if self.jogo.verifica_ganhador()!=(-1):
            self.label.configure(text=self.jogo.limpa_jogadas())
            self.botao1.configure(text=self.jogo.matriz[0][0])
            self.botao2.configure(text=self.jogo.matriz[0][0])
            self.botao3.configure(text=self.jogo.matriz[0][0])
            self.botao4.configure(text=self.jogo.matriz[0][0])
            self.botao5.configure(text=self.jogo.matriz[0][0])
            self.botao6.configure(text=self.jogo.matriz[0][0])
            self.botao7.configure(text=self.jogo.matriz[0][0])
            self.botao8.configure(text=self.jogo.matriz[0][0])
            self.botao9.configure(text=self.jogo.matriz[0][0])
            self.jogo.jogadas=[]
            print(self.jogo.matriz)
            
    def mudar6(self):
        self.botao6.configure(text=self.jogo.recebe_jogada(1,2))    
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        print(self.jogo.verifica_ganhador())
        if self.jogo.verifica_ganhador()!=(-1):
            self.label.configure(text=self.jogo.limpa_jogadas())
            self.botao1.configure(text=self.jogo.matriz[0][0])
            self.botao2.configure(text=self.jogo.matriz[0][0])
            self.botao3.configure(text=self.jogo.matriz[0][0])
            self.botao4.configure(text=self.jogo.matriz[0][0])
            self.botao5.configure(text=self.jogo.matriz[0][0])
            self.botao6.configure(text=self.jogo.matriz[0][0])
            self.botao7.configure(text=self.jogo.matriz[0][0])
            self.botao8.configure(text=self.jogo.matriz[0][0])
            self.botao9.configure(text=self.jogo.matriz[0][0])
            self.jogo.jogadas=[]
            print(self.jogo.matriz)
            
    def mudar7(self):
        self.botao7.configure(text=self.jogo.recebe_jogada(2,0))    
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        print(self.jogo.verifica_ganhador())
        if self.jogo.verifica_ganhador()!=(-1):
            self.label.configure(text=self.jogo.limpa_jogadas())
            self.botao1.configure(text=self.jogo.matriz[0][0])
            self.botao2.configure(text=self.jogo.matriz[0][0])
            self.botao3.configure(text=self.jogo.matriz[0][0])
            self.botao4.configure(text=self.jogo.matriz[0][0])
            self.botao5.configure(text=self.jogo.matriz[0][0])
            self.botao6.configure(text=self.jogo.matriz[0][0])
            self.botao7.configure(text=self.jogo.matriz[0][0])
            self.botao8.configure(text=self.jogo.matriz[0][0])
            self.botao9.configure(text=self.jogo.matriz[0][0])
            self.jogo.jogadas=[]
            print(self.jogo.matriz)
            
    def mudar8(self):
        self.botao8.configure(text=self.jogo.recebe_jogada(2,1))    
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        print(self.jogo.verifica_ganhador())
        if self.jogo.verifica_ganhador()!=(-1):
            self.label.configure(text=self.jogo.limpa_jogadas())
            self.botao1.configure(text=self.jogo.matriz[0][0])
            self.botao2.configure(text=self.jogo.matriz[0][0])
            self.botao3.configure(text=self.jogo.matriz[0][0])
            self.botao4.configure(text=self.jogo.matriz[0][0])
            self.botao5.configure(text=self.jogo.matriz[0][0])
            self.botao6.configure(text=self.jogo.matriz[0][0])
            self.botao7.configure(text=self.jogo.matriz[0][0])
            self.botao8.configure(text=self.jogo.matriz[0][0])
            self.botao9.configure(text=self.jogo.matriz[0][0])
            self.jogo.jogadas=[]
            print(self.jogo.matriz)
            
    def mudar9(self):
        self.botao9.configure(text=self.jogo.recebe_jogada(2,2))    
        self.label.configure(text='proxima jogada:{0}'.format(self.jogo.proxima))
        print(self.jogo.verifica_ganhador())
        if self.jogo.verifica_ganhador()!=(-1):
            self.label.configure(text=self.jogo.limpa_jogadas())
            self.botao1.configure(text=self.jogo.matriz[0][0])
            self.botao2.configure(text=self.jogo.matriz[0][0])
            self.botao3.configure(text=self.jogo.matriz[0][0])
            self.botao4.configure(text=self.jogo.matriz[0][0])
            self.botao5.configure(text=self.jogo.matriz[0][0])
            self.botao6.configure(text=self.jogo.matriz[0][0])
            self.botao7.configure(text=self.jogo.matriz[0][0])
            self.botao8.configure(text=self.jogo.matriz[0][0])
            self.botao9.configure(text=self.jogo.matriz[0][0])
            self.jogo.jogadas=[]
            print(self.jogo.matriz) 
            
app= Tabuleiro()

