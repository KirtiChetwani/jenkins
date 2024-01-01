from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home_page(name=None):
    return render_template('index.html',name=name)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)