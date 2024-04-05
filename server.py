from flask import Flask, request

app = Flask(__name__)
shutdown_flag = False


@app.route('/set_flag', methods=['POST'])
def set_flag():
    global shutdown_flag
    data = request.json
    shutdown_flag = data['flag']
    return 'Flag set successfully'


@app.route('/get_flag', methods=['GET'])
def get_flag():
    global shutdown_flag
    return {'flag': shutdown_flag}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
