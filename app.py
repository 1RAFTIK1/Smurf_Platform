from flask import Flask, render_template
from flask_cors import CORS
from database import db
from routes import setup_routes

app = Flask(__name__)
CORS(app)  # Для разрешения CORS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knowledge_assistant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # Создание таблиц

setup_routes(app)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)