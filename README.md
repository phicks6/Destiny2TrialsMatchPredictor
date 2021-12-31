# Destiny2TrialsMatchPredictor
For the final project in one of my classes I researched and created an AI to predict the outcome of matches. The AI takes the class (Hunter, Warlock, Titan) and the player's elo and predict which team will win.
For more information about the selection, training, and testing process for the model, you can read the report I wrote up for the class in ```Report.pdf```. 
The short version is that a random forest classifier with 750 estimators preformed the best with an accuracy of 84%. I later created a GUI around the best model for it to make playing around with it easier.

# Running
###### Option 1: TrialsMatchPredictor.py
Most versions of python3 should be able to run this, but I used python3.8.  
The required modules are listed in requirements.txt and can be installed with:
```pip install -r requirements.txt```  
Then just run the script with:
```python TrialsMatchPredictor.py```  
###### Option 2: EXE
I've packaged the project into a single file (TrailsMatchPredictor.exe) if you don't want to hassle with setting put a python environment.
The .exe was created from the following command:  
```pyinstaller --onefile -w TrialsMatchPredictor.py --hidden-import "sklearn.neighbors._partition_nodes" --add-data "random_forest.joblib;."```

# Using
Below is the GUI
![GUI](https://user-images.githubusercontent.com/9009879/147838993-4066241d-7da6-4d38-8214-3f4b05b459c8.PNG)
Select a class for each player and input their Trials of Osiris elos from https://destinytracker.com/. Then press predict to see the results.
