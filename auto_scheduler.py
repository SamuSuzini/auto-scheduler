import os
import datetime
import pandas as pd
import logging
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Configuração do logger
logging.basicConfig(
    filename='auto_scheduler.log',
    level=logging.ERROR,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Função para autenticar e obter o serviço do Google Calendar
def get_calendar_service():
    try:
        SCOPES = ['https://www.googleapis.com/auth/calendar']
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=8080)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        service = build('calendar', 'v3', credentials=creds)
        return service
    except Exception as e:
        logging.error(f"Erro ao obter serviço do Google Calendar: {e}")
        raise

# Função para criar um evento no Google Calendar
def create_event(service, event_details):
    try:
        event = {
            'summary': event_details['summary'],
            'start': {
                'dateTime': event_details['start'],
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': event_details['end'],
                'timeZone': 'America/Sao_Paulo',
            },
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
    except Exception as e:
        logging.error(f"Erro ao criar evento: {event_details} - {e}")

# Função para ajustar as datas e horas no DataFrame
def ajustar_datas_horas(df):
    try:
        # Tratamento da coluna de data para garantir o formato correto
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce', format='%d/%m/%Y')

        # Tratamento da coluna de hora para garantir o formato correto
        def ajustar_hora(hora_str):
            try:
                # Tenta converter para datetime e formata para HH:MM
                hora = pd.to_datetime(hora_str, format='%H:%M:%S', errors='coerce')
                if pd.isna(hora):
                    hora = pd.to_datetime(hora_str, format='%H:%M', errors='coerce')
                return hora.strftime('%H:%M')
            except Exception as e:
                logging.error(f"Erro ao ajustar a hora: {hora_str} - {e}")
                return None

        df['Hora'] = df['Hora'].apply(ajustar_hora)
        return df
    except Exception as e:
        logging.error(f"Erro ao ajustar datas e horas: {e}")
        raise

# Função principal para ler a lista e agendar os eventos
def main():
    try:
        service = get_calendar_service()

        # Leitura da lista a partir de um arquivo Excel
        df = pd.read_excel('eventos.xlsx')

        # Ajusta as datas e horas no DataFrame
        df = ajustar_datas_horas(df)

        for index, row in df.iterrows():
            date_time_str = f"{row['Data'].strftime('%d/%m/%Y')} {row['Hora']}"
            start_time = datetime.datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
            end_time = start_time + datetime.timedelta(hours=1)  # Supondo que cada procedimento dure 1 hora
            event_details = {
                'summary': row['Evento'],
                'start': start_time.isoformat(),
                'end': end_time.isoformat()
            }
            create_event(service, event_details)
    except Exception as e:
        logging.error(f"Erro na execução principal: {e}")

if __name__ == '__main__':
    main()