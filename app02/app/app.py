from flask import Flask, request, abort
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/mail', methods=['POST'])
def root():
    if request.method == 'POST':
        request_json = request.get_json()
        gmail_user = 'guilhermeedington@gmail.com.br'
        gmail_pass = open('senha.pass','r').read()
        gmail_server = 'smtp.gmail.com'
        gmail_port = 587
        mail = MIMEMultipart("alternative")
        mail['From'] = gmail_user
        mail['To'] = request_json["mail"]
        mail['Subject'] = 'INSCRIÇÃO | APP FLASK EDINGTON'
        mail_html = '''\
            <h1>Inscrição realizada com sucesso!</h1>
            <h3>Parabéns !!NOME!!, você foi inscrito no app flask Edington!</h3>
            <p>desenvolvido por Edington</p>
        '''
        mail_html = mail_html.replace("!!NOME!!",request_json["nome"])
        mail_message = MIMEText(mail_html,"html")
        mail.attach(mail_message)
        with smtplib.SMTP(gmail_server, gmail_port) as server:
            server.starttls()
            server.login(gmail_user, gmail_pass)
            server.sendmail(gmail_user, request_json["mail"], mail.as_string())
    else:
        abort(400)

if __name__ == "__main__":
 app.run(host="0.0.0.0")
