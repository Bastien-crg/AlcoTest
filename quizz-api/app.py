from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt_utils
import sqlite3
from Question import Question 
from Answer import Answer

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
	request.headers.get('Authorization')
	
	payload = request.get_json() 
	print(payload)
	question = Question.ConvertToPython(payload)
	Question.AddQuestionToSql(question)		
	for data in payload["possibleAnswers"]:
		anwser = Answer.ConvertToPython(data)
		anwser.questionId = question.id
		Answer.AddAnswerToSql(anwser)
	return {"id" : question.id}, 200
 


if __name__ == "__main__":
    app.run()
    