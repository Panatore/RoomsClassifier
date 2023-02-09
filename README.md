# RoomsClassifier

*Room Classifier* is a machine learning system that is used to identify and categorize images of different rooms. This system is built using TensorFlow, a popular open-source software library for machine learning. The primary goal of this classifier is to accurately recognize different types of rooms based on their visual characteristics, such as furniture, flooring, and wall colors.

In the methodology for this room image classifier project, we initially utilized a Convolutional Neural Network (CNN) to classify the images. However, upon obtaining an accuracy of 70%, we decided to implement additional machine learning techniques and statistical methodologies to improve the performance of the model.

To achieve this, we utilized Image Data Generator and Transfer Learning techniques. The Image Data Generator was used to augment the data by applying various transformations, such as rotation and scaling, to the images to increase the diversity of the data and reduce overfitting. Transfer learning allowed us to take the pre-trained weights of a larger model and fine-tune them on our smaller dataset. This allowed us to leverage the knowledge of the pre-trained model, while also making the most of our smaller dataset.

These techniques, when combined with the original CNN model, resulted in a significant improvement in accuracy, as well as a more robust and generalizable model, obtaining an accuracy of over 93%. The methodology and results of these techniques are described in detail in the code notebooks, available in the repository.


![CNN](https://user-images.githubusercontent.com/97985464/214332583-2642de92-8539-4824-80d4-9aacf175dad0.jpg)

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
3. Replace myenv with the name you want to give to your virtual environment.

4. Activate the virtual environment by running the following command:
```bash
conda activate myenv
```
Verify that the virtual environment is activated by checking the command prompt. It should display the name of the virtual environment in brackets at the beginning of the line.
#### Using virtualenv
1. Open your terminal or command prompt.
2. Navigate to your project's directory using the cd command.
3. Run the following command to create a virtual environment:
```bash
python3 -m venv myenv
```
Replace myenv with the name you want to give to your virtual environment.

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
git clone https://github.com/your-repo-link
```
2. Navigate to the project directory:
```bash
cd your-project-directory
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
## Download Data and Model

Using these link you can download a zip with all the Data used for the creation of the model [Data](https://drive.google.com/file/d/1hXXvO09P8IV6dR8dquvwP1ACy4osZNat/view?usp=share_link "Click here to Download") and the model that you can use with Keras [Model](https://drive.google.com/file/d/1F4WHTeUOoD53BqTvAk0MqmFfq-_Jcidd/view?usp=share_link "Click here to Download").

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
python streamlit run webapp.py
```

This webapp shows us how the user experience will improve using the room image classifier. The room image classifier makes the real estate advertisement creation process even more efficient and user-friendly. The classifier allows users to easily label each room in the property, providing a clear and organized way for potential buyers to view the layout of the property. The labeling process is quick and simple, and the classifier accurately identifies the different rooms in the property, reducing the need for manual input from the user. This feature enhances the visual appeal of the advertisement, making it easier for potential buyers to understand the property layout. The improved organization and visual appeal provided by the room image classifier increase the chances of attracting more potential buyers and ultimately lead to a successful sale. The addition of this feature further demonstrates the webapp's commitment to providing an enhanced user experience and making the process of advertising real estate properties easier and more efficient.

The architecture of the webapp comprises a two-page interface, where the first page is dedicated to the creation of a real estate advertisement. The user is prompted to provide detailed information regarding the property, including its operational status, price, location, street address, and a comprehensive description. The user is also able to upload relevant images to accompany the advertisement, enhancing its visual appeal and providing potential buyers with a comprehensive understanding of the property.

The second page of the webapp serves as the display platform for the created advertisement. Once the advertisement has been created, it is promptly displayed on this page, showcasing all the information and images provided by the user in an organized and visually appealing manner. The display page serves as the main platform for potential buyers to interact with the advertisement and gain a comprehensive understanding of the property being offered for sale.

