# coding: utf-8

"""
Codigo para calcular e enviar por e-mail os seguintes dados:

- faturamento por loja
- quantidade de produtos vendidos por loja
- ticket medio por produto em cada loja

Como fazer:
- importar base de dados
- tratar base de dados
- visualizar base de dados
- enviar dados tratados

Exercício do minicurso de Python da Hashtag Programação

by:BrunoBTO
"""

# bibliotecas usadas
import pandas as pd
import smtplib
import email.message

# importando a base de dados do excel
vendas_df = pd.read_excel('Vendas.xlsx')

# visualizando a base de dados
pd.set_option('display.max_columns', None)

# faturamento por loja
faturamento_loja = vendas_df[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
faturamento_loja = faturamento_loja.sort_values(by='Valor Final', ascending=False)

# quantidade de produtos vendidos por loja
quantidade_loja = vendas_df[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
quantidade_loja = quantidade_loja.sort_values(by='Quantidade', ascending=False)

# ticket medio por venda em cada loja
ticket_medio = (faturamento_loja['Valor Final'] / quantidade_loja['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
ticket_medio = ticket_medio.sort_values(by='Ticket Médio', ascending=False)
print(ticket_medio)

# criando email com relatorio
corpo_email = f"""
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada loja</p>

<p>&nbsp;</p>
<p>&nbsp;</p>

<p>Faturamento:</p>
{faturamento_loja.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>&nbsp;</p>
<p>&nbsp;</p>

<p>Quantidade Vendida:</p>
{quantidade_loja.to_html(formatters={'Quantidade': '{:,.0f}'.format})}

<p>&nbsp;</p>
<p>&nbsp;</p>

<p>Ticket Médio por produto em cada loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>&nbsp;</p>
<p>&nbsp;</p>

<p>Qualquer dúvida estarei à disposição.</p>

<p>&nbsp;</p>

<p>Att.</p>
<p>Bruno Oliveira</p>
"""
# Enviando email
msg = email.message.Message()
msg['Subject'] = "Treinamento Hashtag Python"
msg['From'] = 'brunot.oliveira95@gmail.com'
msg['To'] = 'brunot.oliveira95@gmail.com'
password = 'Aqui vc coloca a sua senha ;)'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado')
