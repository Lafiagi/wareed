import requests

# Django Imports
from django.conf import settings
from django.core.mail import send_mail

# Third Party Imports
from celery import shared_task


@shared_task
def send_welcome_mail(
    name: str,
    user_email: str,
) -> str:
    """
    This function sends an email to the user.

    :param name: The name of the user
    :type name: str

    :param user_email: The email address of the user
    :type user_email: str
    """

    mail_subject = "[Wareed]: Welcome Onboard!"

    body = f"""
    Hi {name},\n
    Welcome To Wareed,
    Waared is the first Freight Marketplace in Saudi Arabia,
    connecting SME & Enterprise businesses to courier and Logistic service providers.
    Our instant quoting tools will reduce the time spent looking for the best shipping option, 
    and it will give you full control over you exports and shipments.
    """

    requests.post(
        settings.MAILGUN_BASE_URL,
        auth=("api", f"{settings.MAILGUN_API_KEY}"),
        data={
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": [user_email],
            "subject": mail_subject,
            'text': body
        },
    )
