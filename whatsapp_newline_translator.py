class WhatsappTranslator:
    @staticmethod
    def whatsapp_newline_translator(texto_pra_formatar):
        mensagem_inicial = open(texto_pra_formatar, 'r', encoding='utf8', errors='ignore')
        texto_final = open("texto_formatado.txt", 'w', encoding='utf8', errors='ignore')

        codigo = '%0' + 'a'
        text = ""
        lines = mensagem_inicial.readlines()
        for line in lines :
            text += line.replace("\n", ('%0' + 'a'))

        texto_final.write(text)
        print(text)



