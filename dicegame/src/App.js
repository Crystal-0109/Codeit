import { useState } from "react";
import Board from "./Board";
import Button from "./Button";


function random(n) {
  return Math.ceil(Math.random() * n);
}

function App() {
  const [num, setNum] = useState(1);  // 주사위 초깃값
  const [sum, setSum] = useState(0);  // 총점 초깃값
  const [gameHistory, setGameHistory] = useState([]);  // 기록 초깃값 배열로 생성
  const [otherNum, setOtherNum] = useState(1);  // 주사위 초깃값
  const [otherSum, setOtherSum] = useState(0);  // 총점 초깃값
  const [otherGameHistory, setOtherGameHistory] = useState([]);  // 기록 초깃값 배열로 생성

  const handleRollClick = () => { // 던지기 버튼
    const nextNum = random(6);
    const nextOtherNum = random(6);
    setNum(nextNum);
    setSum(sum + nextNum);
    setGameHistory([...gameHistory, nextNum]);
    setOtherNum(nextOtherNum);
    setOtherSum(otherSum + nextOtherNum);
    setOtherGameHistory([...otherGameHistory, nextOtherNum]);
  };

  const handleClearClick = () => { // 처음부터 버튼(초기화 버튼)
    setNum(1);
    setSum(0);
    setGameHistory([]);
    setOtherNum(1);
    setOtherSum(0);
    setOtherGameHistory([]);
  };

  return (
    <div>
      <Button onClick={handleRollClick}>던지기</Button>
      <Button onClick={handleClearClick}>처음부터</Button>
      <div>
        <Board name="나" color="blue" num={num} sum={sum} gameHistory={gameHistory} />
        <Board name="상대" color="red" num={otherNum} sum={otherSum} gameHistory={otherGameHistory} />
      </div>
    </div>
  );
}

export default App;