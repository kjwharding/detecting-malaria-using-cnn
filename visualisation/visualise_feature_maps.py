from tensorflow.keras import layers
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import matplotlib.pyplot as plt 
import numpy as np
from tensorflow.keras.models import load_model

################################################################################
# define params
################################################################################
MODEL_NAME = "colour_model"
IMG_DIMENSION = 100
EXAMPLE_IMG = r"visualisation\imgs\h1.png"
model = load_model(r"C:\ce301_harding_kiernan_j_w\models\final\final.model", compile=True)
model.summary()

################################################################################
# creating feature maps
################################################################################

# get the list of layers
layer_outputs = [layer.output for layer in model.layers[1:]]

# create a visualisation model
visualise_model = Model(inputs=model.input, outputs=layer_outputs)

# load in image and rescale respectively
img_in = load_img(EXAMPLE_IMG, target_size=(100,100))
img = img_to_array(img_in)
img = np.reshape(img, (1, 100, 100, 3)) / 255

# get all feature maps for all layers
feature_maps = visualise_model.predict(img)
layer_names = [layer.name for layer in model.layers]

# plotting the feature map graph
model_layer = 0
for layer_names, feature_maps in zip(layer_names, feature_maps):
    if len(feature_maps.shape) == 4 :
        channels = feature_maps.shape[-1]
        size = feature_maps.shape[1]
        display_grid = np.zeros((size, size * channels))
        for ch in range(channels):
            ft_map = feature_maps[0, :, :, ch]
            ft_map -= np.mean(ft_map)
            ft_map /= np.std(ft_map)
            ft_map *= 50
            ft_map += 100
            ft_map = np.clip(ft_map, 0, 255).astype('uint8')
            
            display_grid[:, ch * size : (ch + 1) * size] = ft_map
            scale = 20. / channels

        # output feature map as an image
        plt.figure(figsize=(scale * channels, scale))
        plt.title(layer_names)
        plt.grid(False)
        plt.imshow(display_grid, aspect='auto', cmap='viridis')
        plt.savefig("visualisation\\tmp\\" + str(model_layer) + "_" + layer_names + "_" + MODEL_NAME + ".png", bbox_inches='tight')
        model_layer += 1

# modified from: https://www.youtube.com/watch?v=i3qjgJgQqgg&ab_channel=Pathshala
