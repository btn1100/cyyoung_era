import pandas as pd
import re

class CYYOUNG:
    def __init__(self):
        pass
    def cyFunct(self,col1,col2,col3,col4,col5,col6):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

        yearVar = input("What year did you want to check on the Cy Young Winner? ")
        if int(yearVar) < 1967:
            print("The League Cy Young awards started in 1967, input a valid year")
            exit()
        if not re.search(r'\d{4}', yearVar):
            print("Please input a value 4 digit year")
            exit()


        leagueVar = input("What league did you want to check on the Cy Young Winner, AL or NL? ")
        leagueVar = leagueVar.upper()

        if not re.search(r'[AL|NL]', leagueVar):
            print("Please input AL or NL for the league ")
            exit()

        if leagueVar == "AL":
            df = pd.read_html('https://en.wikipedia.org/wiki/Cy_Young_Award', header=0)[3]
            df['Year']=df.Year.astype(str)
            df = df[df['Year'].str.contains(yearVar)]
            return ("{} {}".format(df[[col1,col2,col3,col4,col5,col6]].head(1).to_string(index=False), "- "+leagueVar))

        if leagueVar == "NL":
            df = pd.read_html('https://en.wikipedia.org/wiki/Cy_Young_Award', header=0)[4]
            df['Year']=df.Year.astype(str)
            df = df[df['Year'].str.contains(yearVar)]
            return ("{} {}".format(df[[col1,col2,col3,col4,col5,col6]].head(1).to_string(index=False), "- "+leagueVar))
