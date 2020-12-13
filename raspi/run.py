from api import create_app, socketio
from flask_socketio import SocketIO

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    socketio.run(app, debug=True, host='0.0.0.0')
