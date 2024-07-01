## Auto Scheduler

### 🛠️ Tecnologias Utilizadas

- Python 3.7+
- Bibliotecas:
  - `os`
  - `datetime`
  - `pandas`
  - `logging`
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `googleapiclient`

### ✨ Funcionalidades Principais

- **Autenticação com Google Calendar**: Autentica usando OAuth 2.0 e obtém o serviço do Google Calendar.
- **Criação Automática de Eventos**: Lê eventos de um arquivo Excel e cria eventos correspondentes no Google Calendar.
- **Ajuste de Datas e Horas**: Ajusta as datas e horas no DataFrame antes de criar os eventos, garantindo o formato correto.

### 📋 Requisitos

1. Python 3.7 ou superior.
2. Dependências Python (instaláveis via `pip`):
   - `os`
   - `datetime`
   - `pandas`
   - `logging`
   - `google-auth`
   - `google-auth-oauthlib`
   - `google-auth-httplib2`
   - `googleapiclient`
3. Arquivo `credentials.json` obtido do Google Cloud.
4. Arquivo `eventos.xlsx` com as colunas `Evento`, `Data` (formato `DD/MM/YYYY`), e `Hora` (formato `HH:MM` ou `HH:MM:SS`).

### Instruções de Uso

1. Clone o repositório e navegue até o diretório do projeto.
2. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   .\env\Scripts\activate  # Windows


### Instale as dependências:

pip install -r requirements.txt

3.Instale as dependências:

pip install -r requirements.txt


4.Coloque o arquivo credentials.json na raiz do projeto.
5.Coloque o arquivo eventos.xlsx na raiz do projeto.
6.Execute o script principal:

python auto_scheduler.py


Obrigado por visitar o meu projeto! Sinta-se a vontade para realizar uma cópia e personalizar para assim também demonstrar os seus projetos! 😊