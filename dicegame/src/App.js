import { useState } from "react";
import Button from "./Button";
import Dice from "./Dice";


function random(n) {
  return Math.ceil(Math.random() * n);
}

function App() {
  const [num, setNum] = useState(1);  // 초깃값
  const [sum, setSum] = useState(0);

  const handleRollClick = () => { // 던지기 버튼
    const nextNum = random(6);
    setNum(nextNum);
    setSum(sum + nextNum);
  }

  const handleClearClick = () => { // 처음부터 버튼(초기화 버튼)
    setNum(1);
    setSum(0);
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
    </div>
  </div>
  );
}

export default App;