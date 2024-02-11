import ReactDOM from 'react-dom/client';

const root = ReactDOM.createRoot(document.getElementById('root'));

function Hello() {
  return <h1>안녕 리액트</h1>;
}

const element = (
  <>
    <Hello />
    <Hello />
    <Hello />    
  </>
)

root.render(
  element
  
);