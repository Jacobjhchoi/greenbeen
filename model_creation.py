import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Create training and test directories
train_dir = "Organic or Recycle or Trash Dataset\TEST"
test_dir = "Organic or Recycle or Trash Dataset\TRAIN"

# Create data inputs
IMAGE_SHAPE = (224, 224)
BATCH_SIZE = 32
train_datagen = ImageDataGenerator(rescale=1/255.,
                                   rotation_range=20,# rotate the image slightly between 0 and 20 degrees (note: this is an int not a float)
                                   shear_range=0.2,  # shear the image
                                   zoom_range=0.2,  # zoom into the image
                                   width_shift_range=0.2,  # shift the image width ways
                                   height_shift_range=0.2,  # shift the image height ways
                                   horizontal_flip=True)  # flip the image on the horizontal axis

test_datagen = ImageDataGenerator(rescale=1/255.)  # flip the image on the horizontal axis

print("Training images:")
train_data = train_datagen.flow_from_directory(train_dir,
                                               target_size=IMAGE_SHAPE,
                                               batch_size=BATCH_SIZE,
                                               class_mode='binary')

print("Testing images:")
test_data = train_datagen.flow_from_directory(test_dir,
                                              target_size=IMAGE_SHAPE,
                                              batch_size=BATCH_SIZE,
                                              class_mode='binary')

# Custom model
model_1 = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(10, 3, activation="relu", input_shape=(224, 224, 3)),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1, activation="sigmoid")
])


model_1.compile(loss="binary_crossentropy",
                optimizer=tf.keras.optimizers.Adam(lr=(0.001)),
                metrics=["accuracy"])

history_1 = model_1.fit(train_data,
                        epochs=2,
                        steps_per_epoch=len(train_data))

# Save model using the HDF5 format
# model_1.save("model_1_2") # note the addition of '.h5' on the end
