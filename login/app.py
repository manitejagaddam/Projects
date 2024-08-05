from flask import Flask, render_template, request
# import dbapp as db
from dbapp import dbmanager as db

app = Flask(__name__)

class LoginForm:
    def __init__(self, app):
        self.app = app
        self.add_routes()

    def add_routes(self):
        @self.app.route('/register', methods=['POST'])
        def register():
            name = request.form.get('name')
            username = request.form.get('username')
            password = request.form.get('password')
            db.add_user(name, username, password)
            return 'Registration successful'

        @self.app.route('/submit', methods=['POST'])
        def login():
            username = request.form.get('username')
            password = request.form.get('password')
            print(username, password)
            if db.check_db(username, password):
                return render_template("home.html")
            else:
                return "Username/password is wrong"
            
        @self.app.route('/register', methods=['GET'])
        def register_page():
            return render_template('register.html')

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == "__main__":
    # Initialize route classes
    LoginForm(app)
    app.run(debug=True)
