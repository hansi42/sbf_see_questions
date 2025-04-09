import pandas as pd
import csv
import math
import random 
class Game:

    def __init__(self):
        self.data = pd.read_csv("data/sbf_fragen.csv", quotechar="|",  names=
                list(range(9))).to_numpy()



    def ask_random_question(self):
        
        q_number = random.randint(0, self.data.shape[0])
        self.ask_question(q_number)

    def ask_question(self, q_number):

        print("Frage:")
        print()
        print(self.data[q_number][1])
        print("\n")
        for i in range(6, len(self.data)):
            if (type(self.data[q_number][i])== float):
                break
            print(self.data[q_number][i])


        order = [2,3,4,5]
        random.shuffle(order)
        correct  = 0
        for i in range(len(order)):
            # because a is always right
            if order[i] == 2:
                correct = i
            print(str(i)+"): "+ self.data[q_number][order[i]])
        
        versuch = 2
        anzahl_versuche = 0
        while(True):
            try:
                answer = int(input("Wähle Zahl 0 - 3:\n>> "))
            except:
                print("Falsche eingabe getätigt!")
                continue
                
            if order[answer] == 2:
                print("Richtig")
                break
            else:
                print("Falsch")
                anzahl_versuche += 1
            if anzahl_versuche >= versuch:
                print("Zu Viele Fehler! 💀\nDie Antwort wäre:   " +
                        self.data[q_number][2])
                break
        


if __name__ == "__main__":
    g = Game()
    g.ask_random_question()

