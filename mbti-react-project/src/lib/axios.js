import axios from "axios";

const instance = axios.create({
  baseURL: "http://learn.codeit.kr/api/",
});

export default instance;
