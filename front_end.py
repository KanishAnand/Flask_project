from t import *
from t_5 import *
import json
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


#ROUTES
@app.route("/")
@app.route("/introduction")
def render_introduction():
	return render_template("Introduction.html")

@app.route("/calculate",methods=['GET','POST'])  #TO CALCULATE THE ANSWERS WHEN TWO BINARY NUMBERS ARE SENT FOR PROCESSING
def calculate():
	#print("dfs")
	#print(request.is_json)

	var_1 = request.json['var_1']
	var_2 = request.json['var_2']
	# db = SQLAlchemy();
	# db.inti_app(app)
	
	#db.create_all()
	# db.session.add(var_1);
	# db.session.add(var_2);
	# db.session.commit();
	# obj = json.loads(data)
	# print(obj['var_1'])
	#print(var_1)
	#print(var_2)
	return fun(var_1,var_2);

@app.route("/calculate_5bit",methods=['GET','POST'])  #TO CALCULATE THE ANSWERS WHEN TWO BINARY 5-bit NUMBERS ARE SENT FOR PROCESSING
def calculate_5bit():
	print("dfs")
	print(request.is_json)
	var_1 = request.json['var_1']
	var_2 = request.json['var_2']
	# obj = json.loads(data)
	# print(obj['var_1'])
	print(var_1)
	print(var_2)
	return fun_5bit(var_1,var_2);

@app.route('/theory')
def render_theory():
    return render_template('Theory.html')

@app.route('/objective')
def render_objective():
    return render_template('Objective.html')

@app.route('/experiment')
def render_experiment():
    return render_template('Experiment.html')

@app.route('/exp')
def render_exp():
    return render_template('exp.html')

@app.route('/exp_5bit')
def render_exp_5bit():
	return render_template('exp_5bit.html')

@app.route("/help")
def render_help():
	return render_template('help.html')

@app.route('/function')
def function():
    return 5

@app.route('/manual')
def render_manual():
    return render_template('Manual.html')


@app.route('/quizzes')
def render_quizzes():
    return render_template('Quizzes.html')

@app.route('/procedure')
def render_procedure():
	return render_template('Procedure.html')

@app.route('/refrences')
def render_refrences():
	return render_template('Refrences.html')

@app.route('/feedback')
def render_feedback():
	return render_template('Feedback.html')


#TO RUN ON LOCALHOST AT PORT 5000
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
