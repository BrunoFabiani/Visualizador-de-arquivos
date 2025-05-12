import FreeSimpleGUI as sg
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Salva a imagem
def processar_imagem(image_path):  
    try:
        img = cv2.imread(image_path)
        return img
    except Exception as e:
        sg.popup_error(f"Erro ao processar a imagem: {e}")

# Funções para processar a imagem
def cinza(img):
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plt.imshow(img, cmap='gray')
        plt.show()
        return img
    except Exception as e:
        sg.popup_error(f"Erro ao processar a imagem: {e}")

def inversao_cores(img):
    try:
        img = cv2.bitwise_not(img)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()
        return img
    except Exception as e:
        sg.popup_error(f"Erro ao processar a imagem: {e}")

def aumento_contraste(img):
    try:
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        l = cv2.equalizeHist(l)
        img = cv2.merge((l, a, b))
        img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()
        return img
    except Exception as e:
        sg.popup_error(f"Erro ao processar a imagem: {e}")

def blur(img):
    try:
        img = cv2.GaussianBlur(img, (7, 7), 0)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()
        return img
    except Exception as e:
        sg.popup_error(f"Erro ao processar a imagem: {e}")

def sharpen(img):
    try:
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        img = cv2.filter2D(img, -1, kernel)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()
        return img
    except Exception as e:
        sg.popup_error(f"Erro ao processar a imagem: {e}")

def deteccao_bordas(img):
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.Canny(img, 100, 200)
        plt.imshow(img, cmap='gray')
        plt.show()
        return img
    except Exception as e:
        sg.popup_error(f"Erro ao processar a imagem: {e}")

# Layout da janela ________________________________________________
layout = [
    [sg.Text('Selecione uma imagem para processar')],
    [sg.InputText(key='-FILE-', enable_events=True), sg.FileBrowse(file_types=(("Images", "*.png;*.jpg;*.jpeg"),))],
    [sg.Button('PROCESSAR IMAGEM'), sg.Button('Cinza'), sg.Button('Inverter Cores'), sg.Button('Aumento de contraste'), sg.Button('Desfoque'), sg.Button('Nitidez'), sg.Button('Deteccao de borda'), sg.Button('Cancelar')]
]

# Criando a janela
window = sg.Window('Processamento de Imagem', layout)

# Loop de eventos
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    if event == 'PROCESSAR IMAGEM':
        image_path = values['-FILE-']
        if image_path:
            img = processar_imagem(image_path)
        else:
            sg.popup_error("Por favor, selecione uma imagem.")

    if event == 'Cinza':
        if 'img' in locals():
            img = cinza(img)
        else:
            sg.popup_error("Por favor, selecione uma imagem.")

    if event == 'Inverter Cores':
        if 'img' in locals():
            img = inversao_cores(img)
        else:
            sg.popup_error("Por favor, selecione uma imagem.")

    if event == 'Aumento de contraste':
        if 'img' in locals():
            img = aumento_contraste(img)
        else:
            sg.popup_error("Por favor, selecione uma imagem.")

    if event == 'Desfoque':
        if 'img' in locals():
            img = blur(img)
        else:
            sg.popup_error("Por favor, selecione uma imagem.")

    if event == 'Nitidez':
        if 'img' in locals():
            img = sharpen(img)
        else:
            sg.popup_error("Por favor, selecione uma imagem.")

    if event == 'Deteccao de borda':
        if 'img' in locals():
            deteccao_bordas(img)
        else:
            sg.popup_error("Por favor, selecione uma imagem.")
    

# Fechar a janela
window.close()