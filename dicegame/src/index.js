import ReactDOM from 'react-dom/client';

const root = ReactDOM.createRoot(document.getElementById('root'));

const product = "MacBook";

root.render(
  <h1>나만의 {product.toUpperCase()} 주문하기</h1>
  
);