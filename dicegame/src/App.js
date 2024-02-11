import { useState } from "react";
import Board from "./Board";
import Button from "./Button";
import './App.css';
import logo from './assets/logo.png';

function random(n) {
  return Math.ceil(Math.random() * n);
}

function App() {
  const [myHistory, setMyHistory] = useState([]);
  const [otherHistory, setOtherHistory] = useState([]);

  const handleRollClick = () => { // 던지기 버튼
    const nextMyNum = random(6);
    const nextOtherNum = random(6);
    setMyHistory([...myHistory, nextMyNum]);
    setOtherHistory([...otherHistory, nextOtherNum]);
  };

  const handleClearClick = () => { // 처음부터 버튼(초기화 버튼)
    setMyHistory([]);
    setOtherHistory([]);
  };

  return (
    
    <div className="App">
      <img className="App-logo" src={logo} alt="주사위 게임 로고" />
      <h1 className="App-title">주사위게임</h1>
      <Button className="App-button" color="blue" onClick={handleRollClick}>던지기</Button>
      <Button className="App-button" color="red" onClick={handleClearClick}>처음부터</Button>
      <div className="App-boards">
        <Board className="Board-heading" name="나" color="blue" gameHistory={myHistory} />
        <Board className="Board-heading" name="상대" color="red" gameHistory={otherHistory} />
      </div>
    </div>
  );
}

export default App;