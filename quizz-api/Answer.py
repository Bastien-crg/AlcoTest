import json
import sqlite3

class Answer():
    def __init__(self,questionId:int,Content:str,isCorrect : int,Id:int,position :int):
        self.questionId = questionId
        self.content = Content
        self.isCorrect = isCorrect
        self.id = Id
        self.position = position
    
    @staticmethod
    def ConvertToJson(anwser : 'Answer'):
        Json = json.dumps({
            "questionId" : anwser.questionId,
            "content" : anwser.content,
            "isCorrect" : anwser.isCorrect,
            "id" : anwser.id,
            "position" : anwser.position
        })
        return Json

    @staticmethod
    def ConvertToPython(Json):
        return Answer(questionId = -1,
                        Content = Json["text"],
                        isCorrect = Json["isCorrect"],
                        Id = -1,
                        position = -1)
    
    @staticmethod
    def AddAnswerToSql(anwser : 'Answer'):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute(
            "INSERT INTO Anwsers (questionId, Content, isCorrect, Position) VALUES (?,?,?,?)",
            (anwser.questionId,anwser.content,anwser.isCorrect,anwser.position)
        )
        cur.execute("commit")
        cur.close()
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
        cur.execute("commit")
        cur.close()
        lst = []
        for data in records:
            lst.append(Answer.TupleToJson(data))
        return json.dumps({"possibleAnswers" : lst})

    def GetCorrectAnswerPosition(QuestionId : int):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        sql_select_query = """select * from Anwsers where questionId = ? and IsCorrect = 1"""
        cur.execute(sql_select_query, (QuestionId,))
        records = cur.fetchall()
        cur.execute("commit")
        cur.close()
        return Answer.TupleToJson(records[0])

    @staticmethod
    def TupleToJson(data : tuple):
        Json = {
            "id" : data[1],
            "text" : data[2],
            "isCorrect" : bool(data[3]),
            "position" : data[4],
        }
        return Json
    
    @staticmethod
    def UpdateAnswer(questionId : int,Json : str):   
        position = 1 
        Answer.DeleteAnswer(questionId)
        for data in Json["possibleAnswers"]:
            anwser = Answer.ConvertToPython(data)
            anwser.questionId = questionId
            anwser.position = position
            Answer.AddAnswerToSql(anwser)
            position += 1
        
        
            
    @staticmethod
    def DeleteAnswer(questionId : int):
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")     
        cur.execute('''
        DELETE FROM Anwsers
        WHERE questionId = ?
        ''', (questionId,))
        cur.execute("commit")
        cur.close()
        
    @staticmethod
    def DeleteAllAnswer():
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")     
        cur.execute('''
        DELETE FROM Anwsers
        ''',)
        cur.execute("commit")
        cur.close()
        

        