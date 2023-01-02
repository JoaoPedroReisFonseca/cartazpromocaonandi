from reportlab.pdfgen import canvas

def sizeSpace(marca):
  tamanho = len(marca);
  print(tamanho)

def GeneratePDF(lista):
    try:
        nome_pdf = 'teste01'
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))

        pdf.setFont("Helvetica-Bold", 70)
        pdf.drawString(100, 600, "CERVEJA")
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica", 30)
        pdf.drawString(100,560, 'BAUDUCO')
        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(260,560, '300ML')
        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(120,380, 'R$')
        pdf.setFont("Helvetica-Bold", 150)
        pdf.drawString(180,360, '50')
        pdf.setFont("Helvetica-Bold", 80)
        pdf.drawString(350,410, ',49')
        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(470,350, 'UND')

        pdf.rotate(15)
        pdf.rect(300, 250, 250, 4, fill=True)
        pdf.rect(340, 230, 185, 4, fill=True)

        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))

lista = {'Rafaela': '19', 'Jose': '15', 'Maria': '22','Eduardo':'24'}

GeneratePDF(lista)
# sizeSpace("skol")