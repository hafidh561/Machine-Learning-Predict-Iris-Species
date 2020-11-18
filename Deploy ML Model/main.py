from flask import Flask, render_template

from forms import DataFormfrom model_ml import predict_input

app = Flask(__name__)

app.config['SECRET_KEY'] = '0f551dada7d7bcc38d1b10a73cd3e3b4'


@app.route("/", methods=['GET', 'POST'])
def index():
	form = DataForm()
	if form.validate_on_submit():
		sl = form.sepal_length.data
		sw = form.sepal_width.data
		pl = form.petal_length.data
		pw = form.petal_width.data
		result = predict_input(sl, sw, pl, pw)
		return render_template('index.html', form=form, title='Predict Iris Species', result=result)
	else:
		return render_template('index.html', form=form, title='Predict Iris Species', result='')


if __name__ == "__main__":
	app.run()
