# RoomsClassifier

*Room Classifier* is a classifier of room images


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

## Execute the webapp

In case you want to deploy the Streamlit app, you will need to execute the next commnand while you are in the same directory where the file *webapp.py* is.

```bash
python streamlit run webapp.py
```
