from flask import Flask,redirect,url_for,request,render_template
import dbhandler #user-created file to handle data

app = Flask(__name__)


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


@app.route('/database')
def database_handler():
    data = dbhandler.get_data_from_database()
    return render_template('database_page.html',data=data)

@app.route('/images/')
def image_handler():
    return render_template('images_page.html')


if __name__=='__main__':
    app.run(debug=True)