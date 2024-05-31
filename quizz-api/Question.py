import json
import sqlite3

class Question():
    def __init__(self,position:int,Title:str,Content:str,Image:str,Id:int):
        self.position = position
        self.title = Title
        self.content = Content
        self.image = Image
        self.id = Id
    
    @staticmethod
    def ConvertToJson(question : 'Question'):
        Json = json.dumps({
            "position" : question.position,
            "title" : question.title,
            "content" : question.content,
            "image" : question.image,
            "id" : question.id
        })
        return Json
    
    @staticmethod
    def ConvertToPython(Json):
        return Question(position = Json["position"],
                        Title = Json["title"],
                        Content = Json["text"],
                        Image = Json["image"],
                        Id = -1)
    
    @staticmethod
    def AddQuestionToSql(question : 'Question'):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute(
            "INSERT INTO Questions (Position, Title, Content, Image) VALUES (?,?,?,?)",
            (question.position,question.title,question.content,question.image)
        )
        cur.execute("commit")
        question.id = cur.lastrowid

    @staticmethod
    def GetQuestionFromSqlId(id : int):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        sql_select_query = """select * from Questions where id = ?"""
        cur.execute(sql_select_query, (id,))
        records = cur.fetchall()
        return Question.TupleToJson(records[0])

    @staticmethod
    def GetQuestionFromSqlPosition(position : int):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        sql_select_query = """select * from Questions where position = ?"""
        cur.execute(sql_select_query, (position,))
        records = cur.fetchall()
        return Question.TupleToJson(records[0])

    @staticmethod
    def TupleToJson(data : tuple):
        Json = json.dumps({
            "position" : data[0],
            "title" : data[1],
            "text" : data[2],
            "image" : data[3],
            "id" : data[4]
        })
        return Json
    
    