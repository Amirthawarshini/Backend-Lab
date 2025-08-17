
from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def primes(n):
    count = 0
    num = 2
    result = ""
    while count < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            result += str(num) + ", "
            count += 1
        num += 1
    return f"The first {n} prime numbers are: {result.rstrip(', ')}"

if __name__ == '__main__':
    app.run()
