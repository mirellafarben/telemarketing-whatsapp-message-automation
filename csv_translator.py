class CSVTranslator:
    @staticmethod
    def csv_translator(planilha):
        planilha_a_ser_convertida = open(planilha, 'r', encoding='utf8', errors='ignore')
        planilha_convertida = open("planilha_convertida.csv", 'w', encoding='utf8', errors='ignore')

        lines = planilha_a_ser_convertida.readlines()

        for line in lines :
            planilha_convertida.write(line.replace(";", ','))

