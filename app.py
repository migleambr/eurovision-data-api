from flask import Flask
from routes.HistoryRoutes import history_bp

app = Flask(__name__)

# registering the history blueprint
app.register_blueprint(history_bp)

if __name__ == '__main__':
    app.run(debug=True)
