from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store messages in memory (not recommended for production, use a database)
messages = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    messages.append(message)
    return '', 204  # HTTP 204 No Content: Success, no response needed


@app.route('/get_messages')
def get_messages():
    return jsonify(messages)


if __name__ == '__main__':
    app.run(debug=True)
