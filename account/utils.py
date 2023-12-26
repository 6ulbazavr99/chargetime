from django.core.mail import send_mail
from django.dispatch import receiver


from django_rest_passwordreset.signals import reset_password_token_created


HOST = 'localhost:8000'


def send_confirmation_email(user, code):
    link = f'http://{HOST}/api/v1/accounts/activate/{code}/'
    send_mail(
        'ANVAR LOX! Здравствуйте, активируйте ваш аккаунт!',
        f'Что активировать ваш аккаунт нужно перейти по ссылке ниже:'
        f'\n{link}'
        f'\nСсылка работает один раз!',
        'adiletraimbekov269@gmail.com',
        [user],
        fail_silently=False,
    )


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    send_mail(
        'ANVAR PIDOR! Password reset',
        f'Что reset ваш password нужно ввести код ниже:'
        f'\n'
        f'{reset_password_token.key}',
        'adiletraimbekov269@gmail.com',
        [reset_password_token.user.email],
        fail_silently=False,
    )
