from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def hello_world():
    return render_template("index.html")

@app.route("/predictions",methods= ['GET','POST'])
def predict():
    return "Here you have the predictions"

if __name__ == "__main__":
    app.run(port= 3000, debug = True)