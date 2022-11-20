import csv
#Toss winning stats
def toss_Win(team):
    total=0
    tosswon=0
    listtoss=[]
    with open(r'.\matches.csv') as csvfile:
         alldatafile=csv.DictReader(csvfile)
         for data in alldatafile:
             if team in [data['Team1'],data['Team2']]:
                 total+=1
                  if data['TOSS WINNER'] == team:
                      tosswon+=1

                 listtoss.append(total)
             listtoss.append(tosswon)
         return listtoss
#Yearwise matches played/won
def yearwise_Wonplayed(team):
    listResult = list()
    listYear = getyears()
    for year in listYear:
        with open(r'.\matches.csv') as csvfile:
             allDataFile = csv.DictReader
             total = 0
             won=0
        for data in allDataFile:
            if(team in [data['Team 1']],data['Team 2']]) , data['Team']==Year:
                Total+=1

                if data['WINNER'] == team:
                    won+=1
            listResult.append([year,total,won])
                    return listResult

#citywise matches played/won
def Citywise_Wonplayed(team):
    listResult = list()
    listcity = getcities()
    for year in listcity:
        with open (r'.\matches.csv') as csvfile:
             allDatafile = csv.DictReader(csvfile)
             total = 0
             won = 0

             for data in allDatafile:
                 if (team in [data['TEAM1'],data['TEAM2']]) and data['CITY'] == city:
                     total = 1
                     if data ['WINNER']== team:
                         won = 1
             listResult.append([city,total,won])
        return listResult

    def getYear():
        listSeason = set()
        with open(r'.\matches.csv') as csvfile:
            allDatafile = csv.Dictreader(csvfile)
            for data in allDatafile:
                listSeason.add(data['SEASON'])
        return list(listSeason)
    def getCities():
        listCity = set()
        with open (r'.\matches.csv')as csvfile:
            allDatafile = csv.DictReader(csvfile)
            for data in allDatafile:
                listCity.add(data['CITY'])
        return list (listCity)
    def readCSVfile():
        print('in readCSV')
        with open(r'.\matches.csv') as csvfile:
            allDataFile = csv.DictReader(csvfile)
        return allDataFile

    def showTeam():
        print('====TEAM====')
        listTeam = ['Mumbai Indians', 'Chennai Super Kings', 'Kolkata Knight Riders', 'Delhi Daredevils',
                    'Gujarat Lions', 'Sunrisers Hyderabad', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                    'Rajasthan Royals', 'Rising Pune Supergiants']
        dictTeam = dict(enumerate(listTeam, 1))
        value = True
        while value:
            printTeam(dictTeam)
            team = input('Enter a Team: ')
            validTeam = isValidTeam(team, dictTeam)
            if validTeam:
                value = False
            else:
                print('Invalid Team Choice')
        return dictTeam[team]

    def printTeam(dictTeam):
        for keys, Teams in dictTeam.items():
            print("%s. %s" % (keys, Teams))

    def isValidTeam(team, dictTeam):
        if team in dictTeam.keys():
            return True
        else:
            return False














