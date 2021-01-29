import pyautogui as pg
import webbrowser as wb
import time
import pandas

class MessageSender:
    @staticmethod
    def message_sender(planilha, telefone, message):
        fivefive = "+55"
        data = pandas.read_csv (planilha)
        data_dict = data.to_dict('list')
        number = data_dict[telefone]
        combo = zip (number)
        contador = 0
        for number in combo:

            final_number = fivefive + str (number).replace ('(', '').replace (')', '').replace ('.0', '').replace (
                ',', '')

            wb.open ('https://web.whatsapp.com/send?phone=' + final_number + '&text=' + message)
            width, height = pg.size ()
            pg.click (width / 2, height / 2)
            time.sleep (20)

            pg.press ('enter')

            time.sleep (2)
            pg.hotkey ('ctrl', 'w')
            pg.press ('enter')

            contador += 1

            print (contador)
            print (final_number)
