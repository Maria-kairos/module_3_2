def send_email(message, recipient, *,sender='university.help@gmail.com'):
    if recipient.count('@'):
        pass
    else:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
        return
    if recipient.count('.com') or recipient.count('.ru') or recipient.count('.net'):
        pass
    else:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
        return

    if sender.count('@'):
        pass
    else:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
        return
    if sender.count('.com') or sender.count('.ru') or sender.count('.net'):
        pass
    else:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
        return

    if sender.count(recipient) or recipient.count(sender):
            print('Нельзя отправить письмо самому себе!')
    else:
        if sender == 'university.help@gmail.com':
            print('Письмо успешно отправлено с адреса ', sender, 'на адрес ', recipient, '.')
        else:
            print('НЕСТАНДАРТНЫЙ ОТПРАПВИТЕЛЬ! Письмо отпрапвлено с адреса ', sender, 'на адрес ', recipient, '.')

send_email('Здарова!', 'hgreo@gmail.com')


