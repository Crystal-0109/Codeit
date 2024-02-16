function MBTIOption({ selected, label, value, onClick }) {
  const style = { fontWeight: selected ? 'bold' : 'normal' };

  return (
    <span style={style} onClick={onClick}>
      {label}
      {value}
    </span>
  );
}

export default MBTIOption;