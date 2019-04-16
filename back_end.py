from adder_4bit import *
from adder_5bit import *
import json
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db=SQLAlchemy(app)

class input(db.Model): #Class to implement database
	id = db.Column(db.Integer,primary_key=True)
	value_1 = db.Column(db.String(10),unique=False)
	value_2 = db.Column(db.String(10),unique=False)

	def __init__(self,val_1,val_2):
		self.value_1 = val_1
		self.value_2 = val_2

class submission(db.Model): #Class to implement submission for quiz
	id = db.Column(db.Integer,primary_key=True)
	sub = db.Column(db.Integer,unique=False)

	def __init__(self,arr):
		self.sub = arr;

#BACKEND_ROUTES
@app.route("/quiz",methods=['GET','POST'])    #Quiz section backend implemented here
def quiz():
	sub = request.json;
	print(sub);
	db.create_all()
	sb = submission("4");
	db.session.add(sb)
	db.session.commit()
	return "True";

@app.route("/calculate",methods=['GET','POST'])  #TO CALCULATE THE ANSWERS WHEN TWO BINARY NUMBERS ARE SENT FOR PROCESSING
def calculate():
	print(request.is_json)
	var_1 = request.json['var_1']
	var_2 = request.json['var_2']
	db.create_all()
	val = input(var_1,var_2)
	db.session.add(val)
	db.session.commit()
	return fun(var_1,var_2);

@app.route("/calculate_5bit",methods=['GET','POST'])  #TO CALCULATE THE ANSWERS WHEN TWO BINARY 5-bit NUMBERS ARE SENT FOR PROCESSING
def calculate_5bit():
	print(request.is_json)
	var_1 = request.json['var_1']
	var_2 = request.json['var_2']
	db.create_all()
	val = input(var_1,var_2)
	db.session.add(val)
	db.session.commit()
	return fun_5bit(var_1,var_2);

#FRONTEND_ROUTES
@app.route("/")
@app.route("/introduction")
def render_introduction():
	return render_template("Introduction.html")

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
