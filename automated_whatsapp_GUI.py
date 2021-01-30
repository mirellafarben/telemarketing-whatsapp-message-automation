import tkinter as tk
from tkinter import ttk
import automated_whatsapp as aw
from tkinter import filedialog
import time

background_color = '#002c3e'
font_color = "#afbec4"
button_color = "#5f676b"

root = tk.Tk ()
root.geometry ("800x800")
root.config (bg=background_color)

text = "Bem vindo(a) ao meu software! Digite ou escolha o arquivo de texto\n com a mensagem que você deseja" \
       " enviar aos contatos."
instructions = tk.Label (root, text=text, width=57, height=2, font=('helvetica', 10),
                         bg=font_color, anchor='center')
instructions.pack (side=tk.TOP)

my_text = tk.Text (root, width=60, height=25)
my_text.pack (pady='50')


def send():
    mensagem_final = ""

    texto_pra_formatar = my_text.get ("1.0", tk.END)
    mensagem_inicial = aw.whatsapp_newline_translator (texto_pra_formatar)
    mensagem_final += mensagem_inicial

    instructions.pack_forget ()
    my_text.pack_forget ()
    get_text_button.pack_forget ()

    create_excel_chooser_page ()
    return mensagem_final


def search_contact_file_and_send():
    planilha_com_numeros = filedialog.askopenfilename ()
    aw.csv_translator (planilha_com_numeros)


    telefones = ["TELEFONE1", "TELEFONE2", "TELEFONE3"]
    for telefone in telefones:
        aw.message_sender ('output.csv', telefone, send ())


def create_excel_chooser_page():
    excel_text = "Agora, escolha o arquivo em formato de PDF ou Planilha do Excel onde se encontram \n" \
                 " as listas com os números de telefones."

    excel_information = tk.Label (root, text=excel_text, width=80, height=4, font=('helvetica', 12),
                                  bg=font_color, anchor='center', bd=10)
    excel_information.pack (side=tk.TOP)

    browse_excel_button = tk.Button (root, text="Selecione o arquivo.", bg=button_color, fg="black", width=40, height=5,
                                     font=('helvetica', 14), anchor='center', command=search_contact_file_and_send)
    browse_excel_button.pack(side=tk.BOTTOM)


get_text_button = tk.Button (root, text="Enviar", bg="#42c964", fg="black", width=25, height=8,
                             font=('helvetica', 11), anchor='center', command=send)
get_text_button.pack (side=tk.BOTTOM)

root.mainloop ()

