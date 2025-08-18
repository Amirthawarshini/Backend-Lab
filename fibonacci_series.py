from flask import Flask, request

app = Flask(__name__)

@app.route('/fibonacci')
def fibonacci():
    n = int(request.args.get('n', 10))
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return str(result)

if __name__ == '__main__':
    app.run()