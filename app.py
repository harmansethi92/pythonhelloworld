from flask import Flask
app = Flask(__name__)

PORT = 5000
@app.route("/")
def hello():
<<<<<<< HEAD
    return "Hello World"
=======
    return "Hello World!!"
>>>>>>> d5306fac859717c08a5af7b6a453a75be20f8393
if __name__ == "__main__":
    app.run(host="0.0.0.0",port= PORT)

