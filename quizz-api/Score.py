import json
import sqlite3

class Score():
    def __init__(self,name:str,date:str,score:int,id:int):
        self.name = name
        self.date = date
        self.score = score
        self.id = id
    
    @staticmethod
    def ConvertToJson(score : 'Score'):
        Json = json.dumps({
            "Name" : score.position,
            "Date" : score.title,
            "Score" : score.content,
            "id" : score.id
        })
        return Json
    
    @staticmethod
    def ConvertToPython(Json):
        return Score(name = Json["Name"],
                        Date = Json["Date"],
                        Score = Json["Score"],
                        Id = -1)
    
    @staticmethod
    def AddScoreToSql(score : 'Score'):
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")        
        cur.execute(
            "INSERT INTO Score (Name, Date, Score) VALUES (?,?,?)",
            (score.name,score.date,score.score)
        )
        cur.execute("commit")
        cur.close()
        score.id = cur.lastrowid
        
    @staticmethod
    def DeleteAllScore():
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute("DELETE * FROM Score")
        cur.execute("commit")
        cur.close()

    