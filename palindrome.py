from flask import Flask, request

app = Flask(__name__)

@app.route('/palindrome')
def palindrome():
    text = request.args.get('text', '')
    is_palindrome = text == text[::-1]
    return f"{text} is {'a' if is_palindrome else 'not a'} palindrome"

if __name__ == '__main__':
    app.run()