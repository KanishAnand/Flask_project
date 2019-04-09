from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home")
def render_static():
	return render_template("Introduction.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)