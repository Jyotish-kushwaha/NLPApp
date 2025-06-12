from flask import Flask ,render_template,request, redirect, url_for
from db import Database
from flask import request, redirect, flash, session, render_template
from myapi import MyAPI



app=Flask(__name__)
app.secret_key = 'myverysecurekey123'

dbo=Database()
api=MyAPI()



@app.route('/')
def register():
    return render_template('register.html')

@app.route('/register')
def register_page():
    return render_template('register.html')


@app.route('/perform_registeration', methods=['POST'])
def perform_registeration():
   username=request.form['name']
   password=request.form['password']
   email=request.form['email']
   response = dbo.insert(username, email, password)
   if response:
       flash('Registration successful!','success')
       return redirect('/login')
   else:    
       flash('Email already exists!','error')
       return redirect('/register')
  
   
   
   
      
@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/perform_login', methods=['POST'])
def perform_login():
    username = request.form['email']
    password = request.form['password']
    
    response = dbo.login(username, password)
    if response:
        
        flash('Login successful! Welcome, '  , 'success')
        return redirect('/home')  # redirect to home page
    else:
        flash('Invalid credentials! Please try again.', 'error')
        return redirect('/login')  # redirect back to login

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')



@app.route('/perform_sentiment', methods=['POST'])
def perform_sentiment():
    text = request.form['text']
    api_response = api.sentiment_analysis(text)
    
    return render_template('sentiment.html', result=api_response)


    




@app.route('/language')
def language():
    return  render_template('language.html')

@app.route('/perform_language',methods=['POST'])
def perform_language():
    text=request.form['text']
    api_response = api.language_detection(text)
    return render_template('language.html', result=api_response)

@app.route('/semantic')
def semantic():
    return render_template('semantic.html ')

@app.route('/perform_semantic',methods=['POST'])
def perform_semantic():
    text1 = request.form['text1']
    text2=request.form['text2']
    api_response=api.semantic_analysis(text1, text2)
    return render_template('semantic.html', result=api_response)

if __name__ == '__main__':
    app.run(debug=True)