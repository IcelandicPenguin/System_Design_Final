from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def welcome_page():
    return render_template ('Homepage.htm')
    

@app.route('/Management')
def Management():
    return render_template ('Manager.htm')

@app.route('/BookRoom')
def BookRoom():
    return render_template ('book room.htm')

@app.route('/ConfirmationPage')
def Confirmation():
    return render_template ('confirmation.htm')

@app.route('/',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
    return redirect(url_for('Management',name = user))

if __name__ == "__main__":
    app.run(debug=True)
