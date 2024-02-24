import axios from "axios";

const instance = axios.create({
  baseURL: "http://learn.codeit.kr/api/codeitmall",
});

export default instance;
