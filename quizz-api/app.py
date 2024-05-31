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
	Json = Question.GetQuestionFromSql(questionId)
	lst = Answer.GetListAnswerFromSql(questionId)
	dict1 = json.loads(Json)
	dict2 = json.loads(lst)
	merged_dict = {**dict1, **dict2}
	merged_json_str = json.dumps(merged_dict)
	print(merged_json_str)
	return merged_json_str, 200

if __name__ == "__main__":
    app.run()
    