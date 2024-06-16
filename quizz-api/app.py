from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt_utils
import sqlite3
from Question import Question 
from Answer import Answer
from Score import Score
import json
from db import Database

app = Flask(__name__)
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    size = Question.GetNumOfQuestion()
    lst = Score.GetAllScore()
    return {"size": size, "scores": lst}, 200


@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()
	passwordUser = payload["password"]
	if(passwordUser == "flask2023"):
		token = jwt_utils.build_token()
		return jsonify({'token': token}), 200
	return 'Unauthorized', 401

@app.route('/questions', methods=['POST'])
def CreateQuestion():    
	if (request.headers.get('Authorization') == None):
		return 'Unauthorized', 401
	payload = request.get_json()
	question = Question.ConvertToPython(payload)
	print(question.content)
	Question.AddQuestionToSql(question)
	position = 1		
	for data in payload["possibleAnswers"]:
		anwser = Answer.ConvertToPython(data)
		anwser.questionId = question.id
		anwser.position = position
		Answer.AddAnswerToSql(anwser)
		position += 1	
	return {"id" : question.id}, 200
 
@app.route('/questions/<questionId>', methods=['GET'])
def GetQuestionInfo(questionId):
	Json = Question.GetQuestionFromSqlId(questionId)
	if(not Json):
		return "No Content", 404
	lst = Answer.GetListAnswerFromSqlQuestionId(questionId)
	dict1 = json.loads(Json)
	dict2 = json.loads(lst)
	merged_dict = {**dict1, **dict2}
	merged_json_str = json.dumps(merged_dict)
	return merged_json_str, 200


@app.route('/questions', methods=['GET'])
def GetQuestionInfoByPosition():
	bar = request.args.to_dict()
	Json = Question.GetQuestionFromSqlPosition(bar['position'])
	if(not Json):
		return "No Content", 404
	temp = json.loads(Json)
	lst = Answer.GetListAnswerFromSqlQuestionId(int(temp['id']))
	dict1 = json.loads(Json)
	dict2 = json.loads(lst)
	merged_dict = {**dict1, **dict2}
	merged_json_str = json.dumps(merged_dict)
	return merged_json_str, 200

@app.route('/questions/<questionId>', methods=['PUT'])
def UpdateQuestion(questionId):
	payload = request.get_json()
	bollean = Question.UpdateQuestion(questionId,payload)
	if(not bollean):
		return "No Content", 404
	Answer.UpdateAnswer(questionId,payload)
	return 'No content', 204

@app.route('/questions/<questionId>', methods=['DELETE'])
def DeleteQuestion(questionId):
	if (request.headers.get('Authorization') == None):
		return 'Unauthorized', 401
	if(not Question.IsQuestionExisting(questionId)):
		return "No Content", 404
	Answer.DeleteAnswer(questionId)
	Question.DeleteQuestion(questionId)
	return 'No content', 204

@app.route('/questions/all', methods=['DELETE'])
def DeleteAllQuestion():
	if (request.headers.get('Authorization') == None):
		return 'Unauthorized', 401
	Answer.DeleteAllAnswer()
	Question.DeleteAllQuestion()
	return 'No content', 204




@app.route('/participations/all', methods=['DELETE'])
def DeleteParticipations():
	if (request.headers.get('Authorization') == None):
		return 'Unauthorized', 401
	Score.DeleteAllScore()
	return 'No content', 204


@app.route('/participations', methods=['POST'])
def AddParticipation():
	payload = request.get_json()
	size = Question.GetNumOfQuestion()
	if(size != len(payload["answers"])):
		return "Bad request", 400
	score = 0
	anwserSummary = []
	for i in range(len(payload["answers"])):
		quest = Question.GetQuestionFromSqlPosition(i+1)
		dict1 = json.loads(quest)
		anwser = (Answer.GetCorrectAnswerPosition(dict1["id"]))
		anwserSummary.append((anwser["position"],payload["answers"][i]))
		if anwser["position"] == payload["answers"][i]:
			score += 1
	jsonScore = {"score": score}
	payload.update(jsonScore)
	Score.AddScoreToSql(Score.ConvertToPython(payload))
	return {"answersSummaries" : anwserSummary, "playerName" : payload["playerName"], "score" : score}, 200	

@app.route('/rebuild-db', methods=['POST'])
def BuildDatabase():
    db = Database(name="SQLBase.db")
    db.createDatabase()
    db.createDatabaseContent()
    return 'Ok', 200


if __name__ == "__main__":
    app.run()
    