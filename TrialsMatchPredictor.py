import os
import sys
import joblib
import sklearn
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk


#Function used to append player info to one row for model
def playerAppend(master,player):
	for i in player:
		master.append(i)

#Class to hold onto predictionLabel so it can be destroyed when overwritten
class Predictor:

    def __init__(self, root):
        self.root = root
        self.model = joblib.load("random_forest.joblib") #Loads model from file
        self.predictionLabel =  tk.Label(self.root)
        self.predictionLabel.grid(row=9, column=1)

    #Triggered by predict button, displays team 1's chance to win
    def predict(self,team1Container,team2Container):
        #Remove the output of previous runs
        #self.predictionLabel.destroy()

        #Average elo and standard deviation of the dataset used to train the model
        avgElo = 1527
        stddev = 538.1244366499313

        player1 = []
        #Gets class from which button is pressed down
        if(team1Container[0]["HunterButton"].config('relief')[-1] == 'sunken'):
            player1 = [1,0,0]
        elif(team1Container[0]["WarlockButton"].config('relief')[-1] == 'sunken'):
            player1 = [0,1,0]
        elif(team1Container[0]["TitanButton"].config('relief')[-1] == 'sunken'):
            player1 = [0,0,1]
        else:
            self.predictionLabel.config(text="Player 1 missing class", font=("Arial", 10), fg="red")
            return

        #Gets elo from input field
        if(team1Container[0]["Elo"].get().isdigit()):
            elo = int(team1Container[0]["Elo"].get())
            player1.append((elo-avgElo)/stddev) #Standardizes elo 
        else:
            self.predictionLabel.config(text="Player 1 needs valid elo", font=("Arial", 10), fg="red")
            return
            

        player2 = []
        #Gets class from which button is pressed down
        if(team1Container[1]["HunterButton"].config('relief')[-1] == 'sunken'):
            player2 = [1,0,0]
        elif(team1Container[1]["WarlockButton"].config('relief')[-1] == 'sunken'):
            player2 = [0,1,0]
        elif(team1Container[1]["TitanButton"].config('relief')[-1] == 'sunken'):
            player2 = [0,0,1]
        else:
            self.predictionLabel.config(text="Player 2 missing class", font=("Arial", 10), fg="red")
            return

        #Gets elo from input field
        if(team1Container[1]["Elo"].get().isdigit()):
            elo = int(team1Container[1]["Elo"].get())
            player2.append((elo-avgElo)/stddev) #Standardizes elo 
        else:
            self.predictionLabel.config(text="Player 2 needs valid elo", font=("Arial", 10), fg="red")
            return
        

        player3 = []
        #Gets class from which button is pressed down
        if(team1Container[2]["HunterButton"].config('relief')[-1] == 'sunken'):
            player3 = [1,0,0]
        elif(team1Container[2]["WarlockButton"].config('relief')[-1] == 'sunken'):
            player3 = [0,1,0]
        elif(team1Container[2]["TitanButton"].config('relief')[-1] == 'sunken'):
            player3 = [0,0,1]
        else:
            self.predictionLabel.config(text="Player 3 missing class", font=("Arial", 10), fg="red")
            return

        #Gets elo from input field
        if(team1Container[2]["Elo"].get().isdigit()):
            elo = int(team1Container[2]["Elo"].get())
            player3.append((elo-avgElo)/stddev) #Standardizes elo 
        else:
            self.predictionLabel.config(text="Player 3 needs valid elo", font=("Arial", 10), fg="red")
            return
        


        player4 = []
        #Gets class from which button is pressed down
        if(team2Container[0]["HunterButton"].config('relief')[-1] == 'sunken'):
            player4 = [1,0,0]
        elif(team2Container[0]["WarlockButton"].config('relief')[-1] == 'sunken'):
            player4 = [0,1,0]
        elif(team2Container[0]["TitanButton"].config('relief')[-1] == 'sunken'):
            player4 = [0,0,1]
        else:
            self.predictionLabel.config(text="Player 4 missing class", font=("Arial", 10), fg="red")
            return

        #Gets elo from input field
        if(team2Container[0]["Elo"].get().isdigit()):
            elo = int(team2Container[0]["Elo"].get())
            player4.append((elo-avgElo)/stddev) #Standardizes elo 
        else:
            self.predictionLabel.config(text="Player 4 needs valid elo", font=("Arial", 10), fg="red")
            return

        player5 = []
        #Gets class from which button is pressed down
        if(team2Container[1]["HunterButton"].config('relief')[-1] == 'sunken'):
            player5 = [1,0,0]
        elif(team2Container[1]["WarlockButton"].config('relief')[-1] == 'sunken'):
            player5 = [0,1,0]
        elif(team2Container[1]["TitanButton"].config('relief')[-1] == 'sunken'):
            player5 = [0,0,1]
        else:
            self.predictionLabel.config(text="Player 5 missing class", font=("Arial", 10), fg="red")
            return

        #Gets elo from input field
        if(team2Container[1]["Elo"].get().isdigit()):
            elo = int(team2Container[1]["Elo"].get())
            player5.append((elo-avgElo)/stddev) #Standardizes elo 
        else:
            self.predictionLabel.config(text="Player 5 needs valid elo", font=("Arial", 10), fg="red")
            return

        player6 = []
        #Gets class from which button is pressed down
        if(team2Container[2]["HunterButton"].config('relief')[-1] == 'sunken'):
            player6 = [1,0,0]
        elif(team2Container[2]["WarlockButton"].config('relief')[-1] == 'sunken'):
            player6 = [0,1,0]
        elif(team2Container[2]["TitanButton"].config('relief')[-1] == 'sunken'):
            player6 = [0,0,1]
        else:
            self.predictionLabel.config(text="Player 6 missing class", font=("Arial", 10), fg="red")
            return

        #Gets elo from input field
        if(team2Container[2]["Elo"].get().isdigit()):
            elo = int(team2Container[2]["Elo"].get())
            player6.append((elo-avgElo)/stddev) #Standardizes elo 
        else:
            self.predictionLabel.config(text="Player 6 needs valid elo", font=("Arial", 10), fg="red")
            return
        
        
        #The model will give a slightly different answer based on where the players are placed on a team
        #The following code enumerates the match into the 72 possible different inputs based on the given players 
        team1 = [player1,player2,player3]
        team2 = [player4,player5,player6]
        matchEnumerated = []
        for i in range(3):
            for j in range(3):
                if(i != j):
                    for k in range(3):
                        if(k != i and k != j):
                            for x in range(3):
                                for y in range(3):
                                    if(x != y):
                                        for z in range(3):
                                            if(z != x and z!=y):
                                                temp = []
                                                playerAppend(temp,team1[i])
                                                playerAppend(temp,team1[j])
                                                playerAppend(temp,team1[k])
                                                playerAppend(temp,team2[x])
                                                playerAppend(temp,team2[y])
                                                playerAppend(temp,team2[z])
                                                matchEnumerated.append(temp)
        team1 = [player4,player5,player6]
        team2 = [player1,player2,player3]
        for i in range(3):
            for j in range(3):
                if(i != j):
                    for k in range(3):
                        if(k != i and k != j):
                            for x in range(3):
                                for y in range(3):
                                    if(x != y):
                                        for z in range(3):
                                            if(z != x and z!=y):
                                                temp = []
                                                playerAppend(temp,team1[i])
                                                playerAppend(temp,team1[j])
                                                playerAppend(temp,team1[k])
                                                playerAppend(temp,team2[x])
                                                playerAppend(temp,team2[y])
                                                playerAppend(temp,team2[z])
                                                matchEnumerated.append(temp)

        #This feeds the model all 72 matches
        results = self.model.predict_proba(matchEnumerated)

        #The first halve has team 1 as class 0, and the second halve has team 1 as class 1
        averageResult = 0
        firstHalf = results[0:36]
        secondHalf = results[36:]
        for result in firstHalf:
            averageResult+=result[0]
        for result in secondHalf:
            averageResult+=result[1]
        averageResult/=72

        #Display the prediction
        predictionStr = "Team 1 has a " + str(round((1-averageResult)*100,2))+"% chance to win."
        self.predictionLabel.config(text=predictionStr,font=("Arial", 13),fg="black")

#Causes the button to remain pressed and causes other buttons to raise
def press(player,type):
    if(type=="Hunter"):
        player["HunterButton"].config(relief="sunken")
        player["WarlockButton"].config(relief="raised")
        player["TitanButton"].config(relief="raised")
    if(type=="Warlock"):
        player["HunterButton"].config(relief="raised")
        player["WarlockButton"].config(relief="sunken")
        player["TitanButton"].config(relief="raised")
    if(type=="Titan"):
        player["HunterButton"].config(relief="raised")
        player["WarlockButton"].config(relief="raised")
        player["TitanButton"].config(relief="sunken")



def main():
    #Changes the directory if script has been packaged into an .exe
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)
    

    root = tk.Tk()
    root.title('Destiny 2 Trials of Osiris Match Predictor')
    root.geometry("800x500")
    predictor = Predictor(root)

    team1Label = tk.Label(root,text="Team 1",font=("Arial", 25))
    team1Label.grid(row=1,column=1)

    #Create input fields for player 1
    player1ButtonsFrame = tk.Frame(root, height=5,width=30,bg="green")
    player1EloFrame = tk.Frame(root, height=10,width=220,bg="blue")
    player1 = {
        "HunterButton": tk.Button(player1ButtonsFrame, text="Hunter", width=10, height=5, command=lambda: press(player1, "Hunter")),
        "WarlockButton": tk.Button(player1ButtonsFrame, text="Warlock", width=10, height=5, command=lambda: press(player1, "Warlock")),
        "TitanButton": tk.Button(player1ButtonsFrame, text="Titan", width=10, height=5, command=lambda: press(player1, "Titan")),
        "Elo": tk.Entry(player1EloFrame,width=40)
    }
    #Position input fields for player 1
    player1["HunterButton"].grid(row=1,column=0)
    player1["WarlockButton"].grid(row=1,column=1)
    player1["TitanButton"].grid(row=1,column=2)
    player1["Elo"].pack(padx=0,pady=0)
    player1ButtonsFrame.grid(row=2,column=0)
    player1EloFrame.grid(row=3,column=0)
    player1["Elo"].insert(0,"Enter Player's Elo")
    player1["Elo"].bind("<FocusIn>", lambda args: player1["Elo"].delete('0', 'end'))

    #Create input fields for player 2
    player2ButtonsFrame = tk.Frame(root, height=5,width=30,bg="green")
    player2EloFrame = tk.Frame(root, height=10,width=220,bg="blue")
    player2 = {
        "HunterButton": tk.Button(player2ButtonsFrame, text="Hunter", width=10, height=5, command=lambda: press(player2, "Hunter")),
        "WarlockButton": tk.Button(player2ButtonsFrame, text="Warlock", width=10, height=5, command=lambda: press(player2, "Warlock")),
        "TitanButton": tk.Button(player2ButtonsFrame, text="Titan", width=10, height=5, command=lambda: press(player2, "Titan")),
        "Elo": tk.Entry(player2EloFrame,width=40)
    }
    #Position input fields for player 2
    player2["HunterButton"].grid(row=1,column=0)
    player2["WarlockButton"].grid(row=1,column=1)
    player2["TitanButton"].grid(row=1,column=2)
    player2["Elo"].pack(padx=0,pady=0)
    player2ButtonsFrame.grid(row=2,column=1,padx=34)
    player2EloFrame.grid(row=3,column=1,padx=34)
    player2["Elo"].insert(0,"Enter Player's Elo")
    player2["Elo"].bind("<FocusIn>", lambda args: player2["Elo"].delete('0', 'end'))

    #Create input fields for player 3
    player3ButtonsFrame = tk.Frame(root, height=5,width=30,bg="green")
    player3EloFrame = tk.Frame(root, height=10,width=220,bg="blue")
    player3 = {
        "HunterButton": tk.Button(player3ButtonsFrame, text="Hunter", width=10, height=5, command=lambda: press(player3, "Hunter")),
        "WarlockButton": tk.Button(player3ButtonsFrame, text="Warlock", width=10, height=5, command=lambda: press(player3, "Warlock")),
        "TitanButton": tk.Button(player3ButtonsFrame, text="Titan", width=10, height=5, command=lambda: press(player3, "Titan")),
        "Elo": tk.Entry(player3EloFrame,width=40)
    }
    #Position input fields for player 3
    player3["HunterButton"].grid(row=1,column=0)
    player3["WarlockButton"].grid(row=1,column=1)
    player3["TitanButton"].grid(row=1,column=2)
    player3["Elo"].pack(padx=0,pady=0)
    player3ButtonsFrame.grid(row=2,column=2)
    player3EloFrame.grid(row=3,column=2)
    player3["Elo"].insert(0,"Enter Player's Elo")
    player3["Elo"].bind("<FocusIn>", lambda args: player3["Elo"].delete('0', 'end'))


    spacerFrame = tk.Frame(root, height=60)
    spacerFrame.grid(row=4,column=1)


    team2Label = tk.Label(root, text="Team 2",font=("Arial", 25))
    team2Label.grid(row=5,column=1)

    #Create input fields for player 4
    player4ButtonsFrame = tk.Frame(root, height=5,width=30,bg="green")
    player4EloFrame = tk.Frame(root, height=10,width=220,bg="blue")
    player4 = {
        "HunterButton": tk.Button(player4ButtonsFrame, text="Hunter", width=10, height=5, command=lambda: press(player4, "Hunter")),
        "WarlockButton": tk.Button(player4ButtonsFrame, text="Warlock", width=10, height=5, command=lambda: press(player4, "Warlock")),
        "TitanButton": tk.Button(player4ButtonsFrame, text="Titan", width=10, height=5, command=lambda: press(player4, "Titan")),
        "Elo": tk.Entry(player4EloFrame,width=40)
    }
    #Position input fields for player 4
    player4["HunterButton"].grid(row=1,column=0)
    player4["WarlockButton"].grid(row=1,column=1)
    player4["TitanButton"].grid(row=1,column=2)
    player4["Elo"].pack(padx=0,pady=0)
    player4ButtonsFrame.grid(row=6,column=0)
    player4EloFrame.grid(row=7,column=0)
    player4["Elo"].insert(0,"Enter Player's Elo")
    player4["Elo"].bind("<FocusIn>", lambda args: player4["Elo"].delete('0', 'end'))

    #Create input fields for player 5
    player5ButtonsFrame = tk.Frame(root, height=5,width=30,bg="green")
    player5EloFrame = tk.Frame(root, height=10,width=220,bg="blue")
    player5 = {
        "HunterButton": tk.Button(player5ButtonsFrame, text="Hunter", width=10, height=5, command=lambda: press(player5, "Hunter")),
        "WarlockButton": tk.Button(player5ButtonsFrame, text="Warlock", width=10, height=5, command=lambda: press(player5, "Warlock")),
        "TitanButton": tk.Button(player5ButtonsFrame, text="Titan", width=10, height=5, command=lambda: press(player5, "Titan")),
        "Elo": tk.Entry(player5EloFrame,width=40)
    }
    #Position input fields for player 5
    player5["HunterButton"].grid(row=1,column=0)
    player5["WarlockButton"].grid(row=1,column=1)
    player5["TitanButton"].grid(row=1,column=2)
    player5["Elo"].pack(padx=0,pady=0)
    player5ButtonsFrame.grid(row=6,column=1,padx=34)
    player5EloFrame.grid(row=7,column=1,padx=34)
    player5["Elo"].insert(0,"Enter Player's Elo")
    player5["Elo"].bind("<FocusIn>", lambda args: player5["Elo"].delete('0', 'end'))

    #Create input fields for player 6
    player6ButtonsFrame = tk.Frame(root, height=5,width=30,bg="green")
    player6EloFrame = tk.Frame(root, height=10,width=220,bg="blue")
    player6 = {
        "HunterButton": tk.Button(player6ButtonsFrame, text="Hunter", width=10, height=5, command=lambda: press(player6, "Hunter")),
        "WarlockButton": tk.Button(player6ButtonsFrame, text="Warlock", width=10, height=5, command=lambda: press(player6, "Warlock")),
        "TitanButton": tk.Button(player6ButtonsFrame, text="Titan", width=10, height=5, command=lambda: press(player6, "Titan")),
        "Elo": tk.Entry(player6EloFrame,width=40)
    }
    #Position input fields for player 6
    player6["HunterButton"].grid(row=1,column=0)
    player6["WarlockButton"].grid(row=1,column=1)
    player6["TitanButton"].grid(row=1,column=2)
    player6["Elo"].pack(padx=0,pady=0)
    player6ButtonsFrame.grid(row=6,column=2)
    player6EloFrame.grid(row=7,column=2)
    player6["Elo"].insert(0,"Enter Player's Elo")
    player6["Elo"].bind("<FocusIn>", lambda args: player6["Elo"].delete('0', 'end'))

    spacerFrame = tk.Frame(root, height=60)
    spacerFrame.grid(row=8,column=1)

    #Creates prediction button which calls predictor's predict
    predictButton = tk.Button(root, text="Predict",font=("Arial", 15), command=lambda: predictor.predict([player1,player2,player3],[player4,player5,player6]))
    predictButton.grid(row=9, column=0, sticky="W", padx=2)

    root.mainloop()


if __name__=="__main__":
    main()
