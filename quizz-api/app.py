from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt_utils
import sqlite3
from Question import Question 
from Answer import Answer
import json

app = Flask(__name__)
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200


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
	Question.AddQuestionToSql(question)		
	for data in payload["possibleAnswers"]:
		anwser = Answer.ConvertToPython(data)
		anwser.questionId = question.id
		Answer.AddAnswerToSql(anwser)
	return {"id" : question.id}, 200
 
@app.route('/questions/<questionId>', methods=['GET'])
def GetQuestionInfo(questionId):
	Json = Question.GetQuestionFromSqlId(questionId)
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
	Question.UpdateQuestion(questionId,payload)
	Answer.UpdateAnswer(questionId,payload)
	return 'No content', 204

@app.route('/questions/<questionId>', methods=['DELETE'])
def DeleteQuestion(questionId):
	if (request.headers.get('Authorization') == None):
		return 'Unauthorized', 401
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

if __name__ == "__main__":
    app.run()
    