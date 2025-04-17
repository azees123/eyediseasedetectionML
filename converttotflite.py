import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model('eye_disease_model.h5')

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the converted model
with open('eye_disease_model.tflite', 'wb') as f:
    f.write(tflite_model)
