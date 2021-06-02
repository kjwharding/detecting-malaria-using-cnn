# Optimizer Adjustment
Apart from changing the model’s complete architecture, the last thing that I needed to investigate was the different optimizers. Optimizers are algorithms that adjust attributes within a neural network, specifically weights and learning rate to minimise loss. Originally, I was using the Adam (Adaptive Moment Estimation) optimizer but wanted to explore other frequently used optimizers and what effects they had on my custom CNN model. These are:
* SGD (Stochastic Gradient Descent)
* RMSprop (Root Mean Squared Propagation)

*Note: All graphs start at epoch 0 (e.g. epoch 1 is 0 on the graph).*

### SGD
Figure 1, 2 and 3 represent the training of a custom CNN model which use the SGD optimizer, but increasingly have more epochs. I found that the SGD optimizer took longer to find a more optimal solution, but eventually had better validation accuracy over the Adam optimizer. For example, in figure 3 the model achieved validation accuracy of 0.962 and validation loss of 0.125. This was found at the 78th epoch (77th in the graph and [csv]( /models/colour_model_3/sgd_all/sgd_e100/colour_model_3_sgd_100e_data.csv)). This was the best solution found so far. 

*Figure 1: Custom CNN with SGD optimizer (10 epochs).*
* Validation Accuracy (of last epoch): 0.949

![Graph 1](/models/colour_model_3/sgd_all/sgd_e10/colour_model_3_sgd_10e_graph_v2.png)

*Figure 2: Custom CNN with SGD optimizer (100 epochs).*
* Validation Accuracy (of last epoch): 0.958

![Graph 2](/models/colour_model_3/sgd_all/sgd_e100/colour_model_3_sgd_100e_graph_v2.png)

*Figure 3: Custom CNN with SGD optimizer (250 epochs).*
* Validation Accuracy (of last epoch): 0.955

![Graph 3](/models/colour_model_3/sgd_all/sgd_e250/colour_model_3_sgd_graph_v2.png)

### SGD from the NIH custom model
```
sgd = SGD(lr=1e-6, decay=1e-6, momentum=0.9, nesterov=True)
```
The tweaked SGD optimizer can be found via the NIH [here]( https://github.com/sivaramakrishnan-rajaraman/CNN-for-malaria-parasite-detection/blob/master/Custom%20CNN%20for%20Malaria%20Parasite%20Detection.ipynb). I decided to use the optimizer used by the NIH to visualise its effect on my custom CNN. I found that this model would most likely take hundreds of epochs to find a good solution, so would be impractical to train on my hardware. Please note that figure 4 has a different perspective to any of the graphs found on this page. 

*Figure 4: Custom CNN with SGD optimizer used in NIH custom model (10 epochs).*
* Validation Accuracy (of last epoch): 0.523

![Graph 4](/models/colour_model_3/sgd_all/sgd_nih_e10/colour_model_3_sgd_nih_10e_graph_v3.png)


### RMSprop
I found that when using RMSprop, the model converges very quickly, but doesn’t find an optimal solution (see figure 5). Instead the model only finds a ‘good’ solution. 

*Figure 5: Custom CNN with RMSprop optimizer (10 epochs).*
* Validation Accuracy (of last epoch): 0.891

![Graph 5](/models/colour_model_3/rmsprop_e10/colour_model_3_rmsprop_10e_graph_v2.png)

### Summary
I concluded that the SDG optimizer would be optimal for this problem space. This is due to the high validation accuracy and minimized validation loss achieved by the model using the SDG optimizer. The relevant details can be found in the summaries above. 

[Return to 'README.md'](../../README.md)
