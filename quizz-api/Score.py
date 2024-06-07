import json
import sqlite3
import datetime

class Score():
    def __init__(self,name:str,date:str,score:int,id:int):
        self.name = name
        self.date = date
        self.score = score
        self.id = id
    
    @staticmethod
    def ConvertToJson(score : 'Score'):
        Json = json.dumps({
            "playerName" : score.position,
            "Date" : score.title,
            "score" : score.content,
            "id" : score.id
        })
        return Json
    
    @staticmethod
    def ConvertToPython(Json):
        return Score(name = Json["playerName"],
                    date = datetime.datetime.now(),
                    score = Json["score"],
                    id = -1)
        
    
    @staticmethod
    def AddScoreToSql(score : 'Score'):
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")       
        
        cur.execute(
            "INSERT INTO Score (playerName, Date, score) VALUES (?,?,?)",
            (score.name,score.date,score.score)
        )
        cur.execute("commit")
        cur.close()
        score.id = cur.lastrowid 
        return score
        
        
    @staticmethod
    def DeleteAllScore():
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute("DELETE FROM Score")
        cur.execute("commit")
        cur.close()

    @staticmethod
    def GetNumOfScore():
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")  
        cur.execute(
            "SELECT COUNT(*) FROM Score",
        )
        size = cur.fetchall()[0][0]
        cur.execute("commit")
        cur.close()
        return size
    
    @staticmethod
    def GetAllScore():
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")  
        cur.execute(
            "SELECT playerName,score,date,id FROM Score ORDER BY score DESC",
        )
        scores = cur.fetchall()
        cur.execute("commit")
        cur.close()
        lst = []
        for data in scores:
            lst.append(participationResult(name=data[0],score=data[1],date=data[2]).ConvertToJson())
        return lst
    
class participationResult:
    def __init__(self,name:str,date:str,score:int):
        self.name = name
        self.date = date
        self.score = score
        
    def ConvertToJson(self):
        Json = {
            "playerName" : self.name,
            "Date" : self.date,
            "score" : self.score,
        }
        return Json
        
    
    