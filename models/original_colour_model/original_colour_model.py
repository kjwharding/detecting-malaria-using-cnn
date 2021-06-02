import tensorflow as tf 
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

# define params
DATA_DIR = r"C:\ce301_harding_kiernan_j_w\dataset\original\training_set"
CATEGORIES = ["parasitized", "uninfected"]
IMG_DIMENSION = 100
BATCH_SIZE = 32

# preprocessing
training_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    DATA_DIR, 
    validation_split=0.2,
    subset="training",
    seed=0,
    image_size=(IMG_DIMENSION, IMG_DIMENSION),
    batch_size=BATCH_SIZE
)
validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    DATA_DIR, 
    validation_split=0.2,
    subset="validation",
    seed=0,
    image_size=(IMG_DIMENSION, IMG_DIMENSION),
    batch_size=BATCH_SIZE
)

# caching images in memory to improve training performance
AUTOTUNE = tf.data.experimental.AUTOTUNE
training_dataset = training_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.cache().prefetch(buffer_size=AUTOTUNE)

# creating base model to add layers to
model = Sequential([layers.experimental.preprocessing.Rescaling(
    1./255, 
    input_shape=(IMG_DIMENSION, IMG_DIMENSION, 3)),

    ######## first layer ########
    # 32 = no. of files the convolutional layers will learn from at a time
    # 3,3 = the convolution window (or kernal size)
    layers.Conv2D(32, 3, padding="same"),

    # applying the rectified linear activation function
    # in basic terms - return 0 if negative and x if positive
    layers.Activation("relu"),

    # used to reduce the spatial size of the representation
    layers.MaxPooling2D(pool_size=(2,2)),

    ######## second layer ########
    layers.Conv2D(32, 3, padding="same"),
    layers.Activation("relu"),
    layers.MaxPooling2D(pool_size=(2,2)),

    ######## third layer ########
    # dense layer requires a 1D dataset
    layers.Flatten(),

    # deeply connected layers
    layers.Dense(128),
    layers.Activation("relu"),
    layers.Dense(2)
])

# view model before output starts
model.summary()

# -- output --
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

model_history = model.fit(
    training_dataset,
    validation_data = validation_dataset,
    epochs = 16
)

model.save('malaria_classifier_colour.model')