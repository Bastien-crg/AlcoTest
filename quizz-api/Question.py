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
        if(Question.GetQuestionFromSqlPosition(question.position)):
            db_connection = sqlite3.connect(f"SQLBase.db")
            cur = db_connection.cursor()
            cur.execute("begin")
            Question.UpdatePositionAllQuestion(99999,question.position,cur)
            cur.close()
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")        
        cur.execute(
            "INSERT INTO Questions (Position, Title, Content, Image) VALUES (?,?,?,?)",
            (question.position,question.title,question.content,question.image)
        )
        cur.execute("commit")
        cur.close()
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
        cur.execute("commit")
        cur.close()
        if(not Question.IsQuestionExisting(id)):
            return False
        return Question.TupleToJson(records[0])

    def GetPositionFromId(id :int):
        Json = Question.GetQuestionFromSqlId(id)
        if(not json):
            return False
        dict1 = json.loads(Json)
        return dict1['position']

    @staticmethod
    def GetQuestionFromSqlPosition(position : int):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        sql_select_query = """select * from Questions where Position = ?"""
        cur.execute(sql_select_query, (position,))
        records = cur.fetchall()
        cur.execute("commit")
        cur.close()
        if(records == []):
            return False
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
    
    
    @staticmethod
    def UpdateQuestion(id : int,Json : str):
        if(not Question.IsQuestionExisting(id)):
            return False     
        Question.UpdateValuesQuestion(Json,id) 
        return True     
        
        
    
    @staticmethod
    def UpdatePositionAllQuestion(oldPosition : int, newPosition : int,cur):
        if(oldPosition < newPosition):
            sql_select_query = """UPDATE questions
            SET position = position - 1
            WHERE position >= ? and position <= ?"""
            cur.execute(sql_select_query, (oldPosition,newPosition))
            cur.execute("commit")
        else:
            sql_select_query = """UPDATE questions
            SET position = position + 1
            WHERE position >= ? and position <= ?"""
            cur.execute(sql_select_query, (newPosition,oldPosition))
            cur.execute("commit")
        
        
    @staticmethod
    def UpdateValuesQuestion(Json : str,id : int):
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute('''
        UPDATE questions
        SET content = ?, title = ?, image = ?
        WHERE id = ?
        ''', (Json['text'],Json['title'],Json['image'], id))
        cur.execute("commit")
        cur.execute('''
        SELECT 1 FROM questions WHERE position = ? and id != ?
        ''', (Json['position'],id))
        if(cur.fetchone() is not None):
            Question.UpdatePositionAllQuestion(Question.GetPositionFromId(id),Json['position'],cur)
            cur.execute('''
            UPDATE questions
            SET position = ?
            WHERE id = ?
            ''', (Json['position'], id))
            cur.execute("commit")
        cur.close()
        
    @staticmethod
    def DeleteQuestion(id : int):
        if(not Question.IsQuestionExisting(id)):
            return False 
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        Question.UpdatePositionAllQuestion(Question.GetPositionFromId(id),999999,cur)    
        cur.execute('''
        DELETE FROM questions
        WHERE id = ?
        ''', (id,))
        cur.close()
        return True
        
    @staticmethod
    def DeleteAllQuestion():
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")    
        cur.execute('''
        DELETE FROM questions
        ''',)
        cur.execute("commit")   
        cur.close()
        
    @staticmethod
    def IsQuestionExisting(id : int,cur = False):
        db_connection = sqlite3.connect(f"SQLBase.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        sql_select_query = """SELECT 1 FROM Questions WHERE id = ?"""
        cur.execute(sql_select_query, (id,))
        if(cur.fetchone() is None):
            cur.execute("commit")
            cur.close()
            return False
        cur.execute("commit")
        cur.close()
        return True
    
    @staticmethod
    def GetNumOfQuestion():
        db_connection = sqlite3.connect(f"SQLBase.db")
        cur = db_connection.cursor()
        cur.execute("begin")  
        cur.execute(
            "SELECT COUNT(*) FROM Questions",
        )
        size = cur.fetchall()[0][0]
        cur.execute("commit")
        cur.close()
        return size
    