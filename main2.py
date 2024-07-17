from flask import Flask, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sreejasrp22@gmail.com'
app.config['MAIL_PASSWORD'] = 'lhpl muhh vnjv kjlm'

mail = Mail(app)

def send_email_with_attachments(subject, body, recipients, attachments):
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=recipients)
    msg.body = body

    for attachment in attachments:
        try:
            with app.open_resource(attachment['path']) as fp:
                msg.attach(attachment['filename'], attachment['mimetype'], fp.read())
        except Exception as e:
            print(f"Error attaching file {attachment['path']}: {e}")
            return False

    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/send_email', methods=['POST', 'GET'])
def send_email():
    subject = "Python (Selenium) Assignment - Sreeja Bhattacharya"
    body = """Please find the following attachments:
1. Screenshot of the form filled via code.
2. Source code (GitHub repository).
3. Brief documentation of my approach.
4. My resume.
5. Links to past projects/work samples.
6. I confirm my availability to work full-time (10 am to 7 pm) for the next 3-6 months.
"""
    recipients = ['tech@themedius.ai']
    cc = ['hr@themedius.ai']

    attachments = [
        {'path': r'C:\Users\Sreej\Downloads\Screenshot (27).png', 'filename': 'Screenshot (27).png', 'mimetype': 'image/png'},
        {'path': r'C:\Users\Sreej\Downloads\link to git repo.txt', 'filename': 'link to git repo.txt','mimetype': 'text/plain'},
        {'path': r'C:\Users\Sreej\Downloads\Documentation- google form fill.txt', 'filename': 'Documentation- google form fill.txt', 'mimetype': 'text/plain'},
        {'path': r'C:\Users\Sreej\Downloads\updated resume.pdf', 'filename': 'updated resume.pdf', 'mimetype': 'application/pdf'},
        {'path': r'C:\Users\Sreej\Downloads\link to github.txt', 'filename': 'link to github.txt', 'mimetype': 'text/plain'}
    ]

    if send_email_with_attachments(subject, body, recipients + cc, attachments):
        return "Email sent!"
    else:
        return "Failed to send email."

if __name__ == '__main__':
    app.run(debug=True)
