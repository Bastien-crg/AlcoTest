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
      console.log(participationStorageService.getToken())
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
    return this.call("get", "quiz-info", participationStorageService.getToken());
  },
  getQuestionByPos(position) {
    return this.call("get", "questions?position="+position, participationStorageService.getToken());
  },
  getQuestionByPos(position) {
    return this.call("get", "questions?position="+position, participationStorageService.getToken());
  },
  login() {
    let body = {
      "password": "flask2023"
    }
    return this.call("post", "login", body);
  },

};