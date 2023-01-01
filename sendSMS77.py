 # !/usr/bin/env python
# SMS77.io V 2022.12.001
# https://www.sms77.io/de/docs/gateway/http-api/sms-versand/

from sms77api.Sms77api import Sms77api
import json
# import datetime

# API-KEY
api_key = 'Hier-dein-ApiKey-eintragen'

# Debug Modus, falls aktiviert werden keine SMS verschickt oder berechnet
int_debug = 1

# SMS als Flash SMS versenden. Nur wenn ohne 'delay', diese werden direkt im Display des Empfängers angezeigt. Flash-SMS haben keinen Absender.
int_flash = 0

# Datum/Zeit für zeitversetzten Versand, Unix-Timestamp oder ein Zeitstempel im Format yyyy-mm-dd hh:ii
# wenn leer oder in vergangenheit, wird das sofort gesendet
# test mit unix date (ist nicht notwendig)
# unix_delay = int(datetime.datetime.strptime(str_delay, '%Y-%m-%d %H:%M:%S').timestamp())
str_delay = ''
# str_delay = '2023-10-22 21:42:00'

# Empfänger-Telefonnummer, mehrere Empfänger können per Komma separiert werden
phone_to = '49xxxxxxxxxxxx'

# Absender-Telefonnummer, dieser darf maximal 11 alphanumerische oder 16 numerische Zeichen enthalten
phone_from = 'Test42'

# Eigene ID für diese Nachricht
foreign_id = 'smsPython'

# SMS-Nachricht, bei mehr als 160 Zeichen wird der Text auf mehrere SMS verteilt, welche einzeln berechnet werden
str_message = 'Text bla bla bla bla ....)'

# sms77api-Client erstellen
client = Sms77api(api_key)

if __name__ == '__main__':

    # SMS-Nachricht senden und Antwort des Servers in der Variablen "response" speichern
    response = client.sms(phone_to, str_message, {
        'from': phone_from,
        'foreign_id ': foreign_id,
        'flash': int_flash,
        'json': True,
        'delay': str_delay,
        'debug': int_debug,
    })

    # Antwort des Servers in einen JSON-formatierten String umwandeln
    response_json_str = json.dumps(response)

    # JSON-formatierten String parsen und in das Python-Objekt "response_json" umwandeln
    response_json = json.loads(response_json_str)

    # schluessel_liste = response_json.keys()
    # alle Schlüssel ausgeben
    # print(schluessel_liste)
    # Ergebnis: dict_keys(['success', 'total_price', 'balance', 'debug', 'sms_type', 'messages'])

    # Werte der Schlüssel abfragen
    success = response_json['success']
    total_price = response_json['total_price']
    balance = response_json['balance']
    sms_type = response_json['sms_type']
    messages = response_json['messages']
    debug = response_json['debug']

    # Überprüfen, ob die SMS erfolgreich gesendet wurde
    if success == '100':
        # SMS wurde erfolgreich gesendet
        print('\nNachricht wurde erfolgreich gesendet.')
    else:
        # SMS konnte nicht gesendet werden
        print('\nFehler beim Senden der Nachricht.')

    print(f'Preis: {total_price} €')
    print(f'Saldo: {balance} €')
    print(f'SMS Typ: {sms_type}')
    print(f'Delay: {str_delay}')
    # print(f'Nachricht: {messages}')
    print(f'Debug: {debug}')


    # Durch die Nachrichtenobjekte iterieren
    for message in messages:
        # Informationen über den Sendestatus abrufen
        id = message['id']
        sender = message['sender']
        recipient = message['recipient']
        text = message['text']
        encoding = message['encoding']
        success = message['success']
        error_text = message['error_text']

        # Sendestatus ausgeben
        print(f'ID: {foreign_id}')
        print(f'Absender: {sender}')
        print(f'Empfänger: {recipient}')
        print(f'Nachricht: {text}')
        print(f'Encoding: {encoding}')
        print(f'Success: {success}')
        print(f'Error: {error_text}')
