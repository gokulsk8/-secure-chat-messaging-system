from flask import Flask, render_template, request
from cryptography.fernet import Fernet
from ciphers import rail_fence, row_transposition

app = Flask(__name__)

# Generate key (in real apps, store it safely!)
fernet_key = Fernet.generate_key()
cipher_suite = Fernet(fernet_key)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        message = request.form['message']
        mode = request.form['mode']
        cipher = request.form['cipher']

        if cipher == 'rail_fence':
            rails = int(request.form['rails'])
            if mode == 'encrypt':
                result = rail_fence.encrypt(message, rails)
            else:
                result = rail_fence.decrypt(message, rails)

        elif cipher == 'row_transposition':
            row_key = request.form['key']  # 🔄 renamed to avoid conflict
            if mode == 'encrypt':
                result = row_transposition.encrypt(message, row_key)
            else:
                result = row_transposition.decrypt(message, row_key)


    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
