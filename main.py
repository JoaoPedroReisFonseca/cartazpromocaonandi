from reportlab.pdfgen import canvas

def GeneratePDFA4(lista):
    try:
        nome_pdf = lista["codigo"]
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))

        if(len(lista["nome"]) > 10):
          pdf.setFont("Helvetica-Bold", 40)
          pdf.drawString(40, 600, lista["nome"].upper())
        else:
          pdf.setFont("Helvetica-Bold", 80)
          pdf.drawString(40, 600, lista["nome"].upper())

        pdf.setTitle(nome_pdf)


        pdf.setFont("Helvetica", 30)
        pdf.drawString(40, 560, lista["marca"].upper()+"  " +lista["gramagem"].upper())

        if(len(lista["preco"].split(',')[0]) < 2):
          pdf.setFont("Helvetica-Bold", 30)
          pdf.drawString(110,330, 'R$')
          pdf.setFont("Helvetica-Bold", 250)
          pdf.drawString(150,300, lista["preco"].split(',')[0])
          pdf.setFont("Helvetica-Bold", 100)
          pdf.drawString(280,380, ","+lista["preco"].split(',')[1])
        else:
          pdf.setFont("Helvetica-Bold", 30)
          pdf.drawString(80,330, 'R$')
          pdf.setFont("Helvetica-Bold", 250)
          pdf.drawString(120,300, lista["preco"].split(',')[0])
          pdf.setFont("Helvetica-Bold", 100)
          pdf.drawString(390,380, ","+lista["preco"].split(',')[1])

        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(450,275, lista["tipo"].upper())

        pdf.rotate(15)
        pdf.rect(270, 180, 250, 4, fill=True)
        pdf.rect(310, 160, 185, 4, fill=True)

        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))

listas = [
  {"codigo": "4321", "nome": "cerveja", "marca": "12345678901234567890", "preco":"2,49", "gramagem": "300ml", "tipo": "und"},
  {"codigo": "1234", "nome": "PÃO tradicional", "marca": "bauduco", "preco":"12,49", "gramagem": "70gr", "tipo": "und"},
  {"codigo": "5678", "nome": "maionese", "marca": "hellmann's-pote", "preco":"22,49", "gramagem": "70gr", "tipo": "und"},
  {"codigo": "5679", "nome": "esponja multiuso", "marca": "hellmann's-pote", "preco":"12,49", "gramagem": "70gr", "tipo": "und"}
  ]

for lista in listas:
  GeneratePDFA4(lista)

