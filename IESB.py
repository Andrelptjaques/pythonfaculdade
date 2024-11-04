import pyautogui
import time 

def abrir_navegador_e_entrar_no_site(url):
    pyautogui.press("winleft")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(7)

    pyautogui.write("iesb.blackboard.com")
    pyautogui.press("enter")
    time.sleep(4)

def clicar_para_entrar_no_site (x,y):
    pyautogui.moveTo(x=961, y=891, duration=1)
    time.sleep(7)
    pyautogui.click()

def clicar_para_entrar_materia (x,y):
    pyautogui.moveTo(x=91, y=416, duration=1)
    time.sleep(7)
    pyautogui.click()

def mudar_o_mouse_de_posicao (x,y):
    pyautogui.moveTo(x=1431, y=388, duration=1)
    time.sleep(4)
    pyautogui.click()

def descer_o_mouse ():
    pyautogui.scroll(-100)
    time.sleep(4)

def entrar_na_materia_do_momento (x,y):
    pyautogui.moveTo(x=434, y=617, duration=1)
    time.sleep(4)
    pyautogui.click()

def main():
    url = "iesb.blackboard.com"

    abrir_navegador_e_entrar_no_site(url)
    
    clicar_para_entrar_no_site(x=961, y=891)  # Ajuste as coordenadas conforme necessário
    clicar_para_entrar_materia(x=91, y=416)  # Ajuste as coordenadas conforme necessário
    mudar_o_mouse_de_posicao(x=1431, y=388)  # Ajuste as coordenadas conforme necessário
    descer_o_mouse()  # Rola para baixo
    entrar_na_materia_do_momento(x=568, y=671)  # Ajuste as coordenadas conforme necessário

if __name__ == "__main__":
    main()