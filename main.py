from flask import Flask,redirect,url_for,request,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/login')
def login():
   
    return render_template('simpleform.html')

@app.route('/login_success')
def login_success():
    user = request.args.get('input_box')
    return redirect(url_for('main',name=user))

@app.route('/<name>/')
def main(name):
    return render_template('greeting.html',user=name)



if __name__=='__main__':
    app.run(debug=True)