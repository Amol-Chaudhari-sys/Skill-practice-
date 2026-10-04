from flask import Flask , render_template

app= Flask(__name__)

@app.route("/")
def helloworld():
    return '<h1> Hello World <h1>'

@app.route("/welcome/<name>")
def welcome(name):
    return "<h1>welcome user  "+name +" ! <h1>"

@app.route("/wel/")
def wel():
    return render_template("index.html")



if __name__=="__main__":
    app.run (debug=True )