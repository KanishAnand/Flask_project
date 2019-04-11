from flask import Flask, render_template
app = Flask(__name__)

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



if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
