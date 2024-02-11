import ReactDOM from 'react-dom/client';

const root = ReactDOM.createRoot(document.getElementById('root'));

const product = "MacBook";
const model = " Air";
const item = product + model;
const imageUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/MacBook_with_Retina_Display.png/500px-MacBook_with_Retina_Display.png";

root.render(
  <>
    <h1>나만의 {item} 주문하기</h1>
    <img src={imageUrl} alt='제품 사진' />
  </>
  
);