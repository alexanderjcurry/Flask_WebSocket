from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def background_thread():
    count = 0
    while True:
        socketio.sleep(5)
        count += 1
        print(f"Emitting a new log entry: {count}")
        socketio.emit('log_update', {'data': f'Log entry #{count}'})

if __name__ == '__main__':
    socketio.start_background_task(background_thread)
    socketio.run(app, debug=True, use_reloader=False)  # Disable the reloader or else connections will be dropped