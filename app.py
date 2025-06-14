from flask import Flask ,render_template,request, redirect, url_for
from db import Database
from flask import request, redirect, flash, render_template,session
from myapi import MyAPI



app=Flask(__name__)
app.secret_key = 'myverysecurekey123'

dbo=Database()
api=MyAPI()
import pycountry

def get_language_name(code):
    try:
        language = pycountry.languages.get(alpha_2=code)
        return language.name
    except:
        return code  # fallback if code not found




@app.route('/')
def register():
    return render_template('register.html')

@app.route('/register')
def register_page():
    return render_template('register.html')


@app.route('/perform_registeration', methods=['POST','GET'])
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



@app.route('/perform_login', methods=['POST','GET'])
def perform_login():
    username = request.form['email']
    password = request.form['password']
    
    response = dbo.login(username, password)
    if response:
        session['logged_in']=True
        
        
        return redirect('/home')
    

    else:
        flash('Invalid credentials! Please try again.', 'error')
        return redirect('/login')  # redirect back to login
    
    

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect('/login')

@app.route('/home')
def home():
    if not session.get('logged_in'):
        flash('you need to login first','error')
        return redirect('/login')
    return render_template('home.html')

@app.route('/sentiment')
def sentiment():
    if not session.get('logged_in'):
        flash('you need to login first','error')
        return redirect('/login')
    return render_template('sentiment.html')



@app.route('/perform_sentiment', methods=['POST','GET'])
def perform_sentiment():
    if not session.get('logged_in'):
        flash('you need to login first','error')
        return redirect('/login')
    text = request.form['text']
    api_response = api.sentiment_analysis(text)
    
    return render_template('sentiment.html', result=api_response)


    




@app.route('/language')
def language():
    if not session.get('logged_in'):
        flash('you need to login first','error')
        return redirect('/login')
    return  render_template('language.html')

@app.route('/perform_language', methods=['POST','GET'])
def perform_language():
    if not session.get('logged_in'):
        flash('You need to login first', 'error')
        return redirect('/login')

    text = request.form['text']
    api_response = api.language_detection(text)  # {'de': 0.8571}

    lang_code = list(api_response.keys())[0]
    confidence = api_response[lang_code]
    lang_name = get_language_name(lang_code)

    return render_template('language.html', 
                           language=lang_name,
                           confidence=f"{confidence:.1%}")


        


@app.route('/semantic')
def semantic():
    if not session.get('logged_in'):
        flash('you need to login first','error')
        return redirect('/login')
    return render_template('semantic.html ')

@app.route('/perform_semantic', methods=['POST','GET'])
def perform_semantic():
    if not session.get('logged_in'):
        flash('You need to login first', 'error')
        return redirect('/login')

    text1 = request.form['text1']
    text2 = request.form['text2']
    
    api_response = api.semantic_analysis(text1, text2)
    similarity_score = api_response['score']

    similarity_percent = round(similarity_score * 100, 1)

    if similarity_score > 0.85:
        message = "The texts are very similar."
    elif similarity_score > 0.6:
        message = "The texts are somewhat similar."
    elif similarity_score > 0.4:
        message = "The texts are slightly related."
    else:
        message = "The texts are different."

    return render_template('semantic.html', 
                           similarity=similarity_percent,
                           message=message,
                           text1=text1,
                           text2=text2)


if __name__ == '__main__':
   import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # fallback to 10000
    app.run(host="0.0.0.0", port=port)

