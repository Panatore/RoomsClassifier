# RoomsClassifier

*Room Classifier* is a machine learning system that is used to identify and categorize images of different rooms. This system is built using TensorFlow, a popular open-source software library for machine learning. The primary goal of this classifier is to accurately recognize different types of rooms based on their visual characteristics, such as furniture, flooring, and wall colors.

In the methodology for this room image classifier project, we initially utilized a Convolutional Neural Network (CNN) to classify the images. However, upon obtaining an accuracy of 70%, we decided to implement additional machine learning techniques and statistical methodologies to improve the performance of the model.

To achieve this, we utilized Image Data Generator and Transfer Learning techniques. The Image Data Generator was used to augment the data by applying various transformations, such as rotation and scaling, to the images to increase the diversity of the data and reduce overfitting. Transfer learning allowed us to take the pre-trained weights of a larger model and fine-tune them on our smaller dataset. This allowed us to leverage the knowledge of the pre-trained model, while also making the most of our smaller dataset.

These techniques, when combined with the original CNN model, resulted in a significant improvement in accuracy, as well as a more robust and generalizable model, obtaining an accuracy of over 93%. The methodology and results of these techniques are described in detail in the code notebooks, available in the repository.


![CNN](https://user-images.githubusercontent.com/97985464/214332583-2642de92-8539-4824-80d4-9aacf175dad0.jpg)

## Repository Files
This repository contains several files, each with its own specific purpose:

1. `GetImagesGoogle.py`: This file allow us to download images from Google Images and save them to a new directory.

2. `webapp.py`: This file contains the code for the Streamlit webapp that allows users to interact with the room classifier. It provides a two-page interface for creating and displaying real estate advertisements.

3. `fine_tuning.py`: This file allow us to test different hyperpharameters from your transfer learning and fine tuning room classifier model.

4. `TFM.ipynb`: This is the jupyter notebook where all the data exploration and models are created.

5. `requirements.txt`: This file lists the required Python packages for running the code in this repository.

By understanding the purpose and functionality of each file, users can easily navigate the repository and understand how to use the room classifier and the webapp.

This project requires Python 3.9 to be installed on your system.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Make sure you have Python 3.9 and either [conda](https://docs.conda.io/en/latest/miniconda.html "Click here to Download") or [virtualenv](https://virtualenv.pypa.io/en/latest/ "Click here to Download") installed on your system.. You can check your Python version by running the following command in your terminal:
```bash
python3 --version
```
If you do not have Python 3.9 installed, you can download it from the official Python website [here](https://www.python.org/downloads/ "Click here to Download").
### Setting up a Virtual Environment
You can choose to create a virtual environment using either conda or virtualenv.

#### Using conda
1. Open your terminal or command prompt.
2. Run the following command to create a virtual environment with Python 3.9:
```bash
conda create --name myenv python=3.9
```
Replace `myenv` with the name you want to give to your virtual environment.

4. Activate the virtual environment by running the following command:
```bash
conda activate myenv
```
4. Verify that the virtual environment is activated by checking the command prompt. It should display the name of the virtual environment in brackets at the beginning of the line.
#### Using virtualenv
1. Open your terminal or command prompt.
2. Navigate to your project's directory using the cd command.
3. Run the following command to create a virtual environment:
```bash
python3 -m venv myenv
```
Replace `myenv` with the name you want to give to your virtual environment.

4. Activate the virtual environment by running the following command:
```bash
source myenv/bin/activate
```
Note: If you're on Windows, the activation command is slightly different:
```Powershell
myenv\Scripts\activate
```
5. Verify that the virtual environment is activated by checking the command prompt. It should display the name of the virtual environment in brackets at the beginning of the line.
### Installing the Project
Once you have activated your virtual environment, you can install the project and its dependencies by following these steps:

1. Clone the project repository:
```bash
git clone https://github.com/Panatore/RoomsClassifier
```
2. Navigate to the project directory:
```bash
cd RoomsClassifier
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
## Download Data and Model

Using these link you can download a zip with all the Data used for the creation of the model [Data](https://drive.google.com/file/d/1hXXvO09P8IV6dR8dquvwP1ACy4osZNat/view?usp=share_link "Click here to Download") and the model that you can use with Keras [Model](https://drive.google.com/file/d/1FRWTe81bn64uXbORmbTcUCF2IU0VM-J-/view?usp=share_link "Click here to Download").

Once you have downloaded the zip folder you must unzip it in the same directory where the repository has been cloned. Using the next code.

In case you are using Bash:
```bash
unzip data.zip
unzip Models.zip
```
In case you are using PowerShell:
```powershell
Expand-Archive .\data.zip
Expand-Archive .\Models.zip
```

## Execute the webapp

In case you want to deploy the Streamlit app,first you need to download the model following the instructions explained in the previous section (Download Data and Model) and then you will need to execute the next commnand while you are in the same directory where the file *webapp.py* is.

```bash
streamlit run webapp.py
```

This webapp shows us how the user experience will improve using the room image classifier. The room image classifier makes the real estate advertisement creation process even more efficient and user-friendly. The classifier allows users to easily label each room in the property, providing a clear and organized way for potential buyers to view the layout of the property. The labeling process is quick and simple, and the classifier accurately identifies the different rooms in the property, reducing the need for manual input from the user. This feature enhances the visual appeal of the advertisement, making it easier for potential buyers to understand the property layout. The improved organization and visual appeal provided by the room image classifier increase the chances of attracting more potential buyers and ultimately lead to a successful sale. The addition of this feature further demonstrates the webapp's commitment to providing an enhanced user experience and making the process of advertising real estate properties easier and more efficient.

The architecture of the webapp comprises a two-page interface, where the first page is dedicated to the creation of a real estate advertisement. The user is prompted to provide detailed information regarding the property, including its operational status, price, location, street address, and a comprehensive description. The user is also able to upload relevant images to accompany the advertisement, enhancing its visual appeal and providing potential buyers with a comprehensive understanding of the property.

The second page of the webapp serves as the display platform for the created advertisement. Once the advertisement has been created, it is promptly displayed on this page, showcasing all the information and images provided by the user in an organized and visually appealing manner. The display page serves as the main platform for potential buyers to interact with the advertisement and gain a comprehensive understanding of the property being offered for sale.

## Future Enhancements
Although the room classifier and the webapp provide a useful solution for creating real estate advertisements, there is always room for improvement. Here are a few potential enhancements that could be made in the future:

1. Integration with other real estate platforms: Integrating the room classifier and the webapp with other real estate platforms will increase its visibility and reach, making it easier for potential buyers to access and view the advertisements.

2. Adding more room categories: Currently, the room classifier supports a limited number of room categories. Adding more room categories will increase its accuracy and provide a more comprehensive labeling system.

3. Improving the user interface: Enhancing the user interface of the webapp will make the creation and display of advertisements even more user-friendly and visually appealing.

4. Adding more features: Adding features such as virtual tours, property videos, and more will provide potential buyers with a more immersive experience and a better understanding of the property being offered for sale.

These are just a few examples of the potential enhancements that could be made in the future. The goal of the room classifier and the webapp is to simplify the process of advertising real estate properties and make it more efficient and user-friendly. By continuously improving and adding new features, we aim to achieve this goal and provide the best possible solution for our users.
