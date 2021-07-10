import pandas as pd
import re

class ERA:
    def __init__(self):
        pass

    def eraFunct(self, col1,col2,col3,col4):

        yearVar = input("What year did you want to check on the ERA Leader? ")
        leagueVar = input("What league did you want to check on the ERA Leader, AL or NL? ")
        leagueVar = leagueVar.upper()

        if not re.search(r'\d{4}', yearVar):
            print("Please input a value 4 digit year")
            exit()
        if not re.search(r'[AL|NL]', leagueVar):
            print("Please input AL or NL for the league")
            exit() 
        if leagueVar == 'AL' and int(yearVar) < 1901:
            print("AL starts in 1901, enter a valid year")
            exit()
        
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

        if leagueVar == "NL":
            df = pd.read_html('https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_annual_ERA_leaders', header=0)[1]
            df['Year']=df.Year.astype(str)
            df = df[df['Year'].str.contains(yearVar)]
            return ("{} {}".format(df[[col1,col2,col3,col4]].head(1).to_string(index=False),"- "+leagueVar))

        if leagueVar == "AL":
            df = pd.read_html('https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_annual_ERA_leaders', header=0)[2]
            df['Year']=df.Year.astype(str)
            df = df[df['Year'].str.contains(yearVar)]
            return ("{} {}".format(df[[col1,col2,col3,col4]].head(1).to_string(index=False),"- "+leagueVar))
