from errno import EDEADLOCK
from django.shortcuts import render
from flask import Flask,render_template,request
app=Flask(__name__,static_folder='templates')
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        edad=int(request.form['txtedad'])
        if edad>=18:
            res="Eres mayor de edad"
            return render_template("index.html",res=res)
        else:
            res="Eres menor de edad"
            return render_template("index.html",res=res)
    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)