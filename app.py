from flask import Flask
app = Flask(__name__)

PORT = 5000
@app.route("/")
def hello():
	return "Presto Magico!"
if __name__ == "__main__":
    app.run(host="0.0.0.0",port= PORT)

