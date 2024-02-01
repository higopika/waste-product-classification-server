- How to start the server ?

1. Create a virtual enviroment - python3 -m venv venv
2. Activate the virtual enviroment - source venv/bin/activate
3. Install the requirements'txt file - pip install -r requirements.txt
4. Download the dataset data.zip (https://drive.google.com/drive/folders/1DKgp7wyM6SoV-sTBTUAjZkEsC_Nzt4I_?usp=drive_link
) and store it in data folder (create a folder with the name "data")
6. Initialize dvc using the command - dvc init
7. Type the command - dvc dag - to see the stages of the project
8. To run the experiment - dvc exp run


REFERENCES

Installations that were required to solve errors 

dvc - pip install dvc

for prepare.py 

to use python type hinting example - list[str] we need to install version of python greater than 3.9
installation link - https://phoenixnap.com/kb/upgrade-python

for train.py file

- pandas  pip install pandas
- torch    pip install torchvision 
- opencv   pip install opencv-python  

DATASET PREPARATION

Prepare.py file will split the data in the data.zip file into test and train

1. Collected images were labelled using label-studio and were compressed into data.zip file. 
   Label Studio is used to generate the labels
   It should contain 4 files 
- images - contains all the images
- labels - contains txt files contains class, bounding box coordintes info
- classes.txt - contains the names of all the classes
- notes.json - contains all the classes with their corresponding ids in json format

2. Collected images and compressed images are present in this link - https://drive.google.com/drive/folders/1DKgp7wyM6SoV-sTBTUAjZkEsC_Nzt4I_?usp=drive_link
3. The rename_file.py file is a utility program that was used in data preparation.
