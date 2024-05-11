import pyautogui
import time
import pandas as pd

tabela = pd.read_csv("produtos.csv")

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https//dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=1686, y=591)
pyautogui.write("python2024@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.click(x=1902, y=838)

for linha in tabela.index:
    pyautogui.click(x=1723, y=418)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha,"obs"]): #verifica se existe informação em obs, caso contrario não preenche
        pyautogui.write(str(tabela.loc[linha,"obs"]))
        
    pyautogui.click(x=1868, y=1380)
    pyautogui.scroll(5000)