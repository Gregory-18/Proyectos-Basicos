import pyautogui as pt
import time 

limite = input('Cantidad de mensajes: ')
mensaje = str(input('Mensaje: '))
i = 0

time.sleep(3)
while i < int(limite):
    pt.typewrite(mensaje)
    pt.press('enter')
    i += 1