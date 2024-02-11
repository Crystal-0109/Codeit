import './Button.css';

function Button({ children, onClick, color = 'blue' }) {
  const classNames = `Button ${color}`;
  return (
    <button className={classNames} onClick={onClick}>
      {children}
    </button>
  );
}

export default Button;