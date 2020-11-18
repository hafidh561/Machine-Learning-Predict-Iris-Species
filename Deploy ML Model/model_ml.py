from tensorflow.keras.models import load_model


def predict_input(sl, sw, pl, pw):
	model = load_model('iris_model.h5')
	result = model.predict_classes([[sl, sw, pl, pw]])
	if result == 0:
		return 'Species Setosa'
	elif result == 1:
		return 'Species Versicolor'
	elif result == 2:
		return 'Species Virginica'
