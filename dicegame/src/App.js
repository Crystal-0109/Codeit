import Button from "./Button";
import Dice from "./Dice";

function App() {
  return (
  <div>
    <div>
      <Button text="던지기" />
      <Button text="처음부터" />
    </div>
    <Dice color="red" num={2} />
  </div>
  );
}

export default App;