from flask import Flask, render_template, request
import tensorflow as tf

app = Flask(__name__)

loaded_model = tf.keras.models.load_model('./model/model_1.h5')
print("+"*50, "Model is loaded")

loaded_model.summary()


class_names = ['Compost', 'Recycle/Trash']

@app.route('/')
def index():
	return render_template("index.html", data="_____")

@app.route("/prediction", methods=["POST"])



def prediction():

	img = request.files['img']
	img.save('img.jpg')

	# Preprocess Image
	image = tf.io.read_file("img.jpg")
	image = tf.image.decode_jpeg(image)
	image = tf.image.resize(image, [224, 224])
	scale = True
	if scale:
		# Rescale the image (get all values between 0 and 1)
		image /= 255.
	else:
		image = image
	image = tf.expand_dims(image, axis=0)


	# predictions
	pred = loaded_model.predict(image)
	print(pred)

	if (pred < 0.5):
		pred_class = class_names[0]
	else:
		pred_class = class_names[1]
	print(pred_class)	

	return render_template("index.html", data=pred_class)


if __name__ == "__main__":
	app.run(debug=True)