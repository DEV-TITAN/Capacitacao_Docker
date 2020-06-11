from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def root():
   return redirect(url_for('.index'))

@app.route("/index", methods=['GET','POST'])
def index():
   if request.method == 'POST':
      nome = request.form['nome']
      mail = request.form['email']
      requests.post('http://app02:5000/mail',{'nome':nome,'mail':mail})
      return redirect(url_for('.thanks', nome = nome))
   return render_template('index.html')

@app.route("/thanks", methods=['GET','POST'])
def thanks():
   nome = request.args.get('nome')
   if nome != None:
      return render_template('thanks.html', nome = nome)
   return redirect(url_for('.index'))
   
if __name__ == "__main__":
 app.run(host="0.0.0.0")
