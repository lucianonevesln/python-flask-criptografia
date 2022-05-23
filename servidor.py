from flask import Flask, render_template, request
import jwt

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/codificar', methods=['POST'])
def codificar():
    id_codificar = request.form['id_codificar']
    id_codificar = jwt.encode({'id_codificar': f'{id_codificar}'},\
                                key = 'secret',\
                                algorithm='HS256')
    return render_template('index.html', id_codificar_html = id_codificar)

@app.route('/decodificar', methods=['POST'])
def decodificar():
    id_decodificar = request.form['id_decodificar']
    id_decodificar = jwt.decode(f'{id_decodificar}',\
                                  key = "secret",\
                                  algorithms=["HS256"])
    return render_template('index.html', id_decodificar_html = id_decodificar)

if __name__ =='__main__':
    app.run(host = 'localhost', port = 5000, debug = True)