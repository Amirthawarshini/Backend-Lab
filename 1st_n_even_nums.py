
from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def even_numbers(n):
    evens = [str(i * 2) for i in range(1, n + 1)]
    return f"The first {n} even numbers are: {', '.join(evens)}"

if __name__ == '__main__':
    app.run()
