"""
Script para envio de emails via SMTP do Gmail
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self):
        self.senha_email = self._load_environment_variables()
        self.email_params = self._setup_email_parameters()

    def _load_environment_variables(self):
        """Carrega variáveis de ambiente"""
        senha = os.getenv("EMAIL_PASSWORD")
        if not senha:
            raise EnvironmentError("EMAIL_PASSWORD não encontrada nas variáveis de ambiente")
        return senha

    def _setup_email_parameters(self):
        """Configura parâmetros do email"""
        return {
            'remetente': "zoroastreshermeticus@gmail.com",
            'destinatario': "mateusgremory@gmail.com",
            'assunto': "Envio de email pelo Python"
        }

    def _create_email_body(self):
        """Cria corpo do email em HTML"""
        return """
        <h1>ATUALIZAÇÃO DE TABELAS COM MySQL</h1>
        
        <h2>TABELAS</h2>
        
        <pre>
        create table cidade (
        id_cidade int primary key,
        cidade_nome varchar (60),
        uf varchar (2),
        grupo numeric (8,2)
        )
        
        create table cliente (
        id_cliente int primary key,
        cliente_nome varchar (100),
        cep numeric (8),
        grupo numeric (8)
        )
        </pre>
        
        <h2>VALORES</h2>
        
        <pre>
        insert into cidade values 
        (1,'ARAGUAINA','TO','1'),
        (2,'SÃO JOSÉ','SP','2'),
        (3,'UBERLANDIA','MG','3'),
        (4,'ILHEUS','BA','4'),
        (5,'CARAJAS','PA','5'),
        (6,'IMPERATRIZ','MA','6')
        
        insert into cliente values 
        (1,'JOSÉ','72888420','1'),
        (2,'CASSIA','73888420','2'),
        (3,'HUGO','74888420','3'),
        (4,'IVO','75888420','4'),
        (5,'JHON','76888420','5'),
        (6,'IRAN','77888420','6')
        </pre>
        """

    def send(self):
        """Envia o email"""
        try:
            msg = MIMEMultipart()
            msg["From"] = self.email_params['remetente']
            msg["To"] = self.email_params['destinatario']
            msg["Subject"] = self.email_params['assunto']
            msg.attach(MIMEText(self._create_email_body(), "html"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.email_params['remetente'], self.senha_email)
                server.send_message(msg)
                print("Email enviado com sucesso")
                
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
            raise


if __name__ == "__main__":
    sender = EmailSender()
    sender.send()
