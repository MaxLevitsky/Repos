from flask import Flask
1
2
3
4
5
14

app= Flask(__name__)

@app.route("/hello/<name>")
def hello_world(name):
    return "<p>Hello?{name}</p>"

app.run()