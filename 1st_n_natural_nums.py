
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome! Use /naturals/<n> to get the first N natural numbers.'

@app.route('/naturals/<int:n>')
def naturals(n):
    numbers = ', '.join(str(i) for i in range(1, n + 1))
    return f'The first {n} natural numbers are: {numbers}'

if __name__ == '__main__':
    app.run()
