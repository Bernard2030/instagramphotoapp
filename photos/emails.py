# from dscmailer import mailer


sender='opiyodoro@gmail.com'
receiver='moseskinyua12@gmail.com'
subject='Sending with Twilio SendGrid is Fun'
api_key= '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'
html='<strong>and easy to do anywhere, even with Python</strong>'


from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(sender,receiver,subject,html):
    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=html)
    try:
        sg = SendGridAPIClient(api_key=api_key)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(f'Error while sending email. {e}')

        
        


send_mail(sender, receiver, subject, html)        