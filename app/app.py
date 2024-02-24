from flask import Flask

app=Flask(__name__)
app.json.ensure_ascii=False

@app.route("/")
def hello():
    return "Hello, World!!!!!!!!"

if __name__ == '__main__':
    app.run()
