 # Parte 1: API Flask

# flask_api/app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    """
    GET /saudacao?nome=SeuNome
    Retorna: 'Olá, SeuNome!'
    """
    nome = request.args.get('nome', '').strip()
    if nome:
        return f'Olá, {nome}!'
    # Se não vier parâmetro nome, retorna saudação genérica
    return 'Olá!'

@app.route('/soma', methods=['POST'])
def soma():
    """
    POST /soma
    Recebe JSON: { "a": número, "b": número }
    Retorna JSON: { "soma": <a + b> }
    """
    data = request.get_json(force=True)  # força parsing JSON, devolve 400 se não for válido
    a = data.get('a')
    b = data.get('b')

    # Validação básica
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({'error': 'Informe dois números válidos em "a" e "b".'}), 400

    return jsonify({'soma': a + b})

if __name__ == '__main__':
    # Roda em http://127.0.0.1:5000 por padrão
    app.run(debug=True)
