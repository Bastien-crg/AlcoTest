import axios from "axios";
import participationStorageService from "@/services/ParticipationStorageService";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*"
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestionByPos(position) {
    return this.call("get", "questions?position=" + position);
  },
  deleteQuestionById(questionId) {
    return this.call("delete", "questions/" + questionId, null, participationStorageService.getToken());
  },
  sendAnswer(playerName, answers) {
    let body = {
      "playerName": playerName,
      "answers": answers
    }
    console.log(body)
    return this.call("post", "participations", body);
  },
  login(password) {
    let body = {
      "password": password
    }
    return this.call("post", "login", body);
  },

};