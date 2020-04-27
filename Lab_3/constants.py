phone_number = "915783624"
out_call_k = 2
in_call_k = 0
free_sms = 10
sms_k = 1
csv_path_telephony = "data.csv"

csv_path_internet = "lab2.csv"
billing_ip = "217.15.20.194"
nfcapd_file = "nfcapd.202002251200"
internet_price = 0.5

info = {
    'recipient': {
        'name': 'Артемьев Даниил Анатольевич',
        'address': '191119, г. Санкт-Петербург, ул. Пушкина, д. 1',
        'account': '1234554321',
        'inn': '111222333',
        'kpp': '333222111',
        'bank': {
            'name': 'ПАО \"ИТМО\"',
            'bik': '3350',
            'account': '335020203350'
        },
        'director': 'Байрон В.А.',
        'accountant': 'Чичиков П.И.'
    },
    'customer': {
        'name': 'Иванов Ф.П.',
        'inn': '001100222',
        'kpp': '222001100',
        'address': '191119, г. Санкт-Петербург, ул. Ломоносова, д.9'
    },
    'payment': {
        'id': '1',
        'date': '25.04.2020',
        'sum': '',
        'nds': '',
        'cause': '#N3350 от 25.04.2020',
        'services': ''
    },
    'services': [
        {
            'id': '1',
            'name': 'Звонки',
            'amount': '',
            'measure': 'мин',
            'price': "Входящие звонки - {0} руб/мин.\nИсходящие звонки - {1} руб/мин".format(in_call_k, out_call_k),
            'sum': ''
        },
        {
            'id': '2',
            'name': 'Смс',
            'amount': '',
            'measure': 'шт',
            'price': "Первые {0} шт бесплатно, далее {1} руб/шт".format(free_sms, sms_k),
            'sum': ''
        },
        {
            'id': '3',
            'name': 'Интернет',
            'amount': '',
            'measure': 'Мб',
            'price': "{0} руб/Мб".format(internet_price),
            'sum': ''
        }
    ]
}

template = 'template.docx'
result = 'Счет №{0} от {1}.docx'.format(info['payment']['id'], info['payment']['date'])