import pyautogui as pg
import webbrowser as wb
import tkinter as tk
from tkinter import filedialog
import time
import pandas
import tabula


def whatsapp_newline_translator(texto_pra_formatar):
    if isinstance (texto_pra_formatar, str):

        text = texto_pra_formatar.replace ("\n", ('%0' + 'a'))

    else:
        mensagem_inicial = ""
        mensagem_inicial += open (texto_

                                  , 'r', encoding='utf-8', errors='ignore')
        text = ""
        lines = mensagem_inicial.readlines ()
        for line in lines:
            text += line.replace ("\n", ('%0' + 'a'))

    return text


def csv_translator(planilha):
    if str (planilha).endswith ('.pdf'):
        tabula.convert_into (planilha, "output.csv", output_format='csv', pages='all')
    elif str (planilha).endswith ('.xlsx'):
        df = pandas.read_excel (planilha)
        df.to_csv ("output.csv", sep=",")
    elif str (planilha).endswith ('.csv'):
        pass
    else:
        print ("Arquivo de planilha não suportado.")


def message_sender(planilha, telefone, message):
    fivefive = "+55"
    data = pandas.read_csv (planilha)
    data_dict = data.to_dict ('list')
    number = data_dict[telefone]
    combo = zip (number)
    contador = 0

    print (len (telefone))
    for number in combo:
        final_number = fivefive + str (number).replace ('(', '').replace (')', '').replace ('.0', '').replace (
            ',', '')

        wb.open ('https://web.whatsapp.com/send?phone=' + final_number + '&text=' + message)
        width, height = pg.size ()
        pg.click (width / 2, height / 2)
        time.sleep (10)

        pg.press ('enter')

        time.sleep (1)
        pg.hotkey ('ctrl', 'w')
        pg.press ('enter')

        contador += 1

        print (contador)
        print (final_number)


def main():
    telefones = ["TELEFONE1", "TELEFONE2", "TELEFONE3"]

    print ("iniciando o processo...")

    for telefone in telefones:
        message_sender ('output.csv', telefone, message)


if __name__ == '__main__':
    main ()
