![Malaria Project](imgs/logos/read_me_logo.png)

# Detecting Malaria Parasites in Red Blood Cells using Machine Learning
* Name: **Kiernan Harding**
* Supervisor: **Dr Alba Garcia Seco De Herrera**
* Second Assessor: **Dr John O'Hara**
* Grade: **Pending**
* Dataset: [National Institutes of Health](https://lhncbc.nlm.nih.gov/LHC-publications/pubs/MalariaDatasets.html)

## Abstract
Malaria has a major impact on global health, with an estimated 229 million cases and more than 409,000 deaths worldwide in 2019 alone. Most of these cases occur in less economically developed countries where the testing facilities are poor. Typically, the malaria testing procedure requires microscopists to manually count the malaria parasites in red blood cell samples. The calibre of this process depends on the proficiency of the microscopist and facility quality. Therefore, to eliminate human error and increase testing speed, Machine Learning (ML) can be used to automate the testing process.

I specifically utilise a Convolutional Neural Network (CNN) to classify red blood cells as either parasitized or healthy. To iteratively increase my classifiers’ accuracy, I use a broad range of ML techniques such as: data augmentation, regularisation, and feature map visualisation. Using these techniques, the model has so far achieved an accuracy of 95.6% on previously unseen test samples.

To accommodate the classifier, I design a convenient application with an intuitive interface. It is vital that the application has wide accessibility, as its main use is in less economically developed countries. Consequently, the application can be used on almost any device.

## Final Report

Please find a download for my final report [here](submissions/report/final_report.pdf).


## Technical Documentation
##### 1. Understanding CNNs in Code
* [Setting up the Environment](practice/docs/environment.md)
* [Implementing a CNN](practice/docs/implementing.md)

##### 2. Designing Custom CNN Models
* [Initial Greyscale Model](models/docs/initial_greyscale.md)
* [Initial Colour Model](models/docs/initial_colour.md)
* [Improving the Model](models/docs/improving_model.md)
    * [Data Visualisation](models/docs/data_visualisation.md)
    * [Data Augmentation](models/docs/data_augmentation.md)
    * [Regularisation](models/docs/regularisation.md)
    * [Optimizer Adjustment](models/docs/optimizer.md)
    * [Feature Map Visualisation](models/docs/feature_maps.md)
* [Evaluation & Results](models/docs/results.md)
* [Discussion](models/docs/discussion.md)

##### 3. Application Design
* [Implementation](web_app/docs/implementation.md)
* [Styling](web_app/docs/styling.md)
* [Examples](web_app/docs/examples.md)

##### 4. Installation & Usage
* [Training Custom Models](models/docs/install.md)
* [Application](web_app/docs/install.md)