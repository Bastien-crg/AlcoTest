import json
import sqlite3

class Answer():
    def __init__(self,questionId:int,Content:str,isCorrect : int,Id:int):
        self.questionId = questionId
        self.content = Content
        self.isCorrect = isCorrect
        self.id = Id
    
    @staticmethod
    def ConvertToJson(anwser : 'Answer'):
        Json = json.dumps({
            "questionId" : anwser.questionId,
            "content" : anwser.content,
            "isCorrect" : anwser.isCorrect,
            "id" : anwser.id
        })
        return Json

    @staticmethod
    def ConvertToPython(Json):
        return Answer(questionId = -1,
                        Content = Json["text"],
                        isCorrect = Json["isCorrect"],
                        Id = -1)
    
    @staticmethod
    def AddAnswerToSql(anwser : 'Answer'):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute(
            "INSERT INTO Anwsers (questionId, Content, isCorrect) VALUES (?,?,?)",
            (anwser.questionId,anwser.content,anwser.isCorrect)
        )
        cur.execute("commit")
        anwser.id = cur.lastrowid

