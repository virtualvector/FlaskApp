from flask import Flask,redirect,url_for,request,render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return redirect(url_for('main',name="stranger"))

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