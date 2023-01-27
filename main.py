from reportlab.pdfgen import canvas
# import tkinter as tk
import pandas as pd

def GeneratePDFA4(lista):
    try:
        nome_pdf = str(lista.CODIGO)
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))

        if(len(lista.NOME) > 10):
          pdf.setFont("Helvetica-Bold", 40)
          pdf.drawString(40, 560, lista.NOME.upper())
        else:
          pdf.setFont("Helvetica-Bold", 80)
          pdf.drawString(40, 560, lista.NOME.upper())

        pdf.setTitle(nome_pdf)


        pdf.setFont("Helvetica", 30)
        pdf.drawString(45, 525, lista.MARCA.upper())
        

        pdf.setFont("Helvetica", 20)
        pdf.drawString(45, 500, lista.GRAMAGEM.upper())
        
        preco = str(lista.PREÇO)

        if(len(preco.split('.')[0]) < 2):
          pdf.setFont("Helvetica-Bold", 30)
          pdf.drawString(110,330, 'R$')
          pdf.setFont("Helvetica-Bold", 250)
          pdf.drawString(150,300, preco.split('.')[0])
          pdf.setFont("Helvetica-Bold", 100)
          pdf.drawString(280,380, ","+preco.split('.')[1])
        else:
          pdf.setFont("Helvetica-Bold", 30)
          pdf.drawString(80,330, 'R$')
          pdf.setFont("Helvetica-Bold", 250)
          pdf.drawString(120,300, preco.split('.')[0])
          pdf.setFont("Helvetica-Bold", 100)
          pdf.drawString(390,380, ","+preco.split('.')[1])

        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(450,275, lista.TIPO.upper())

        pdf.rotate(15)
        pdf.rect(270, 180, 250, 4, fill=True)
        pdf.rect(310, 160, 185, 4, fill=True)

        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))

produtos = pd.read_excel("Produtos.xlsx", engine='openpyxl')

for i, row in pd.DataFrame(produtos).iterrows():
    GeneratePDFA4(row)
    # preco = str(row["PREÇO"])
    # print(preco.split('.'))
    # print(row)

# CODIGO NOME PREÇO GRAMAGEM MARCA TIPO
