# Heart Disease Prediction❤️🩺

![Heart Disease Prediction](https://img.shields.io/badge/HeartDisease-Prediction-brightgreen)

## Overview

The Heart Disease Prediction project leverages machine learning algorithms to predict the presence of heart disease in patients. The goal is to provide a tool that can assist healthcare professionals in diagnosing heart disease early, thereby potentially saving lives through timely intervention.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Cardiovascular diseases are a leading cause of death globally. Early detection of heart disease can significantly improve the treatment outcome. This project uses machine learning techniques to predict the likelihood of heart disease based on various medical attributes.

## Dataset 📊

The dataset used for this project is the [Cleveland Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease) available from the UCI Machine Learning Repository. It includes the following attributes:

- Age
- Sex
- Chest pain type (4 values)
- Resting blood pressure
- Serum cholesterol in mg/dl
- Fasting blood sugar > 120 mg/dl
- Resting electrocardiographic results (values 0, 1, 2)
- Maximum heart rate achieved
- Exercise-induced angina
- ST depression induced by exercise relative to rest
- The slope of the peak exercise ST segment
- Number of major vessels (0-3) colored by fluoroscopy
- Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)

## Installation 🛠️

1. Clone the repository:

    ```bash
    git clone https://https://github.com/lokesh182/Heart-Disease-Prediction.git
    cd Heart-Disease-Prediction
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage 🚀

1. Ensure that you have the dataset in the `data` folder. If not, download it from [here](https://archive.ics.uci.edu/ml/datasets/Heart+Disease).
2. Run the heartdisease.ipynb to train model and perform EDA:

## Model 🤖

The project explores various machine learning algorithms including:

- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

The final model is selected based on its performance metrics such as accuracy, precision, recall, and F1 score.

## Results 📈

The model achieves the following accuracy:

Random Forest:98%

![heart](image.png)



## Contributing 🤝

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License 📄

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

## Contact 📧

For any questions or feedback, please contact:

- **Your Name** - [lokesh18.ml@gmail.com](mailto:lokesh18.ml@gmail.com)
- GitHub: [lokesh182](https://github.com/lokesh182)
