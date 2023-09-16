from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Lista de usuários cadastrados (apenas para fins de exemplo)
usuarios_cadastrados = []

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    # Lógica de validação da senha aqui (1 letra maiúscula, 1 número, 1 caractere especial, pelo menos 6 caracteres)
    if not (len(senha) >= 6 and any(c.isupper() for c in senha) and any(c.isdigit() for c in senha) and any(not c.isalnum() for c in senha)):
        flash('A senha deve conter pelo menos 6 caracteres, 1 letra maiúscula, 1 número e 1 caractere especial.')
        return redirect(url_for('index'))

    # Verifique se o usuário existe (aqui você pode usar uma lógica de banco de dados)
    if (email, senha) in usuarios_cadastrados:
        flash('Login bem-sucedido!')
        return redirect(url_for('index'))
    else:
        flash('Credenciais inválidas. Tente novamente.')
        return redirect(url_for('index'))

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    telefone = request.form['telefone']
    endereco = request.form['endereco']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']

    # Verifique se a senha e a confirmação da senha são iguais
    if senha != confirmar_senha:
        flash('A senha e a confirmação de senha não coincidem.')
        return redirect(url_for('cadastro'))

    # Salvar os dados do usuário (aqui você pode adicionar lógica de banco de dados)
    usuarios_cadastrados.append((email, senha))
    flash('Cadastro realizado com sucesso!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
