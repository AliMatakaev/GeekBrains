import re


def parce_email(email):
    if re.match(r'(\S+)(@)(\S+)(\.)(\S+)', email):
        user = email[:email.find('@')]
        domain_adr = email[email.find('@')+1:]
        result = {'username': user, 'domain': domain_adr}
        print(result)
    else:
        raise ValueError('Wrong email:', email)


parce_email('ivan_ivanov@mail.ru')
