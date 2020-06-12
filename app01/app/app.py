from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)

# Rota / (raiz)
#
# Apenas redireciona o browser para roda /index
@app.route('/', methods=['GET','POST'])
def root():
   return redirect(url_for('.index'))

# Rota /index
#
# Quando o método for GET, exibe a página templates/index.html.
#
# Quando for POST recebe os campos do  formulário  e  cria  uma 
# requisição POST  para  http://app02:5000/mail  com  os  dados
# em  forma   de  JSON.  Após  receber  a  resposta  de  app02, 
# redireciona para  a  rota /thanks passando  o  nome  dado  no 
# formulário como argumento.
@app.route("/index", methods=['GET','POST'])
def index():
   if request.method == 'POST':
      nome = request.form['nome']
      mail = request.form['email']
      requests.post('http://app02:5000/mail',json={'nome': nome,'mail': mail})
      return redirect(url_for('.thanks', nome = nome))
   return render_template('index.html')

# Rota /thanks
#
# Retorna a página temlpates/thanks.html caso receba algum nome
# como parâmetro na URL na requisição.
# 
# Caso não receba, redireciona para a rota /index 
@app.route("/thanks", methods=['GET','POST'])
def thanks():
   nome = request.args.get('nome')
   if nome != None:
      return render_template('thanks.html', nome = nome)
   return redirect(url_for('.index'))
   
if __name__ == "__main__":
 app.run(host="0.0.0.0")
