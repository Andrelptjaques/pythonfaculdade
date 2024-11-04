import pyautogui
from time import sleep

def abrir_navegador_e_fazer_login():
    # Pressiona a tecla 'Win' para abrir o menu Iniciar
    pyautogui.press('winleft')
    sleep(2)
    
    # Escreve 'chrome' para abrir o navegador
    pyautogui.write('chrome')
    sleep(2)
    
    # Pressiona 'Enter' para abrir o navegador Chrome
    pyautogui.press('enter')
    sleep(5)  # Tempo para o navegador abrir completamente
    
    # Aqui você pode adicionar a URL do site e automatizar o login
    pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
    pyautogui.press('enter')
    sleep(5)  # Aguarda o site carregar
    
    print('Chrome aberto e site carregado')

# Chamando a função
abrir_navegador_e_fazer_login()

#Pegar posições do mouse e da tela
print(pyautogui.position())
print(pyautogui.size())

#Funções do mouse 
time.sleep(5)
pyautogui.moveTo(x=957, y=896, duration=1)  # Mover o mouse para a posição
time.sleep(1)  # Pequena pausa para garantir que o movimento foi processado
pyautogui.click() #Clicar no lugar selecionado
pyautogui.moveTo(x=91, y=417, duration=1)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.scroll(-100)

import pyautogui
import time

pyautogui.PAUSE = 0.2

pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("iesb.blackboard.com")
pyautogui.press("enter")

time.sleep(2)

pyautogui.moveTo(x=947, y=889, duration = 1)
time.sleep(2)
pyautogui.click()
pyautogui.moveTo(x=85, y=418, duration = 1)
time.sleep(2)
pyautogui.click()

time.sleep(2)

pyautogui.moveTo(x=1437, y=351, duration = 1)

time.sleep(1)

pyautogui.scroll(-100)
pyautogui.moveTo(x=539, y=766, duration = 1)
pyautogui.click()