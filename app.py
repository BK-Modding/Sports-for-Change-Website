from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/register')
def register():
    return render_template('registration.html')
    
@app.route('/termsandconditions')
def t_and_c():
    return render_template('t&c.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)