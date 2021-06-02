import tensorflow as tf 
from tensorflow.keras import layers, callbacks
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt 
import csv

################################################################################
# define params
################################################################################
MODEL_NAME = "colour_model_3"

TRAIN_DATA = r"C:\ce301_harding_kiernan_j_w\dataset\augmented\training_set"
VAL_DATA = r"C:\ce301_harding_kiernan_j_w\dataset\augmented\validation_set"
IMG_DIMENSION = 100
BATCH_SIZE = 32
EPOCHS = 100

################################################################################
# preprocessing
################################################################################
training_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    directory=TRAIN_DATA, 
    batch_size=BATCH_SIZE,
    image_size=(IMG_DIMENSION, IMG_DIMENSION)
)
validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    directory=VAL_DATA,
    batch_size=BATCH_SIZE,
    image_size=(IMG_DIMENSION, IMG_DIMENSION)
)

# caching images in memory to improve training performance
AUTOTUNE = tf.data.experimental.AUTOTUNE
training_dataset = training_dataset.cache().prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.cache().prefetch(buffer_size=AUTOTUNE)

################################################################################
# creating model
################################################################################
model = Sequential([layers.experimental.preprocessing.Rescaling(
    1./255, 
    input_shape=(IMG_DIMENSION, IMG_DIMENSION, 3)),

    # 32 = no. of files the convolutional layers will learn from at a time
    # 3,3 = the convolution window (or kernal size)
    layers.Conv2D(32, 3, padding="same"),

    # applying the rectified linear activation function
    # in basic terms - return 0 if negative / x if positive
    layers.Activation("relu"),

    # used to reduce the spatial size of the representation
    layers.MaxPooling2D(pool_size=(2,2)),

    # applying dropout
    layers.Dropout(0.5),

    layers.Conv2D(32, 3, padding="same"),
    layers.Activation("relu"),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Dropout(0.5),

    layers.Conv2D(32, 3, padding="same"),
    layers.Activation("relu"),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Dropout(0.5),
    
    # dense layer requires a 1D dataset
    layers.Flatten(),

    # fully connected layers
    layers.Dense(128),
    layers.Activation("relu"),
    layers.Dense(2)
])

model.summary()

################################################################################
# compile model
################################################################################
model.compile(
    optimizer="sgd",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"]
)

################################################################################
# visualise training data
################################################################################
checkpoint = callbacks.ModelCheckpoint(MODEL_NAME + "_{epoch:03d}", period=1)

model_hist = model.fit(
    training_dataset,
    validation_data=validation_dataset,
    epochs=EPOCHS,
    callbacks=[checkpoint]
)

# retrieving data
accuracy = model_hist.history["accuracy"]
val_accuracy = model_hist.history["val_accuracy"]
loss = model_hist.history["loss"]
val_loss = model_hist.history["val_loss"]
epochs_range = range(EPOCHS)

# full overview
plt.figure(figsize=(21, 7))
plt.subplot(1, 2, 1)
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.plot(epochs_range, accuracy, label="Training Accuracy")
plt.plot(epochs_range, val_accuracy, label="Validation Accuracy")
plt.ylim([0.0, 1.0])
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy")

plt.subplot(1, 2, 2)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.plot(epochs_range, loss, label="Training Loss")
plt.plot(epochs_range, val_loss, label="Validation Loss")
plt.ylim([0.0, 1.0])
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")
plt.savefig(MODEL_NAME + "_graph_v1.png")

# targeted overview
plt.figure(figsize=(21, 7))
plt.subplot(1, 2, 1)
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.plot(epochs_range, accuracy, label="Training Accuracy")
plt.plot(epochs_range, val_accuracy, label="Validation Accuracy")
plt.ylim([0.7, 1.0])
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy")

plt.subplot(1, 2, 2)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.plot(epochs_range, loss, label="Training Loss")
plt.plot(epochs_range, val_loss, label="Validation Loss")
plt.ylim([0.0, 0.5])
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")
plt.savefig(MODEL_NAME + "_graph_v2.png")

# automatic overview
plt.figure(figsize=(21, 7))
plt.subplot(1, 2, 1)
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.plot(epochs_range, accuracy, label="Training Accuracy")
plt.plot(epochs_range, val_accuracy, label="Validation Accuracy")
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy")

plt.subplot(1, 2, 2)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.plot(epochs_range, loss, label="Training Loss")
plt.plot(epochs_range, val_loss, label="Validation Loss")
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")
plt.savefig(MODEL_NAME + "_graph_v3.png")

################################################################################
# output training data to csv
################################################################################
with open(MODEL_NAME + "_data" + ".csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(epochs_range)
    writer.writerow(accuracy)
    writer.writerow(val_accuracy)
    writer.writerow(loss)
    writer.writerow(val_loss)

################################################################################
# output model and data
################################################################################
model.save(MODEL_NAME + ".model")