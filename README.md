# RoomsClassifier

*Room Classifier* is a machine learning system that is used to identify and categorize images of different rooms. This system is built using TensorFlow, a popular open-source software library for machine learning. The primary goal of this classifier is to accurately recognize different types of rooms based on their visual characteristics, such as furniture, flooring, and wall colors.


![CNN](https://user-images.githubusercontent.com/97985464/214332583-2642de92-8539-4824-80d4-9aacf175dad0.jpg)

## Installing libraries

To execute this project you will need to install all the libraries that are specified in the requeriments.txt document. 

There are two options to install the libraries:

- Install all libraries using `pip` by executing:

```bash
pip install -r requirements.txt
```

- Create a `Conda` environment by using:

```bash
conda create --name <env> --file requirements.txt
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
