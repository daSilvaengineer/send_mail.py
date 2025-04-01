## Configuração

1. Renomeie `config.py.example` para `config.py`
2. Configure suas credenciais no arquivo
3. Defina a variável de ambiente:
   ```bash
   export EMAIL_PASSWORD="sua_senha"
   ```

## Uso

```python
from src.email_sender import EmailSender

sender = EmailSender()
sender.send()
```

## Requisitos

- Python 3.6+
- Conta no Gmail com SMTP habilitado

Instale as dependências:
```bash
pip install python-dotenv
```

## Segurança

⚠️ Nunca armazene senhas diretamente no código!
Use sempre variáveis de ambiente ou arquivos de configuração seguros.
