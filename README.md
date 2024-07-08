# Sign Language Recognition using SMNIST Dataset

This project is a Sign Language Recognition system using computer vision techniques. It utilizes the SMNIST dataset to train and evaluate a model capable of recognizing sign language gestures.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Results](#results)

## Introduction

This project aims to create a system that can recognize sign language gestures from images. Using the SMNIST dataset, which contains labeled images of sign language gestures, we train a neural network model to identify different signs accurately.

## Dataset

The SMNIST (Sign MNIST) dataset is a collection of labeled images of American Sign Language (ASL) gestures. It includes:
- Training images
- Validation images
- Test images

Each image is labeled with the corresponding sign language character.

## Features

- Data preprocessing and augmentation
- Convolutional Neural Network (CNN) model for gesture recognition
- Training and evaluation scripts
- Visualization of training progress and model performance

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/sign-language-recognition.git
    cd sign-language-recognition
    ```

2. **Install the required Python libraries**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Download the SMNIST dataset**:
    - Place the dataset files in the appropriate directory (e.g., `data/`).

## Usage

1. **Preprocess the data**:
    ```sh
    python preprocess_data.py
    ```

2. **Train the model**:
    ```sh
    python train.py
    ```

3. **Evaluate the model**:
    ```sh
    python evaluate.py
    ```

4. **Run predictions on new images**:
    ```sh
    python predict.py --image_path path_to_image
    ```

## Model

The model used for sign language recognition is a Convolutional Neural Network (CNN) with the following architecture:
- Convolutional layers with ReLU activation
- MaxPooling layers
- Fully connected (Dense) layers
- Softmax output layer

## Results

The trained model achieves high accuracy on the test set, demonstrating its effectiveness in recognizing sign language gestures. Detailed performance metrics and training progress can be found in the `results/` directory.
