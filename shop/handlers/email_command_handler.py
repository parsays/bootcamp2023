import smtplib
from email.mime.text import MIMEText
import logging

logger = logging.getLogger(__name__)


def send_email(to_email, subject, message):
    # Set up the email message
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'parsa.ys10@gmail.com'
    msg['To'] = to_email

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        # Log in to your email account
        smtp.login('parsa.ys10@gmail.com', 'bobkasxmbxvsjzrz')

        # Send the email message
        smtp.send_message(msg)

    print('Email sent successfully')
    logger.info('Email sent successfully')
