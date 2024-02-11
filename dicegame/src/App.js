import { useState } from "react";
import Button from "./Button";
import Dice from "./Dice";


function random(n) {
  return Math.ceil(Math.random() * n);
}

function App() {
  const [num, setNum] = useState(1);  // 주사위 초깃값
  const [sum, setSum] = useState(0);  // 총점 초깃값
  const [gameHistory, setGameHistory] = useState([]);  // 기록 초깃값 배열로 생성

  const handleRollClick = () => { // 던지기 버튼
    const nextNum = random(6);
    setNum(nextNum);
    setSum(sum + nextNum);
    gameHistory.push(nextNum);
    setGameHistory(gameHistory);
  }

  const handleClearClick = () => { // 처음부터 버튼(초기화 버튼)
    setNum(1);
    setSum(0);
    setGameHistory([]);
  } 

  return (
  <div>
    <div>
      <Button onClick={handleRollClick}>던지기</Button>
      <Button onClick={handleClearClick}>처음부터</Button>
    </div>
    <div>
      <h2>나</h2>
      <Dice color="blue" num={num} />
      <h2>총점</h2>
      <p>{sum}</p>
      <h2>기록</h2>
      <p>{gameHistory.join(', ')}</p>
    </div>
  </div>
  );
}

export default App;