import tkinter as tk
import threading
import time

#################################################################
#----------EXERCICIO PARA AULA DE SISTEMAS OPERACIONAIS---------#
#-----FAZER UM SEMÁFORO USANDO THREADS E INTERFACE EM PYTHON----#
#--------------ALUNO: LUIZ EDUARDO FRAZÃO BAGANHA---------------#
#-------------------MATRICULA: 202203338382---------------------#
#--------------FACI WYDEN - SISTEMAS OPERACIONAIS---------------#
#---------------------------------------------------------------#
#################################################################

#FUNÇÃO DO SEMAFORO
def semaforo():
    while True:
        # Luz verde
        luz("VERDE")
        time.sleep(4)
        # Luz amarela
        luz("AMARELO")
        time.sleep(2)
        # Luz vermelha
        luz("VERMELHO")
        time.sleep(3)

#FUNÇÂO DAS CORES DO SEMAFORO E MENSAGENS EXIBIDAS NA INTERFACE
def luz(colour):
    if colour == "VERMELHO":
        texto_luz.config(text="VERMELHO: PARE!", bg="red")
    elif colour == "AMARELO":
        texto_luz.config(text="AMARELO: VÁ DEVAGAR!", bg="yellow")
    else:
        texto_luz.config(text="VERDE: PODE SEGUIR!", bg="green")

#FUNÇÃO PARA EXIBIR A INTERFACE DO PROGRAMA
def interface():
    global texto_luz
    
    window = tk.Tk()
    window.title("Semáforo")
    window.geometry("400x200")
    
    texto_luz = tk.Label(window, text="", font=("Arial", 24), width=24, height=10)
    texto_luz.pack()
    
    threading.Thread(target=semaforo, daemon=True).start()

    window.resizable(False,False)
    window.mainloop()

interface()