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

    @staticmethod
    def GetListAnswerFromSqlQuestionId(id : int):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        sql_select_query = """select * from Anwsers where questionId = ?"""
        cur.execute(sql_select_query, (id,))
        records = cur.fetchall()
        lst = []
        for data in records:
            lst.append(Answer.TupleToJson(data))
        return json.dumps({"possibleAnswers" : lst})

    @staticmethod
    def TupleToJson(data : tuple):
        Json = {
            "is" : data[1],
            "text" : data[2],
            "isCorrect" : bool(data[3]),
        }
        return Json
    
    @staticmethod
    def UpdateAnswer(questionId : int,Json : str):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")      
        cur.execute('''
        DELETE FROM Anwsers
        WHERE questionId = ?
        ''', (questionId,))
        cur.execute("commit")
        for data in Json["possibleAnswers"]:
            anwser = Answer.ConvertToPython(data)
            anwser.questionId = questionId
            Answer.AddAnswerToSql(anwser)
        

        