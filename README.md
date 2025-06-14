# CropLeaf Disease Detection

## Overview

This project implements a deep learning model using TensorFlow to classify plant leaf diseases from images. The model is designed to identify 38 different classes of crop diseases, leveraging a convolutional neural network (CNN) architecture for image classification. A Flask web application has been developed to provide a user interface for uploading images, displaying disease predictions, and recommending remedies through a shopping system, though the shopping system’s backend is still under development.

## Project Description

The CropLeaf Disease Prediction project aims to automate the identification of plant diseases by analyzing images of crop leaves. Using a convolutional neural network (CNN), the model classifies leaf images into one of 38 disease categories, enabling early detection of plant health issues. This is particularly valuable in agriculture, where timely identification of diseases can prevent crop loss and improve yield.

## Flask Web Application

A Flask-based web application has been developed to make the model accessible to users. The app currently allows users to:





Upload leaf images through a web interface.



Receive instant predictions about potential crop diseases with confidence scores.



View disease classification results and basic information.

Additionally, a shopping system has been introduced to recommend remedies or medicines for the identified crop diseases. The frontend for the shopping system is complete, featuring a product catalog, cart, and checkout interface. The backend, which will handle product retrieval, order processing, and integration with disease predictions, is still under development. Once fully implemented, the shopping system will enhance the app’s utility by providing actionable treatment options.

## Shopping System for Remedies

The shopping system is designed to recommend and sell remedies (e.g., pesticides, fungicides, or organic treatments) tailored to the predicted crop disease. Key features include:





Disease-Specific Recommendations: After a disease is predicted, the app displays relevant products mapped to that disease, along with details like product name, description, price, and application instructions.



Product Catalog: A browsable list of remedies, filterable by crop or disease, with options to add items to a cart.



Cart and Checkout: Users can add products to a cart, review their selections, and proceed to a checkout page (currently frontend-only).



## Benefits:





Actionable Solutions: Farmers receive not only disease diagnoses but also immediate access to treatments, streamlining the response process.



Convenience: A one-stop platform for diagnosis and remedy purchase, reducing the need to consult multiple sources.



Education: Product descriptions include usage instructions, helping farmers apply treatments correctly.



Revenue Potential: The shopping system can support agricultural businesses by facilitating direct sales of remedies.

The backend implementation will involve:





A database to store product details and map diseases to remedies.



API endpoints to retrieve products, manage the cart, and process orders.



Integration with the disease prediction pipeline to recommend products based on the model’s output.



## Usefulness in a Web Application

When fully integrated with a backend, the Flask app will offer significant practical benefits:





### Farmer Accessibility: 
Farmers can upload leaf images via a browser or mobile device and receive instant disease predictions, making it accessible even in remote areas with internet access.



### Real-Time Diagnostics: 
The app will provide real-time disease classification, enabling farmers to take immediate action, such as applying targeted treatments or isolating affected crops.



### Scalability: 
The web-based platform can serve multiple users simultaneously, supporting agricultural communities, cooperatives, or extension services in monitoring crop health across large regions.



### User-Friendly Interface: 
The app will display results in a clear format, including disease names, confidence scores, and actionable insights, making it easy for non-technical users to understand.



### Data Collection and Insights: 
The app can collect user-submitted images and predictions, building a database for further analysis or model improvement, and providing insights into regional disease trends.



### Integration with IoT: 
The model can be linked with IoT devices (e.g., drones or cameras) for automated image capture and analysis, enhancing precision agriculture workflows.

By deploying this model in a Flask web application, it becomes a powerful tool for farmers, agronomists, and agricultural organizations to monitor and manage crop health efficiently, reducing economic losses and promoting sustainable farming practices.

## Dataset

The dataset consists of images of crop leaves, divided into training and validation sets:





Training Set: 70,295 images across 38 classes.



Validation Set: 17,572 images across 38 classes.



Image Preprocessing: Images are resized to 128x128 pixels, with RGB color mode, and batched with a size of 32.

## Model Architecture

The model is a Sequential CNN built using TensorFlow/Keras, designed to avoid overshooting and overfitting:





### Convolutional Layers:





Five blocks of Conv2D layers with increasing filters (32, 64, 128, 256, 512).



Each block includes two Conv2D layers with ReLU activation, followed by MaxPooling2D.



Padding is set to 'same' for the first Conv2D layer in each block.



### Dropout Layers:





25% dropout after the final convolutional block.



40% dropout before the output layer to prevent overfitting.



### Fully Connected Layers:





Flattened layer followed by a Dense layer with 1500 units (ReLU activation).



Output layer with 38 units (softmax activation) for multi-class classification.



### Optimizer: 
Adam with a learning rate of 0.0001.



### Loss Function: 
Categorical Crossentropy.
