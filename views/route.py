from __init__ import app
from flask import render_template, request, flash, redirect
from flask_mail import Mail, Message

mail = Mail(app)

class Contato:
    def __init__(self, nome, telefone, email, setor, mensagem):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.setor = setor
        self.mensagem = mensagem
        

# Rotas principais
@app.route('/')
def home():
    return render_template(
        r'homepage.html'
    )

@app.route('/institucional')
def institucional():
    return render_template(
        r'institucional.html'
    )


@app.route('/nosso_ensino')
def nosso_ensino():
    return render_template(
        r'niveisEnsino.html'
    )

@app.route('/nosso_ensino/educacao-infantil')
def educacao_infantil():
    return render_template(
        r'ed-infantil.html'
    )

@app.route('/nosso_ensino/ensino-fundamental')
def ensino_fundamental():
    return render_template(
        r'ensino-fund.html'
    )

@app.route('/nosso_ensino/ensino-medio')
def ensino_medio():
    return render_template(
        r'ensino-medio.html'
    )

@app.route('/secretaria_virtual')
def secretaria_virtual():
    return '<h1>Secretaria Virtual</h1>'


@app.route('/faculdade_cci')
def faculdade_cci():
    return '<h1>Faculdade CCI</h1>'


@app.route('/noticias')
def noticias():
    return '<h1>Noticias</h1>'


@app.route('/multimidia_cci')
def multimidia_cci():
    return '<h1>Multimidia</h1>'


@app.route('/contato')
def contato():
    return '<h1>Contato</h1>'

@app.route('/biblioteca')
def biblioteca():
    return render_template(
        r'biblioteca.html'
    )
@app.route('/funcionamento')
def funcionamento():
    return render_template(
        r'funcionamento.html'
    )
@app.route('/missao')
def missao():
    return render_template(
        r'missao.html'
    )
@app.route('/principios')
def principios():
    return render_template(
        r'principios.html'
    )
@app.route('/projeto')
def projeto():
    return render_template(
        r'projetoSocio.html'
    )
@app.route('/transportes')
def transportes():
    return render_template(
        r'transportes.html'
    )
@app.route('/regimento')
def regimento():
    return render_template(
        r'regimento.html'
    )
@app.route('/inicio')
def inicio():
    return render_template(
        r'inicio.html'
    )
@app.route('/secretaria')
def secretaria():
    return render_template(
        r'secretaria.html'
    )

@app.route('/fale_conosco')
def fale_conosco():
    return render_template(
        r'fale-conosco.html'
    )

@app.route('/fale_conosco/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['nome'],
            request.form['telefone'],
            request.form['email'],
            request.form['setor'],
            request.form['mensagem']    
        )

        if formContato.setor == "Coord":
            email_envio = 'cairo.alvcosta@gmail.com'
            setor = "Coordenadores e SOE"
        elif formContato.setor == "Dir":
            email_envio = 'suporte@portalcci.com.br'
            setor = "Direção"
        elif formContato.setor == "Tecs":
            email_envio = 'cairo.costa@portalcci.com.br'
            setor = 'Escola Técnica'
        elif formContato.setor == "Fac":
            email_envio = 'sosthenes@portalcci.com.br'
            setor = 'Faculdade'
        elif formContato.setor == "Setape":
            email_envio = 'setape@portalcci.com.br'
            setor = 'SETAPE'
        elif formContato.setor == "Sec":
            email_envio = 'candidato@portalcci.com.br' 
            setor = 'Secretaria'   

        msg = Message(
            subject= f'{formContato.nome} entrou em contato atraves do Fale Conosco',
            sender= app.config.get("MAIL_USERNAME"),
            recipients=[email_envio],
            body= f'''
                {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem para o setor {setor}:

                {formContato.mensagem}

            '''
        )
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/fale_conosco')