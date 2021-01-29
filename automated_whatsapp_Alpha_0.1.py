import pyautogui as pg
import webbrowser as wb
import tkinter as tk
from tkinter import filedialog
import whatsapp_newline_translator as wnt
import message_sender as ms
import csv_translator as ct
import time
import pandas


class AutomatedWhatsapp:

    @staticmethod
    def main():
        mensagem = open ("texto_formatado.txt", 'r', encoding='utf8', errors='ignore')
        message = str (mensagem.readline ())
        telefones = ["NUMERO1", "NUMERO2"]
        root = tk.Tk ()
        root.withdraw ()

        print ("Olá")
        time.sleep (2)
        print ("Bem vindo a versão Aplha 0.1 do meu software!")
        time.sleep (2)
        print ('...')
        time.sleep (2)

        print ("Selecione o documento de texto com a mensagem que você quer enviar. ")
        time.sleep (3)
        texto_pra_formatar = filedialog.askopenfilename ()
        wnt.WhatsappTranslator.whatsapp_newline_translator (texto_pra_formatar)

        time.sleep (2)
        print ("Pronto, agora... Selecione a planilha (em CSV) com os números")
        time.sleep (2)
        planilha_com_numeros = filedialog.askopenfilename()
        ct.CSVTranslator.csv_translator (planilha_com_numeros)

        print ("iniciando o processo...")

        sending = ms.MessageSender

        for telefone in telefones:
            sending.message_sender(planilha_com_numeros, telefone, message)
